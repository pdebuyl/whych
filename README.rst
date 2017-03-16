whych
=====

A tool to locate the Python modules that your interpreter has access to.

whych is only run as a "command-line module" with the ``-m`` flag to the Python
interpreter, from the REPL or from a notebook.  whych is not as a standalone
executable, so that the Python interpreter that is used is obvious.

Examples
--------

From the command-line::

    $ python3 -m whych collections
    Python executable: /usr/bin/python3
    Module "collections" found at location: /usr/lib/python3.5/collections


    $ python -m whych numpy --module-version
    Python executable: /usr/bin/python
    Module "numpy" found at location: /usr/lib/python2.7/dist-packages/numpy
    numpy version: 1.12.0b1

From an interpreter::

    >>> import whych
    >>> whych.whych('pip')
    Python executable: /usr/bin/python3
    Module "pip" found at location: /home/pierre/.local/lib/python3.5/site-packages/pip

Installation
------------

    pip install whych

