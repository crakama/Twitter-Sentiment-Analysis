"""Twitter search.

Usage:
  manage.py search [TEXT]...
  manage.py (-h | --help)
  manage.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt

from twitment.search import ClassTwitter


def search_query(namesearch):
    """
       search_query receives commandline args as a string argument and
       passes it to search function defined in Classtwitter module

    """
    search_string = str(namesearch)
    # print search_string

    # while len(search_string) <= 0:
    # print 'In the loop'
    query_obj = ClassTwitter()
    query_obj.search(search_string)



def main():
    arguments = docopt(__doc__, version='Twitter Search')


    print("########################################################################################################################")
    namesearch = ' '.join(arguments['TEXT'])
    search_query(namesearch)


if __name__ == '__main__':
    main()
