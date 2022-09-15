#!/usr/bin/env python

import argparse
import glob
import json
import os
import re
import sys
import time
import yaml
from pprint import pprint as pp


CFG_KEY_AND = "and"
CFG_KEY_OR = "or"
CFG_KEY_RE = "re"
CFG_KEYS = (
    CFG_KEY_AND,
    CFG_KEY_OR,
    CFG_KEY_RE,
)

KEY_ROOT = "root"


def parse_args(*argv):
    parser = argparse.ArgumentParser(description="Code checker")
    parser.add_argument("--cfg", "-c", required=True, help="search criteria .yaml file")
    parser.add_argument("--pattern", "-p", action="append", default=[], dest="patterns", required=True,
                        help="file pattern to search for. Can be specified multiple times. \
                        Must follow https://docs.python.org/3/library/glob.html#glob.glob rules")
    parser.add_argument("--out_file", "-o", help="write results to file instead stdout")
    parser.add_argument("--verbose", "-v", action="store_true", help="verbose mode")
    args, unk = parser.parse_known_args()

    if unk:
        print("Warning - Ignoring unknown args: {:}".format(unk))
    if not os.path.isfile(args.cfg):
        parser.exit(status=-1, message="Config file not found\n")
    return args.cfg, args.patterns, args.out_file, args.verbose


def validate_config(cfg, level=0):
    if isinstance(cfg, dict):
        if len(cfg) != 1:
            return "Key count", level
        key = list(cfg.keys())[0]
        if key.lower() not in CFG_KEYS:
            return "Key name", level
        val = cfg[key]
        if key.lower() == CFG_KEY_RE:
            if not isinstance(val, str):
                return "Value type", level
        else:
            if not isinstance(val, (list, tuple)):
                return "Value (sequence) type", level
            for item in val:
                res = validate_config(item, level=level + 1)
                if res:
                    return res
    else:
        if not isinstance(cfg, str):
            return "Element type", level
    return None, -1


def parse_config(cfg):
    if isinstance(cfg, dict):
        key = list(cfg.keys())[0]
        val = cfg[key]
        if key == CFG_KEY_AND:
            return ".*?".join(parse_config(item) for item in val).join("()")
        elif key == CFG_KEY_OR:
            return ")|(".join(parse_config(item) for item in val).join(("((", "))"))
        elif key == CFG_KEY_RE:
            return val
    else:
        return re.escape(cfg)


def process_file(file_name, criteria):
    matches = []
    txt = open(file_name).read()
    idx = 0
    while True:
        mat = criteria.search(txt[idx:])
        if not mat:
            break
        grp = mat.group()
        idx = txt.index(grp, idx)
        matches.append((grp, txt[:idx].count("\n") + 1))
        idx += len(grp)

    return os.path.abspath(file_name), tuple(matches)


def process_pattern(file_pattern, criteria):
    ret = {}
    for item in sorted(glob.iglob(file_pattern, recursive=True)):
        fname, matches = process_file(item, criteria)
        if matches:
            ret[fname] = matches
    return ret


def main(*argv):
    cfg_file, patterns, out_file, verbose = parse_args()

    try:
        cfg = yaml.safe_load(open(cfg_file))[KEY_ROOT]
    except:
        print("Error loading config")
        return -1
    #print(cfg)
    if not cfg:
        print("Invalid config")
        return -2
    vc = validate_config(cfg)
    if vc[0]:
        print(vc)
        return -3
    cr = parse_config(cfg)
    if verbose:
        print("Search pattern text: {:s}\n".format(cr))
    crit = re.compile(cr)
    data = {}
    time_start = time.time()

    for pat in patterns:
        data.update(process_pattern(pat, crit))
    print("Found {:d} occurrences ({:d} files) in {:.3f} seconds\n".format(
        sum(len(e) for e in data.values()), len(data), time.time() - time_start))

    for k, v in data.items():
        print("File {:s}:\n  Line(s): {:s}".format(k, str([e[1] for e in v])[1:-1]))
    if out_file:
        json.dump(data, open(out_file, mode="w", newline="\n"), indent=2)
    else:
        if verbose:
            print()
            pp(data, indent=2, sort_dicts=False)


if __name__ == "__main__":
    print("Python {:s} {:03d}bit on {:s}\n".format(" ".join(elem.strip() for elem in sys.version.split("\n")),
                                                   64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    rc = main(*sys.argv[1:])
    print("\nDone.\n")
    sys.exit(rc)

