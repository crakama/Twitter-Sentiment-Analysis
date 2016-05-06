"""Twitter search.

Usage:
  manage freq  <wordfreq>
  manage search <name>
  manage analyse <analyse>
  manage send <number>
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
import cmd
from pyfiglet import Figlet
from twitment.search import ClassTwitter
from twitment.sendSMS import SMS
from colorama import init
from colorama import Fore, Back, Style
init()


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
        "1. To Search for tweets by username                $ manage search <twitter_name>\n" + \
        "2. Perform word frequency on the tweets            $ manage <wordfreq> \n" + \
        "2. Send fetched tweet as an SMS                    $ manage  send\n" + \
        "3. To perform Setiment Analysis on tweets          $ manage analyse\n\n\n"

    print Fore.YELLOW + "  "
    f = Figlet(font='basic')
    print f.renderText('Twitter Sentiment Analysis')
    print(Style.RESET_ALL)

    prompt = "(manage)"

    @cliparser
    def do_send(self, arg):
        """Usage: send <number>"""
        mobilenum = arg['<number>']
        send_obj = ClassTwitter()
        send_obj.sendTweet(mobilenum)

    @cliparser
    def do_analyse(self, arg):
        """Usage: analyse <analyse>"""
        print "To analyse, run a search analysis, will happen automatically"


    @cliparser
    def do_freq(self,arg):
        """Usage: freq <wordfreq>"""
        freq_string = str(arg)
        freq_obj = ClassTwitter()
        freq_obj.frequency(freq_string)

    @cliparser
    def do_search(self, arg):
        """Usage: search <name>"""

        search_string = str(arg)
        query_obj = ClassTwitter()
        query_obj.search(search_string)


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        q = Figlet(font='basic')
        print q.renderText('Good Bye!')
        exit()



opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Sentiment().cmdloop()

print(opt)


