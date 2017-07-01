import sys
import os

import subprocess

from util import util


def install():
    shells = ["bash", "zsh"]
    for shell in shells:
        # Include shellrc.* to corresponding rc file

        # Get absolute path of the shellrc file
        shellrc_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "shellrc", "shellrc.%s" % shell)

        if not os.path.isfile(shellrc_file):
            print "%s not a file or does not exist, skipping setup for _%s_" % (shellrc_file, shell)
            continue

        # Get absolute path of the target shell rc file
        target_rc_file = os.path.join(util.get_home_path(), ".%src" % shell)

        # TODO: more intelligent search and insert/replace
        insert_string = "source %s" % shellrc_file
        # Add souce line to *rc files
        if os.path.exists(target_rc_file):
            print "target shell rc file %s exist" % target_rc_file

            if not util.str_exist_in_file(target_rc_file, insert_string):
                print "inserting line \"%s\"" % insert_string
                rc_file = open(target_rc_file, "a")
                rc_file.write(insert_string)
                rc_file.close()
            else:
                print "Already exist line \"%s\"" % insert_string
        else:
            print "%s does not exist, creating!" % target_rc_file
            rc_file = open(target_rc_file, "a")
            rc_file.write(insert_string)
            rc_file.close()


def uninstall():
    raise NotImplementedError()


def verify():
    raise NotImplementedError()


def dryrun():
    raise NotImplementedError()


def checkdeps():
    shell = os.environ["SHELL"]
    print "Current shell: %s" % shell
    return True if shell else False


__all__ = ['install', 'uninstall', 'verify', 'dryrun', 'checkdeps']

