import util

import os

LINK_FILES = [('tmux.conf',        '~/.tmux.conf'),
              ('tmux',             '~/.tmux')]


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
    return True

__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']

