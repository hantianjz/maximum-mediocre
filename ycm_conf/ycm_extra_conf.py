import ycm_normal_conf
import ycm_riker_conf


def FlagsForFile(filename, **kwargs):
    if ycm_riker_conf.IsRiker(filename):
        return ycm_riker_conf.FlagsForFile(filename, kwargs)
    else:
        return ycm_normal_conf.FlagsForFile(filename, kwargs)
