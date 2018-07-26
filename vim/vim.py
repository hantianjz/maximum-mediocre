from git import git
from util import util

import subprocess
import os

LINK_FILES = [('dot_vim',          '~/.vim'),
              ('dot_vim',          '~/.config/nvim'),
              ('vimrc',            '~/.config/nvim/init.vim'),
              ('vimrc',            '~/.vimrc'),
              ('vimrc',            '~/.config/nvim/init.vim'),
              ('vimrc.bundles',    '~/.vimrc.bundles'),
              ]

def _install_github_bundle(rootdir, user, package):
    install_folder = os.path.expanduser("%s/bundle/%s" % (rootdir, package))
    print("install github at: %s" % install_folder)
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

    if package == "YouCompleteMe":
        old_cwd = os.getcwd()
        try:
            os.chdir(install_folder)
            cmd_str = "python install.py --clang-completer --system-libclang"
            subprocess.check_call(cmd_str.split())
        finally:
            os.chdir(old_cwd)


def _install():
    try:
        os.makedirs("dot_vim/backup")
    except OSError as e:
        print(e)

    f_bundles = open("vimrc.bundles")
    for bundle in f_bundles:
        bundle = bundle.split()[1].strip("'")
        github_user = bundle.split("/")[0].strip()
        package = bundle.split("/")[1].strip()
        _install_github_bundle("dot_vim", github_user, package)

    for orig, dest in LINK_FILES:
        orig = os.path.join(os.path.dirname(__file__), orig)
        dest = util.fix_home_path(dest)
        print(orig, dest)
        util.link_file(orig, dest)


def install():
    old_cwd = os.getcwd()
    try:
        os.chdir(os.path.dirname(__file__))
        _install()
    finally:
        os.chdir(old_cwd)


def uninstall():
    for _, sym_link in LINK_FILES:
        sym_link_path = util.fix_home_path(sym_link)
        os.remove(sym_link_path)


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    return git.checkdeps()


__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']
