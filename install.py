#!/usr/bin/python2

import argparse
import importlib

import os

MODULE_LIST = ["package", "vim", "tmux", "git", "shell"]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", default=False)
    for module in MODULE_LIST:
        parser.add_argument("--%s" % module, action="store_true", default=False)
    return parser.parse_args()


def import_modules(args):
    imported_modules = []
    for module in MODULE_LIST:
        attr = getattr(args, module)
        if attr or args.all:
            imported_modules.append(importlib.import_module("..%s" % module, "%s.%s" % (module, module)))

    return imported_modules


def main():
    imported_modules = import_modules(get_args())
    for module in imported_modules:
        try:
            if module.checkdeps():
                module.install()
        except NotImplementedError as e:
            print "module: %s exception: %s" % (repr(module), e)


if __name__ == "__main__":
    main()
