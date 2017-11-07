from util import util

import subprocess
import re

import os

LINK_FILES = [('gitconfig',        '~/.gitconfig')]
GIT_EXECUTABLE_STR = "git"

def install():
    for orig, dest in LINK_FILES:
        orig = os.path.join(os.path.dirname(__file__), orig)
        dest = util.fix_home_path(dest)
        util.link_file(orig, dest)


def uninstall():
    raise NotImplementedError()


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    try:
        subprocess.check_call("which %s" % GIT_EXECUTABLE_STR, shell=True)
    except subprocess.CalledProcessError as e:
        print "%s not found" % GIT_EXECUTABLE_STR
        return False

    try:
        version_str = subprocess.check_output("%s --version" % GIT_EXECUTABLE_STR, shell=True)
    except subprocess.CalledProcessError as e:
        print "%s failed to fetch version!" % GIT_EXECUTABLE_STR
        return False

    # extract the version details
    version = re.match("git version (?P<major>\d+).(?P<minor>\d+).(?P<patch>\d+)", version_str)
    print "git version %s" % repr(version.groupdict())

    return True


__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']
