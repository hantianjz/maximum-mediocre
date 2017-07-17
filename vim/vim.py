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

neovim=False

def _install_github_bundle(user, package):
    if not os.path.exists(os.path.expanduser("~/.vim/bundle/%s" % package)):
        cmd_str = "git clone https://github.com/%s/%s.git %s/.vim/bundle/%s" % (user, package, util.get_home_path(), package)
        subprocess.check_call(cmd_str.split())


def install(neovim=False):
    for orig, dest in LINK_FILES:
        orig = os.path.join(os.path.dirname(__file__), orig)
        dest = util.fix_home_path(dest)
        print orig, dest
        util.link_file(orig, dest)
    _install_github_bundle("VundleVim", "Vundle.vim")
    # Install all the plugins using vundle
    subprocess.check_call('nvim +PluginInstall +qall'.split())


def uninstall():
    raise NotImplementedError()


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    return git.checkdeps()


__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']
