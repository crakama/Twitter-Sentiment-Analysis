"""
twitment

Usage:
  twitment welcome
  twitment -h | --help
  twitment --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
Examples:
  twitment welcome

"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import commands
    ''' Takes in commands in form of dictionary'''
    options = docopt(__doc__, version=VERSION)

    """
    Iterates through the options dict trying to dynamically match
    the command the user is trying to run
    with a pre-defined command class we've already created.
    """
    for k, v in options.iteritems():
        if hasattr(commands, k) and v:
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1]
                       for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
