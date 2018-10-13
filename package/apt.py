import package_manager

import util


class Apt(package_manager.PackagerManager):

    CMD_STR = "apt-get"

    def __init__():
        raise NotImplementedError()

    def exist(package):
        raise NotImplementedError()

    def install(package):
        raise NotImplementedError()

    def remove(package):
        raise NotImplementedError()

    def update():
        raise NotImplementedError()

    def upgrade():
        raise NotImplementedError()
