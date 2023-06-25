__all__ = []

import requests
from bs4 import BeautifulSoup


def make_request_from(

     *
    ,url : str
    ,**kwargs

)->requests.Response:
    """Returns a GET response from the passed URL."""
    return requests.get(url=url,**kwargs)


def make_soup_from(

     *
    ,response : requests.Response
    ,**kwargs

)->BeautifulSoup:
    """ Returns a Beautifulsoup object for the passed GET response."""

    return BeautifulSoup(response.content,features='html.parser',**kwargs)