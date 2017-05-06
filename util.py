import os


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
    print "symlinked %s -> %s" % (orig, dest)
