import sys
import os

import subprocess

from util import util

LINK_FILES = [
    # GIT
    ('gitconfig', '~/.gitconfig'),
    ('gitignore', '~/.gitignore'),

    # ZSH
    ('zlogin', '~/.zlogin'),
    ('zlogout', '~/.zlogout'),
    ('zpreztorc', '~/.zpreztorc'),
    ('zprofile', '~/.zprofile'),
    ('zshenv', '~/.zshenv'),
    ('zshrc', '~/.zshrc'),

    # BASH
    ('profile', '~/.profile'),
    ('bashrc', '~/.bashrc'),
]

PACKAGES = [('https://github.com/oahzjh/prezto.git', '~/.zprezto', None),
            ('https://github.com/junegunn/fzf.git', '~/.fzf/',
             '~/.fzf/install')]


def _download_git_repo(git_url, install_folder, install_script):
    print("install github at: %s" % install_folder)
    if not os.path.exists(install_folder):
        cmd_str = "git clone --depth 1 --recursive %s %s" % (git_url,
                                                             install_folder)
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

    if install_script:
        old_cwd = os.getcwd()
        try:
            os.chdir(install_folder)
            subprocess.check_call(install_script.split())
        finally:
            os.chdir(old_cwd)


def install():
    # Make symlink to files
    for orig, dest in LINK_FILES:
        orig = os.path.join(os.path.dirname(__file__), "shellrc", orig)
        dest = util.fix_home_path(dest)
        util.link_file(orig, dest)

    # Download git repo to destination location
    for git_url, install_folder, install_script in PACKAGES:
        install_folder = os.path.abspath(util.fix_home_path(install_folder))
        if install_script:
            install_script = os.path.abspath(
                util.fix_home_path(install_script))
        _download_git_repo(git_url, install_folder, install_script)


def uninstall():
    raise NotImplementedError()


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    return True


__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']
