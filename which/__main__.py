"""
A module to find the location of other modules. The main use is to diagnose
installation problems.
"""
from __future__ import print_function

if __name__ == '__main__':
    import imp
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('module')
    args = parser.parse_args()

    print(imp.find_module(args.module))

