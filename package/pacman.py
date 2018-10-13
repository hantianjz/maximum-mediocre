import package_manager

import util


class Pacman(package_manager.PackagerManager):
    def __init__(self):
        raise NotImplementedError()

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
