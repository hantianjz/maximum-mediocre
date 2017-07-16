import sys
import os

import subprocess

from util import util

class ShellRC(object):

    def __init__(self, shell):
        self.shell = shell

        # Get absolute path of the shellrc file
        self.rc_file = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "shellrc",
                "shellrc.%s" % shell)

        # The souce line to *rc files
        self.source_str = "source %s" % self.rc_file

        # Get absolute path of the target shell rc file
        self.target_rc_file = os.path.join(util.get_home_path(), ".%src" % shell)


    """ Include shellrc.* to corresponding rc file """
    def install(self):
        if not os.path.isfile(self.rc_file):
            print "%s not a file or does not exist, skipping setup for _%s_" % (self.rc_file, shell)
            return

        # Add souce line to *rc files
        if os.path.exists(self.target_rc_file):
            print "target shell rc file %s exist" % self.target_rc_file

            # TODO: more intelligent search and append/replace
            if not util.str_exist_in_file(self.target_rc_file, self.source_str):
                print "Append line \"%s\"" % self.source_str
                util.append_str_into_file(self.target_rc_file, self.source_str)
            else:
                print "Already exist line \"%s\"" % self.source_str
        else:
            print "%s does not exist, creating!" % self.target_rc_file
            util.append_str_into_file(self.target_rc_file, self.source_str)


    def uninstall(self):
        if os.path.exists(self.target_rc_file):
            print "target shell rc file %s exist" % self.target_rc_file
            print "Removing line \"%s\"" % self.source_str
            util.remove_str_into_file(self.target_rc_file, self.source_str)


SHELLRCS = [ShellRC("bash"), ShellRC("zsh")]


def install():
    for shell in SHELLRCS:
        if shell.get_shell_path():
            shell.install()


def uninstall():
    for shell in SHELLRCS:
        shell.uninstall()


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    for shell in SHELLRCS:
        print "Current shell: %s" % shell.get_shell_path()
        return True if shell.get_shell_path() else False


__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']

