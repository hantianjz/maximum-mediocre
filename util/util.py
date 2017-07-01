import os

import mmap

def get_home_path():
    return os.path.expanduser("~")


def fix_home_path(path):
    return path.replace("~", get_home_path())


def link_file(orig, dest):
    try:
        os.remove(dest)
    except Exception:
        pass
    os.symlink(orig, dest)
    # print "symlinked %s -> %s" % (orig, dest)


def str_exist_in_file(filename, string):
    with open(filename, "r") as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(string.encode("utf-8")) != -1:
            return True
        else:
            return False
