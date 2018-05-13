from util import util

import subprocess
import os

LINK_FILES = [('tmux.conf',        '~/.tmux.conf'),
              ('dot_tmux',             '~/.tmux')]

def _install_tpm(rootdir, user, package):
    install_folder = os.path.expanduser("%s/plugins/%s" % (rootdir, package))
    print "install github at: %s" % install_folder
    if not os.path.exists(install_folder):
        cmd_str = "git clone --recursive https://github.com/%s/%s.git %s" % (user, package, install_folder)
        subprocess.check_call(cmd_str.split())
    else:
        old_cwd = os.getcwd()
        try:
            os.chdir(install_folder)
            cmd_str = "git pull"
            subprocess.check_call(cmd_str.split())
            cmd_str = "git submodule update --init --recursive"
            subprocess.check_call(cmd_str.split())
        finally:
            os.chdir(old_cwd)


def _install():
    for orig, dest in LINK_FILES:
        orig = os.path.join(os.path.dirname(__file__), orig)
        _install_tpm("dot_tmux", "tmux-plugins", "tpm")
        dest = util.fix_home_path(dest)
        util.link_file(orig, dest)


def install():
    old_cwd = os.getcwd()
    try:
        os.chdir(os.path.dirname(__file__))
        _install()
    finally:
        os.chdir(old_cwd)


def uninstall():
    raise NotImplementedError()


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    return True

__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']

