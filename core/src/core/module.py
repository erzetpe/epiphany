import importlib
import glob
import argparse
import sys
import os
from os.path import dirname, basename, isfile, join


def init(info, parser=None):
    # setup the parser
    if parser == None:
        parser = argparse.ArgumentParser(
            description=__doc__,
            usage=f'''{info.MODULE_CLI_NAME} <command> [<args>]''',
            formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('--version', action='version', help='Shows the module version', version=info.MODULE_VERSION)
        sub_parsers = parser.add_subparsers()
    else:
        module_parser = parser.add_parser(info.MODULE_CLI_NAME, description=info.MODULE_DESCRIPTION)
        sub_parsers = module_parser.add_subparsers()

        # load command modules
    command_names = glob.glob(join(info.MODULE_NAME, "*.py"))
    filtered_command_names = [basename(f)[:-3] for f in command_names if
                              isfile(f) and not basename(f)[:-3].startswith('__')]
    for command_name in filtered_command_names:
        command = importlib.import_module(f'{info.MODULE_NAME}.{command_name}')
        command.init(sub_parsers)

    return parser, sub_parsers


def run(info, custom_init=None):
    try:
        if custom_init == None:
            parser, sub_parsers = init(info)
        else:
            parser, sub_parsers = custom_init(info)
        args = parser.parse_args(sys.argv[1:])
        exit(args.func(args))
    except Exception as e:
        print(e)
        exit(1)


def setup(info, dependencies):
    import shutil
    from subprocess import check_output
    from setuptools import setup

    # prepare the requirements.
    out = check_output(['pipenv', 'lock', '-r']).decode("utf-8")
    requirements = out.splitlines()
    del requirements[0]

    # prepare the README
    with open('../README.md') as f:
        readme = f.read()

    # prepare the LICENSE
    with open('../LICENSE') as f:
        license = f.read()

    # prepare the external data
    # datadir = os.path.join('data')
    # datafiles = [(os.path.join('epicli', d), [os.path.join(d, f) for f in files])
    #    for d, folders, files in os.walk(datadir)]

    setup(
        name=f'epi_{info.MODULE_NAME}',
        version=info.MODULE_VERSION,
        description=info.MODULE_DESCRIPTION,
        long_description=readme,
        author='Epiphany Team',
        author_email='',
        url='https://github.com/epiphany-platform/epiphany',
        license=license,
        packages=[*[info.MODULE_NAME], *dependencies],
        # data_files=datafiles,
        entry_points={
            'console_scripts': [
                f'{info.MODULE_CLI_NAME} = {info.MODULE_NAME}.__main:run'
            ]
        },
        install_requires=requirements
    )

    CLEAN_FILES = '../build ../*.pyc ../*.tgz ../*.egg-info'.split(' ')
    print('Cleaning wheel build...')
    for path_spec in CLEAN_FILES:
        # Make paths absolute and relative to this path
        abs_paths = glob.glob(os.path.normpath(os.path.join(os.path.dirname(__file__), path_spec)))
        for path in [str(p) for p in abs_paths]:
            print('Removing %s' % os.path.relpath(path))
            shutil.rmtree(path)
