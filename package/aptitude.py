import package_manager

import util

class Aptitude(package_manager.PackagerManager):

    CMD_STR = "aptitude"

    def __init__():
        raise NotImplementedError()

    def exist(package):
        raise NotImplementedError()

    def install(package):
        print util.run_cmd("%s install %s" % (self.CMD_STR, package))

    def remove(package):
        raise NotImplementedError()

    def update():
        raise NotImplementedError()

    def upgrade():
        raise NotImplementedError()
