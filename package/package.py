#!/usr/bin/env python
import brew
import aptitude

import util

import argparse

import os
import sys

PACKAGE_LIST = ["cmake",
                "vim",
                "python-pip",
                "silversearcher-ag",
                "pass",
                "git",
                "zsh",
                "tmux"
                ]

package_manager = None

def _get_package_manager():
    if not package_manager:
        if sys.platform == "darwin":
            package_manager = new brew.Brew()
        else sys.platform == "linux2":
            package_manager = new aptitude.Aptitude()
    return package_manager


def _package_install():
    # Update packages
    run_cmd("apt-get update");
    for package in PACKAGE_LIST:
        run_cmd("apt-get install %s -y" % package)


def install():
    raise NotImplementedError()


def uninstall():
    raise NotImplementedError()


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    raise NotImplementedError()


__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']
