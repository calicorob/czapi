# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_event.ipynb (unless otherwise specified).

__all__ = ['get_event_name', 'get_event_date']

# Cell

from .base import make_soup
from bs4 import BeautifulSoup

# Cell

def _get_event_name(
     soup : BeautifulSoup
)->str:
    """Returns the name of the event based on the event_id. Built so for larger-scale scraping less API calls are made."""
    return soup.find('title').string

# Cell

def get_event_name(
     cz_event_id : str
    ,**request_kwargs
)->str:
    """Returns the name of the event based on the event_id."""


    # TODO : how to handle situations where an event_id is valid but that event hasn't been conducted yet?
    # e.g. event_id = 12312321312 returns 'CurlingZone – Everything Curling'

    url = 'https://curlingzone.com/event.php?view=Main&eventid=%s#1'%cz_event_id
    return _get_event_name(make_soup(url=url,**request_kwargs))

# Cell

def _get_event_date(

     soup : BeautifulSoup
)->str:
    """Returns the dates of the event from the passed soup. Built so for larger-scale scraping less API calls are made."""
    return soup.find(name='div',attrs={'class':'badge-widget'}).string

# Cell

def get_event_date(

     cz_event_id : str
    ,**request_kwargs

)->str:
    """Returns the dates of the event based on the event_id."""

    # TODO : how to handle situations where an event_id is valid but that event hasn't been conducted yet?
    # e.g. event_id = 12312321312 returns 'Recent'

    url = 'https://curlingzone.com/event.php?view=Main&eventid=%s#1'%cz_event_id
    return _get_event_date(make_soup(url=url,**request_kwargs))