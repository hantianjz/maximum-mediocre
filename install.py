#!/usr/bin/python

import subprocess
import os

HOME_DIR = os.path.expanduser("~")

PACKAGE_LIST = ["cmake",
                "vim-gnome",
                "python-pip",
                "silversearcher-ag",
                "pass",
                "git",
                "zsh",
                ]

LINK_FILES = [('vim',              '~/.vim'),
              ('vim',              '~/.config/nvim'),
              ('vimrc',            '~/.vimrc'),
              ('tmux.conf',        '~/.tmux.conf'),
              ('vimrc.bundles',    '~/.vimrc.bundles')
              ]


def run_cmd(cmd_str):
    subprocess.call(cmd_str.split())


def install_github_bundle(user, package):
    if not os.path.exists(os.path.expanduser("~/.vim/bundle/%s" % package)):
        cmd_str = "git clone https://github.com/%s/%s.git %s/.vim/bundle/%s" % (user, package, HOME_DIR, package)
        run_cmd(cmd_str)


def package_install():
    for package in PACKAGE_LIST:
        run_cmd("sudo apt-get install %s -y" % package)


def link_files():
    for orig, dest in LINK_FILES:
        dest = dest.replace("~", HOME_DIR)
        orig = os.path.abspath(orig)
        if not os.path.exists(dest):
            os.symlink(orig, dest)


def main():
    run_cmd("sudo apt-get update && sudo apt-get upgrade")
    package_install()
    install_github_bundle("VundleVim", "Vundle.vim")
    run_cmd('vim +PluginInstall +qall')
    link_files()


if __name__ == "__main__":
    main()
