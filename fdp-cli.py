#!/usr/bin/env python3

import json
import os
import sys
from typing import Callable

_VERSION_ = '0.1.0'


_CONFIG_PATHS_ = [
    os.path.join(os.getcwd(), 'fdp.config.json'),
    os.path.join(os.getenv('HOME'), 'fdp.config.json'),
]

_CONFIG_ = None
_CONFIG_PATH_ = None

for path in _CONFIG_PATHS_:

    if os.path.exists(path):
        _CONFIG_PATH_ = path
        with open(path, 'r') as f:
            _CONFIG_ = json.load(f)

        break

if _CONFIG_ is None:
    print('Erro! Config not found, please run fdp-configure to setup')
    sys.exit(1)


class Command:
    def __init__(
        self,
        use: str = None,
        short: str = None,
        run: Callable[..., None] = None,
        flags: list[str] = [],
        **kwargs,
    ):
        self.use = use
        self.short = short

        if run is not None:
            self.run = run

        self.flags = flags
        self.attrs = kwargs


class Cli(Command):
    def __init__(
        self,
        commands: list[Command] = [],
        flags: list[str] = [],
    ):
        self.commands = commands

        def version(exit: bool = True):
            print(
                f'FDP CLI - v{_VERSION_} - https://github.com/WilliamSampaio/FDP-CLI'
            )
            if exit:
                sys.exit(0)

        version_cmd = Command(
            'version',
            'Show informations and version',
            version,
        )

        self.commands.append(version_cmd)

        super().__init__(flags=flags)

    def run(self):

        if len(sys.argv) == 1 or sys.argv[1] == '--help':
            self.usage()

        args = sys.argv[1:]

        if args[0] == '--version':
            self.get_command_by_name('version').run()

        if args[0] not in self.list_commands() and args[0] not in self.flags:
            print(f"Erro! Command or flag '{args[0]}' not found")
            sys.exit(1)

        if args[0] in self.list_commands():
            self.get_command_by_name(args[0]).run(args[1:])

    def get_command_by_name(self, command: str) -> Command | None:
        return [c for c in self.commands if c.use == command][0] or None

    def list_commands(self):
        return [c.use for c in self.commands]

    def usage(self):
        self.get_command_by_name('version').run(exit=False)

        print('Usage: fdp-cli <command> [<args>]\n')

        for c in self.commands:
            print(f'{c.use}\t\t\t\t{c.short}')

        print()
        sys.exit(0)


def ignore_run(paths: list[str]):
    if 'ignore' not in _CONFIG_:
        _CONFIG_['ignore'] = []
    for path in paths:
        _CONFIG_['ignore'].append(path)
    with open(_CONFIG_PATH_, 'w') as f:
        json.dump(_CONFIG_, f, indent=2)


_COMMANDS_ = [
    Command('ignore', 'Add path to ignore on deployment', ignore_run)
]


if __name__ == '__main__':

    cli = Cli(_COMMANDS_)
    cli.run()
