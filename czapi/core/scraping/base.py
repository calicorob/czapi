from dataclasses import dataclass, field
from typing import Tuple, Any
from bs4 import Tag
from abc import ABC, abstractmethod,abstractproperty
from czapi.core.utils import make_request_from, make_soup_from
from uuid import uuid4

@dataclass
class ScrapedBoxscore:
    team_name : str = field(default_factory=str)
    href : str = field(default_factory=str)
    hammer_start : bool = field(default_factory=bool)
    score : list[str] = field(default_factory=list)
    final_score : str = field(default_factory=str)
    boxscore_guid : int = field(default_factory=int)


    def add_score(self,end_score:str)->None:
        self.score.append(end_score)


def generate_scraped_boxscore_from_table(table:Tag)->tuple[ScrapedBoxscore]:
    

    if table is None:
        raise ValueError('Table tag is NoneType.') # TODO, custom error event for this
    
    scraped_boxscores = list()
    guid = uuid4().int
    

    for tag in table.find_all(name='td'):
        if tag.attrs.get('class') == ['linescoreteam']:
            
            boxscore = ScrapedBoxscore()
            boxscore.boxscore_guid = guid
            scraped_boxscores.append(boxscore)

            boxscore.team_name = tag.a.string.strip() 
            boxscore.href = tag.a['href']

        if tag.attrs.get('class') == ['linescorehammer']:
            boxscore.hammer_start = not bool(tag.string)

        if tag.attrs.get('class') == ['linescoreend']:
            end_score = tag.string.strip()
            if end_score: boxscore.add_score(end_score)

        if tag.attrs.get('class') == ['linescorefinal']:
            boxscore.final_score = tag.b.string.strip()

        
    return tuple(scraped_boxscores)
            
            

class Page(ABC):


    @abstractproperty
    def url(self)->str:
        pass

    @abstractproperty
    def event_name(self)->str:
        pass

    @abstractproperty
    def event_date(self)->str:
        pass

    @abstractproperty
    def draw(self)->str:
        pass

    @abstractproperty
    def draw_num(self)->int:
        pass

    @abstractproperty
    def tables(self)->list[Tag]:
        pass

    @abstractmethod
    def generate_scraped_boxscores(self)->tuple[tuple[ScrapedBoxscore]]:
        pass



@dataclass
class LinescorePage(Page):
    """
        Represents a CurlingZone linescore page.
        Example page here: https://curlingzone.com/event.php?eventid=7795&view=Scores&showdrawid=25#1

    """
    cz_event_id : int
    cz_draw_id: int


    def __post_init__(self)->None:
        response = make_request_from(url = self.url)
        self.soup = make_soup_from(response=response)


    @property
    def url(self)->str:
        return 'https://curlingzone.com/event.php?eventid=%s&view=Scores&showdrawid=%s#1'%(self.cz_event_id,self.cz_draw_id)

    @property
    def event_name(self)->str:
        return self.soup.find('h3',attrs={'class':'entry-title-widget'}).string

    @property
    def event_date(self)->str:
        return self.soup.find('div',attrs={'class':'badge-widget'}).string

    @property
    def draw_num(self)->int:
        return self.soup.find(name='select').find_all(name='option').index(self.soup.find(name='option',attrs={'selected':'selected'}))+1

    @property
    def draw(self)->str:
        return self.soup.find(name='option',attrs={'selected':'selected'}).string

    @property
    def tables(self)->list[Tag]:
        return self.soup.find_all(name = 'table',attrs={'class':'linescorebox'})

    def generate_scraped_boxscores(self)->tuple[tuple[ScrapedBoxscore]]:
        return tuple([generate_scraped_boxscore_from_table(table=table) for table in self.tables])

   