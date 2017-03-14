# whych

**Author:** Pierre de Buyl
**License:** 3-clause BSD

A tool to locate the Python modules that your interpreter has access to.

`whych` is *only* run as a "command-line module" and not as a standalone
executable, so that the Python interpreter that is used is obvious.

Examples:

```
$ python3 -m whych collections
Python executable: /usr/bin/python3
Module "collections" found at location: /usr/lib/python3.5/collections
```

```
$ python -m whych numpy --module-version
Python executable: /usr/bin/python
Module "numpy" found at location: /usr/lib/python2.7/dist-packages/numpy
numpy version: 1.12.0b1
```
