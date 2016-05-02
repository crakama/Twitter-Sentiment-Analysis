""" The welcome command """

from json import dumps
from search import ClassTwitter


from .base import Base


class Welcome(Base):

    """ call search function in search.py module """
    def run(self):
        print " Welcome to twitter sentiment analysis tool"
