# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_base.ipynb (unless otherwise specified).

__all__ = ['Page', 'LinescorePage', 'get_flat_boxscores_from']

# Cell

import requests
from requests.models import Response
from bs4 import BeautifulSoup,Tag
from abc import ABC, abstractproperty, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Any, Tuple
from collections import defaultdict
from uuid import  uuid4
from ..errors import DifferentScoreLengthError,InvalidScoreError

# Internal Cell

def make_request_from(

     *
    ,url : str
    ,**kwargs

)->Response:
    return requests.get(url=url,**kwargs)


def make_soup_from(

     *
    ,response : Response
    ,**kwargs

)->BeautifulSoup:
    """ Returns a Beautifulsoup object for the passed URL."""

    return BeautifulSoup(response.content,features='html.parser',**kwargs)

# Internal Cell

def generate_dict_from_table(

    table : Tag

)->defaultdict:
    """Helper function for returning the curling boxscore from a bs4 Tag object."""
    d = defaultdict(list)
    team = None

    # TODO : add error handling for when no table is passed / None

    if table is None:
        raise ValueError('Table tag is NoneType.')

    # loop through tags in table
    for tag in table.find_all('td'):
        if tag.attrs.get('class') == ['linescoreteam']:
            team = tag.a.string
            d[team] = defaultdict(list)
            d[team]['href'] = tag.a['href']
        elif tag.attrs.get('class') == ['linescorehammer']:
            d[team]['hammer'] = not bool(tag.string) # opposite for some reason
        elif tag.attrs.get('class') == ['linescoreend']:
            d[team]['score'].append(tag.string.strip())
        elif tag.attrs.get('class') == ['linescorefinal']:
            d[team]['finalscore'] = tag.b.string.strip()

    return d

# Internal Cell
def normalize_scores(score_1 : List[str],score_2 : List[str])->List[int]:
    score_1_len = len(score_1)
    score_2_len = len(score_2)
    if score_1_len != score_2_len:
        raise DifferentScoreLengthError(score_1_len =score_1_len,score_2_len = score_2_len)

    end_1 = []
    current_diff = 0

    for i in range(score_1_len):
        try:
            val_1 = int(score_1[i])
            val_2 = int(score_2[i])

        except ValueError:
            break

        if val_1 > 0 and val_2 > 0:
            raise InvalidScoreError(val_1 = val_1,val_2=val_2)

        new_current_diff = current_diff + val_1 - val_2
        end_1.append(new_current_diff)
        current_diff = new_current_diff

    return end_1, list(map(lambda x: -1*x,end_1))




# Internal Cell
def get_hammer_progressions(hammer_start:bool,normalized_score:List[int])->List[bool]:
    current_hammer = hammer_start
    hammer_progression = [hammer_start]
    for i in range(1,len(normalized_score)):
        if current_hammer and (normalized_score[i] > normalized_score[i-1]):
            current_hammer = False
        if not current_hammer and (normalized_score[i] < normalized_score[i-1]):
            current_hammer = True
        hammer_progression.append(current_hammer)

    return hammer_progression, list(map(lambda x: not x, hammer_progression))

# Internal Cell

@dataclass
class HalfBoxscore:
    team_name : str
    href : str
    hammer : bool
    score : List[str]
    finalscore : str


@dataclass
class NormalizedHalfBoxscore(HalfBoxscore):
    hammer_progression : List[bool]
    normalized_score : List[int]

# Internal Cell

def generate_half_boxscore_pair(boxscore:defaultdict)->Tuple[NormalizedHalfBoxscore]:
    half_boxscores = [HalfBoxscore(team_name=team_name,**results) for team_name,results in boxscore.items()]

    normalized_scores = normalize_scores(

         score_1 = half_boxscores[0].score
        ,score_2 = half_boxscores[1].score

    )

    hammer_progressions = get_hammer_progressions(

         hammer_start = half_boxscores[0].hammer
        ,normalized_score = normalized_scores[0]

    )

    return NormalizedHalfBoxscore(**half_boxscores[0].__dict__,hammer_progression = hammer_progressions[0],normalized_score = normalized_scores[0]),NormalizedHalfBoxscore(**half_boxscores[1].__dict__,hammer_progression = hammer_progressions[1],normalized_score = normalized_scores[1] )


# Internal Cell

@dataclass
class NormalizedBoxscore:

    boxscore: defaultdict

    def __post_init__(self)->None:
        self.normalized_half_boxscore_pair = generate_half_boxscore_pair(boxscore=self.boxscore)
        self.guid = uuid4().int
        self.flattened_normalized_boxscore = [list(half_score.__dict__.values())+[self.guid] for half_score in self.normalized_half_boxscore_pair]


#     @property
#     def flattened_normalized_boxscore(self)->List[List[Any]]:
#         return [list(half_score.__dict__.values())+[self.guid] for half_score in self.normalized_half_boxscore_pair]


# Cell


class Page(ABC):


    @abstractproperty
    def url(self)->str:
        ...

    @abstractproperty
    def event_name(self)->str:
        ...

    @abstractproperty
    def event_date(self)->str:
        ...

    @abstractproperty
    def draw(self)->str:
        ...

    @abstractproperty
    def tables(self)->List[Tag]:
        ...

    @abstractmethod
    def generate_boxscores(self)->List[dict]:
        ...


@dataclass
class LinescorePage(Page):
    cz_event_id : int
    cz_draw_id: int


    def __post_init__(self)->None:
        response = make_request_from(url = self.url)
        self.soup = make_soup_from(response=response)
        self.boxscores = self.generate_boxscores()
        self.normalized_boxscores = self.generate_normalized_boxscores()


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
    def draw(self)->str:
        return self.soup.find(name='option',attrs={'selected':'selected'}).string

    @property
    def tables(self)->List[Tag]:
        return self.soup.find_all(name = 'table',attrs={'class':'linescorebox'})

    def generate_boxscores(self)->List[defaultdict]:
        return [generate_dict_from_table(table=table) for table in self.tables]

    def generate_normalized_boxscores(self)->List[NormalizedBoxscore]:
        return [NormalizedBoxscore(boxscore=boxscore) for boxscore in self.boxscores]

    def get_boxscore_from(self,cz_game_id : int)->defaultdict:
        if cz_game_id <= 0:
            raise ValueError('cz_game_id must be 1 or greater.')

        if cz_game_id > len(self.boxscores):
            raise ValueError('') # TODO

        return self.boxscores[cz_game_id - 1]

    # repeated code but will re-factor later
    def get_normalized_boxscore_from(self,cz_game_id : int)->NormalizedBoxscore:
        if cz_game_id <= 0:
            raise ValueError('cz_game_id must be 1 or greater.')

        if cz_game_id > len(self.normalized_boxscores):
            raise ValueError('') # TODO

        return self.normalized_boxscores[cz_game_id - 1]


# Cell
def get_flat_boxscores_from(linescore_page:LinescorePage):
    flattened_boxscores = [boxscore.flattened_normalized_boxscore for boxscore in linescore_page.normalized_boxscores]
    return [[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]] for f in flattened_boxscores for row in f]