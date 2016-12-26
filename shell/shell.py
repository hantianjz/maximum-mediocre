import util

import subprocess

import sys
import os

LINK_FILES = [('alias',        '~/.alias')]

def install():
    print "Linking folders"
    # Install alias folder
    for orig, dest in LINK_FILES:
        orig = os.path.join(os.path.dirname(__file__), orig)
        dest = util.fix_home_path(dest)
        util.link_file(orig, dest)

    shell = os.path.basename(os.environ["SHELL"])

    # Include shell settings by adding sourcing line
    local_rc = "%s.%s.local" % (sys.platform, shell)
    source_local_rc_str = "source ~/.bashrc.local"
    util.link_file(os.path.join(os.path.dirname(__file__), local_rc),
                   util.fix_home_path("~/.bashrc.local"))

    # Add souce line to *rc files
    rc_file_name = os.path.abspath(os.path.join(util.get_home_path(), ".%src" % shell))
    print "checking if rc file exist: %s" % rc_file_name
    if os.path.exists(rc_file_name):
        try:
            # some bash string escaping, hopefully it works for zsh
            subprocess.check_output("grep '%s' %s" % (source_local_rc_str, rc_file_name), shell=True)
        except subprocess.CalledProcessError as e:
            print "sourcing alias dir in %s" % rc_file_name
            rc_file = open(rc_file_name, "a")
            rc_file.write(source_local_rc_str)
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

