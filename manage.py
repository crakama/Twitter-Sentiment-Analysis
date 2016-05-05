"""Twitter search.

Usage:
  manage start  [TEXT]...
  manage search <name>
  manage send [TEXT]...
  manage (-i | --interactive)
  manage (-h | --help)
  manage --version

Options:
  -i, --interactive  Interactive Mode
  -h --help     Show this screen.
  --version     Show version.

"""
import sys
from docopt import docopt, DocoptExit
# from tkinter import *
# from tkinter import ttk
import cmd

from twitment.search import ClassTwitter
from twitment.sendSMS import SMS


def cliparser(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Sentiment (cmd.Cmd):

    intro = "==========================================================================================================================\n \n" + \
        "How to use this application on commandline(CMD): \n\n" + \
        "1. To Search for tweets by username                ===>$ manage.py search <twitter_name>\n" + \
        "2. Perform word frequency on the tweets            ===>$ manage.py freq \n" + \
        "3. To perform Setiment Analysis on tweets          ===>$ manage.py analyse\n\n\n"

    prompt = "(manage)"

    def sendAnalysis(num):
        mobilenum = str(num)
        send_obj = SMS()
        send_obj.send(mobilenum)

    @cliparser
    def start(program):
        pass

    @cliparser
    def do_search(self, arg):
        """Usage: search <name>"""

        search_string = str(arg)
        query_obj = ClassTwitter()
        query_obj.search(search_string)


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()



opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Sentiment().cmdloop()

print(opt)



def namesearch(args):
    """
           search_query receives commandline args as a string argument and
           passes it to search function defined in Classtwitter module
    """
    pass

