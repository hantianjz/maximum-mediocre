#!/usr/bin/env python
import brew
import aptitude
import pacman

import util

import argparse

import os
import sys
import distro

PACKAGE_LIST = [
    "cmake", "vim", "python-pip", "silversearcher-ag", "pass", "git", "zsh",
    "tmux"
]

package_manager = []


def _get_package_manager():
    if package_manager:
        return package_manager

    if sys.platform == "darwin":
        package_manager = brew.Brew()
    elif sys.platform == "linux":
        distro_name, _, _ = distro.linux_distribution()
        if distro_name == 'Arch Linux':
            package_manager = aptitude.Pacman()
        elif distro_name == 'Ubuntu':
            package_manager = aptitude.Aptitude()
    else:
        raise NotImplementedError()
    return package_manager


def install():
    pg = _get_package_manager()

    for item in PACKAGE_LIST:
        pg.install(item)


def uninstall():
    raise NotImplementedError()


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    raise NotImplementedError()


__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']
