import disutils


class PackageManager(object):

    PACKAGE_MANAGER_CMD_STR = None

    def __init__(self):
        if not self.PACKAGE_MANAGER_CMD_STR or not disutils.spawn.find_executable(
                self.PACKAGE_MANAGER_CMD_STR):
            raise NotImplementedError(
                "PackageManager \"{}\" Does not exist".format(
                    self.PACKAGE_MANAGER_CMD_STR))

    def exist(self, package):
        raise NotImplementedError()

    def install(self, package):
        raise NotImplementedError()

    def remove(self, package):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def upgrade(self):
        raise NotImplementedError()
