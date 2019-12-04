#!/usr/bin/env py
from core import module

info = lambda: None
info.MODULE_NAME = 'backup'
info.MODULE_VERSION = '1.0.0'
info.MODULE_DESCRIPTION = 'Module to manage Epiphany backup'
info.MODULE_CLI_NAME = 'backup'


def init(parser):
    return module.init(info, parser)


def run():
    module.run(info)


if __name__ == '__main__':
    run()
