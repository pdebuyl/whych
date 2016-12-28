"""
A module to find the location of other modules. The main use is to diagnose
installation problems.
"""
from __future__ import print_function

if __name__ == '__main__':
    import imp
    import argparse
    import sys
    import os.path

    prog = "{} -m {}".format(os.path.basename(sys.executable), __package__)

    parser = argparse.ArgumentParser(prog=prog, description=__doc__)
    parser.add_argument('module', help='name of module to look for')
    parser.add_argument('--sys-path', action='store_true',
                        help='show the python package path sys.path')
    parser.add_argument('--module-version', action='store_true',
                        help="""show the version of the module if found (this
                        option causes the module to load)""")
    args = parser.parse_args()

    print("Python executable:", sys.executable)
    if args.sys_path:
        print("""System path:""")
        print(sys.path)
    try:
        file, pathname, description = imp.find_module(args.module)
    except:
        print("""Module "{}" not found""".format(args.module))
        sys.exit(0)

    print("""Module "{}" found at location: {}""".format(args.module,
                                                         pathname))
    if args.module_version:
        module = imp.load_module(args.module, file, pathname, description)
        if hasattr(module, '__version__'):
            print("""{} version: {}""".format(args.module, module.__version__))
        else:
            print('Module has no __version__ information')
