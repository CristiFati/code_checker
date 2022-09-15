# Code checker


Created this repository when working on [\[GitHub\]: belangeo/pyo - Fix for #241: Python 3.10 breaks SfPlayer](https://github.com/belangeo/pyo/pull/248).

**WILL ADD MORE DETAILS**

**Note**: **File patterns must follow [\[Python.Docs\]: glob.glob(pathname, \*, root_dir=None, dir_fd=None, recursive=False)](https://docs.python.org/3/library/glob.html#glob.glob) rules** (might be confusing for some users used to *Shell* patterns style)

**Example** (that I worked on):

```
[cfati@cfati-5510-0:/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src]> git show --summary
commit 5602a73c27043862e8e5a614547e448546c257ee (HEAD -> cfati_dev03, upstream/master, origin/master, origin/HEAD, master)
Merge: 7aeb2e88 04ae8fdd
Author: Olivier Bélanger <belangeo@gmail.com>
Date:   Tue May 17 11:53:06 2022 -0400

    Merge branch 'master' of https://github.com/belangeo/pyo

[cfati@cfati-5510-0:/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src]> python ../../code_checker/src/src/check.py -c ../../code_checker/src/src/configs/PY_SSIZE_T_CLEAN__PyO.yaml -p "**/*.c" -o kkt.json
Python 3.8.10 (default, Jun 22 2022, 20:18:18) [GCC 9.4.0] 064bit on linux

Found 18 occurrences (7 files) in 2.696 seconds

File /mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/engine/midilistenermodule.c:
  Line(s): 685
File /mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/engine/pyomodule.c:
  Line(s): 352, 443, 520, 762, 890
File /mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/engine/servermodule.c:
  Line(s): 1868, 2317
File /mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/objects/fftmodule.c:
  Line(s): 3892
File /mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/objects/recordmodule.c:
  Line(s): 149
File /mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/objects/sfplayermodule.c:
  Line(s): 356, 436, 1338, 2206
File /mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/objects/tablemodule.c:
  Line(s): 4370, 4598, 4618, 4645

Done.

[cfati@cfati-5510-0:/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src]> cat kkt.json
{
  "/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/engine/midilistenermodule.c": [
    [
      "PyArg_ParseTuple(args, \"s#li\", &msg, &size, &timestamp, &device)",
      685
    ]
  ],
  "/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/engine/pyomodule.c": [
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"s#|i\", kwlist, &path, &psize, &print)",
      352
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"Os#|iiiid\", kwlist, &samples, &recpath, &psize, &sr, &channels, &fileformat, &sampletype, &quality)",
      443
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"Os#|iid\", kwlist, &table, &recpath, &psize, &fileformat, &sampletype, &quality)",
      520
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"s#s#|ii\", kwlist, &inpath, &psize, &outpath, &psize2, &up, &order)",
      762
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"s#s#|ii\", kwlist, &inpath, &psize, &outpath, &psize2, &down, &order)",
      890
    ]
  ],
  "/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/engine/servermodule.c": [
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"|s#\", kwlist, &filename, &psize)",
      1868
    ],
    [
      "PyArg_ParseTuple(args, \"s#l\", &msg, &size, &timestamp)",
      2317
    ]
  ],
  "/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/objects/fftmodule.c": [
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"Os#|OiiOO\", kwlist, &inputtmp, &self->impulse_path, &psize, &baltmp, &self->size, &self->chnl, &multmp, &addtmp)",
      3892
    ]
  ],
  "/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/objects/recordmodule.c": [
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"Os#|iiiid\", kwlist, &input_listtmp, &self->recpath, &psize, &self->chnls, &fileformat, &sampletype, &self->buffering, &quality)",
      149
    ]
  ],
  "/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/objects/sfplayermodule.c": [
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, TYPE_P__OIFI, kwlist, &self->path, &psize, &speedtmp, &self->loop, &offset, &self->interp)",
      356
    ],
    [
      "PyArg_ParseTuple(args, \"s#\", &self->path, &psize)",
      436
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"s#O|Oi\", kwlist, &self->path, &psize, &markerstmp, &speedtmp, &self->interp)",
      1338
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, \"s#O|OOi\", kwlist, &self->path, &psize, &markerstmp, &speedtmp, &marktmp, &self->interp)",
      2206
    ]
  ],
  "/mnt/e/Work/Dev/GitHub/CristiFati/pyo/src/src/objects/tablemodule.c": [
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, TYPE_P_IFF, kwlist, &self->path, &psize, &self->chnl, &self->start, &self->stop)",
      4370
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, TYPE_P_IFF, kwlist, &self->path, &psize, &self->chnl, &self->start, &stoptmp)",
      4598
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, TYPE_P_FIFF, kwlist, &self->path, &psize, &crosstmp, &self->chnl, &self->start, &stoptmp)",
      4618
    ],
    [
      "PyArg_ParseTupleAndKeywords(args, kwds, TYPE_P_FFIFF, kwlist, &self->path, &psize, &postmp, &crosstmp, &self->chnl, &self->start, &stoptmp)",
      4645
    ]
  ]
}
```

