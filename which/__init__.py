"""
A module to find the location of other modules. The main use is to diagnose
installation problems.
"""
from __future__ import print_function
import imp
import sys

__version__ = '0.2-dev'

def which(module, sys_path=False, module_version=False):
    print("Python executable:", sys.executable)
    if sys_path:
        print("System path:", sys.path)
    try:
        file, pathname, description = imp.find_module(module)
    except:
        print("""Module "{}" not found""".format(module))
        return

    print("""Module "{}" found at location: {}""".format(module,
                                                         pathname))
    if module_version:
        mod = imp.load_module(module, file, pathname, description)
        if hasattr(mod, '__version__'):
            print("""{} version: {}""".format(module, mod.__version__))
        else:
            print('Module has no __version__ information')
