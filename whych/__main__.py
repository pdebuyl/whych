"""
A module to find the location of other modules. The main use is to diagnose
installation problems.
"""
from . import whych

if __name__ == '__main__':
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

    whych(module=args.module, sys_path=args.sys_path,
          module_version=args.module_version)
