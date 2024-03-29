# Welcome to czapi
> A basic API for scraping curling boxscores off of the popular <a href='https://www.curlingzone.com'>CurlingZone</a> website. 


## Install

```
pip install czapi
```

## How to use

```python
import czapi.api as api
```

## LinescorePage
czapi is based around the `LinescorePage` object which represents a linescore page on the CurlingZone website. 

Click [here](https://curlingzone.com/event.php?view=Scores&eventid=7795#1) to see an example linescore page.

Creating an instance of the `LinescorePage` class gives access to every boxscore on that linescore page.

```python
linescore_page = api.LinescorePage(cz_event_id = 6400, cz_draw_id = 2)
```

The `cz_event_id` and `cz_draw_id` arguments are found in the CurlingZone URL. 

Here's an example:
> ht<span>t</span>ps://curlingzone.com/event.php?**eventid=7795**&view=Scores&show**drawid=21**#1

The boxscores on the linescore page can be accessed through the `boxscores` property which returns a list of boxscores.

```python
linescore_page.boxscores
```




    [{'Wayne Tuck Jr.': {'draw': 'Draw: 2',
       'draw_num': 2,
       'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
       'score': ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
       'hammer': True,
       'finalscore': '5'},
      'Matthew Hall': {'draw': 'Draw: 2',
       'draw_num': 2,
       'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       'score': ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
       'hammer': False,
       'finalscore': '7'}},
     {'Dayna Deruelle': {'draw': 'Draw: 2',
       'draw_num': 2,
       'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1',
       'score': ['0', '0', '1', '0', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '1'},
      'Tyler Stewart': {'draw': 'Draw: 2',
       'draw_num': 2,
       'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
       'score': ['0', '2', '0', '2', '1', '1', '4', 'X'],
       'hammer': True,
       'finalscore': '10'}},
     {'Mark Kean': {'draw': 'Draw: 2',
       'draw_num': 2,
       'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
       'score': ['2', '0', '1', '0', '0', '0', '1', '3', 'X'],
       'hammer': True,
       'finalscore': '7'},
      'Jason March': {'draw': 'Draw: 2',
       'draw_num': 2,
       'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
       'score': ['0', '0', '0', '0', '2', '1', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '3'}},
     {'Richard Krell': {'draw': 'Draw: 2',
       'draw_num': 2,
       'href': 'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1',
       'score': ['2', '0', '1', '0', '2', '1', '1', 'X'],
       'hammer': True,
       'finalscore': '7'},
      'Rob Ainsley': {'draw': 'Draw: 2',
       'draw_num': 2,
       'href': 'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       'score': ['0', '0', '0', '1', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '1'}}]



A boxscore is returned as a dictionary of team names, game information dictionary key, value pairs.

Each game information dictionary contains:

* 'href' key with a corresponding string value of CurlingZone IDs identifying the team.
* 'hammer' key with corresponding boolean value of whether or not that team started the game with hammer.
* 'score' key with corresponding list of string value of end-by-end results for that team.
* 'finalscore' key with corresponding final score for the team.
* 'draw_num' key with corresponding draw number for the game.
* 'draw' key with corresponding draw. 

Individual boxscores can be accessed through the `get_boxscore_from` method.

```python
boxscore = linescore_page.get_boxscore_from(cz_game_id = 1)
boxscore
```




    {'Wayne Tuck Jr.': {'draw': 'Draw: 2',
      'draw_num': 2,
      'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
      'score': ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
      'hammer': True,
      'finalscore': '5'},
     'Matthew Hall': {'draw': 'Draw: 2',
      'draw_num': 2,
      'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      'score': ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
      'hammer': False,
      'finalscore': '7'}}



`cz_game_id` argument corresponds to the number the boxscore appears in on the linescore page.

The LinescorePage object contains these properties which details information on the boxscores:

* event_name
* event_date
* draw
* draw number

```python
print(linescore_page.event_name,',',linescore_page.event_date)
```

    Ontario Tankard - Open Qualifier , Jan 17 - 19, 2020
    

For convenience, upon instantiation of a `LinescorePage` object, a `NormalizedBoxscore` instance for each boxscore is created. A `NormalizedBoxscore` holds the same information as a boxscore dictionary with two new pieces of information added: 
1. The hammer progression for both teams throughout the game, i.e. who had hammer in what end.
2. Each team's relative score, i.e. who was up/down X after end Y.

```python
normalized_boxscore = linescore_page.get_normalized_boxscore_from(cz_game_id = 1)
normalized_boxscore
```




    NormalizedBoxscore(boxscore={'Wayne Tuck Jr.': {'draw': 'Draw: 2', 'draw_num': 2, 'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1', 'score': ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'], 'hammer': True, 'finalscore': '5'}, 'Matthew Hall': {'draw': 'Draw: 2', 'draw_num': 2, 'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', 'score': ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'], 'hammer': False, 'finalscore': '7'}})



A `NormalizedBoxscore` object holds two `NormalizedHalfBoxscore` instances. 

```python
normalized_boxscore.normalized_half_boxscore_pair[0]
```




    NormalizedHalfBoxscore(team_name='Wayne Tuck Jr.', href='event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1', hammer=True, score=['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'], finalscore='5', draw_num=2, draw='Draw: 2', hammer_progression=[True, True, False, True, True, True, True, False, False, False], normalized_score=[0, 0, 2, -2, -2, -2, -3, -2, -1, 0])



For Wayne Tuck Jr. the `hammer_progression` attribute can be interpreted as follows: 

* End 1: Wayne had hammer
* End 2: Wayne had hammer
* End 3: Wayne didn't have hammer
* And so on and so forth..

```python
normalized_boxscore.normalized_half_boxscore_pair[-1]
```




    NormalizedHalfBoxscore(team_name='Matthew Hall', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', hammer=False, score=['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'], finalscore='7', draw_num=2, draw='Draw: 2', hammer_progression=[False, False, True, False, False, False, False, True, True, True], normalized_score=[0, 0, -2, 2, 2, 2, 3, 2, 1, 0])



For Matthew Hall, the `normalized_score` attribute can be interpreted as follows:

* The score was tied in the first end (obviously).
* The score was tied in the second end.
* In the 3rd end, Matthew was down 2.
* In the 4th end, Matthew was up 2 after taking 4.
* And so on and so forth..

You'll also notice the `NormalizedBoxscore` object has a guid property which identifies that two `NormalizedHalfBoxscore` belong to the same game.

```python
normalized_boxscore.guid
```




    154352576001077780910640079893588160113



czapi's `get_flat_boxscores_from` function takes a `cz_event_id` and `cz_draw_id` as an arguments and returns a (flat) nested list object of all the boxscore information on the linescore page. This nested list object can be ingested into a pandas DataFrame or pushed to a SQL database.

```python
api.get_flat_boxscores_from(cz_event_id = 6400, cz_draw_id = 2)
```




    [('Wayne Tuck Jr.',
      'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
      True,
      ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
      '5',
      2,
      'Draw: 2',
      [True, True, False, True, True, True, True, False, False, False],
      [0, 0, 2, -2, -2, -2, -3, -2, -1, 0],
      306528221620467227442052913955328486003),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      False,
      ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
      '7',
      2,
      'Draw: 2',
      [False, False, True, False, False, False, False, True, True, True],
      [0, 0, -2, 2, 2, 2, 3, 2, 1, 0],
      306528221620467227442052913955328486003),
     ('Dayna Deruelle',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1',
      False,
      ['0', '0', '1', '0', '0', '0', '0', 'X'],
      '1',
      2,
      'Draw: 2',
      [False, False, True, False, True, True, True, True],
      [0, 0, -2, -1, -3, -4, -5, -9],
      169959036371998794200683443427801286021),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['0', '2', '0', '2', '1', '1', '4', 'X'],
      '10',
      2,
      'Draw: 2',
      [True, True, False, True, False, False, False, False],
      [0, 0, 2, 1, 3, 4, 5, 9],
      169959036371998794200683443427801286021),
     ('Mark Kean',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
      True,
      ['2', '0', '1', '0', '0', '0', '1', '3', 'X'],
      '7',
      2,
      'Draw: 2',
      [True, False, False, False, False, True, True, False, False],
      [0, 2, 2, 3, 3, 1, 0, 1, 4],
      216723633949199876308042205365369844269),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
      False,
      ['0', '0', '0', '0', '2', '1', '0', '0', 'X'],
      '3',
      2,
      'Draw: 2',
      [False, True, True, True, True, False, False, True, True],
      [0, -2, -2, -3, -3, -1, 0, -1, -4],
      216723633949199876308042205365369844269),
     ('Richard Krell',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1',
      True,
      ['2', '0', '1', '0', '2', '1', '1', 'X'],
      '7',
      2,
      'Draw: 2',
      [True, False, False, False, True, False, False, False],
      [0, 2, 2, 3, 2, 4, 5, 6],
      142335171424399828625133635146510278418),
     ('Rob Ainsley',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
      False,
      ['0', '0', '0', '1', '0', '0', '0', 'X'],
      '1',
      2,
      'Draw: 2',
      [False, True, True, True, False, True, True, True],
      [0, -2, -2, -3, -2, -4, -5, -6],
      142335171424399828625133635146510278418)]



## Event

The `Event` object is a data structure which holds all of the `LinescorePage` objects which make up an entire event. 

An `Event` instance is created by passing a `cz_event_id`.

```python
event = api.Event(cz_event_id = 6400,delay=3,verbose=True)
event
```

    Scraping draw 1.
    Scraping draw 2.
    Scraping draw 3.
    Scraping draw 4.
    Scraping draw 5.
    Scraping draw 6.
    Scraping draw 7.
    




    Event(cz_event_id=6400, delay=3, verbose=True)



The created `Event` objects holds all the `LinescorePage` objects in it's `pages` property.

```python
event.pages
```




    [LinescorePage(cz_event_id=6400, cz_draw_id=1),
     LinescorePage(cz_event_id=6400, cz_draw_id=2),
     LinescorePage(cz_event_id=6400, cz_draw_id=3),
     LinescorePage(cz_event_id=6400, cz_draw_id=4),
     LinescorePage(cz_event_id=6400, cz_draw_id=5),
     LinescorePage(cz_event_id=6400, cz_draw_id=6),
     LinescorePage(cz_event_id=6400, cz_draw_id=7)]



Details about specific draws can be accessed by grabbing the correct LinescorePage.

```python
event.pages[2]
```




    LinescorePage(cz_event_id=6400, cz_draw_id=3)



```python
event.pages[2].boxscores
```




    [{'Matthew Hall': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       'score': ['0', '0', '2', '1', '2', '1', '0', '2', 'X'],
       'hammer': True,
       'finalscore': '8'},
      'Tyler Stewart': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
       'score': ['0', '1', '0', '0', '0', '0', '2', '0', 'X'],
       'hammer': False,
       'finalscore': '3'}},
     {'Mark Kean': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
       'score': ['0', '5', '0', '1', '1', '1', 'X'],
       'hammer': True,
       'finalscore': '8'},
      'Richard Krell': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144349&profileid=25962#1',
       'score': ['1', '0', '1', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '2'}},
     {'Damien Villard': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144354&profileid=27373#1',
       'score': ['2', '1', '0', '1', '0', '0', '1', '0', '0', '0'],
       'hammer': True,
       'finalscore': '5'},
      'Sam Steep': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144351&profileid=25978#1',
       'score': ['0', '0', '1', '0', '2', '0', '0', '1', '1', '1'],
       'hammer': False,
       'finalscore': '6'}},
     {'Jason March': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144350#1',
       'score': ['1', '1', '0', '0', '0', '0', '2', '1', '2', 'X'],
       'hammer': True,
       'finalscore': '7'},
      'Matthew Mepstead': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144356#1',
       'score': ['0', '0', '1', '1', '0', '0', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '2'}},
     {'Wayne Tuck Jr.': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144353&profileid=12486#1',
       'score': ['0', '0', '0', '2', '0', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '2'},
      'Rob Ainsley': {'draw': 'Draw: 3',
       'draw_num': 3,
       'href': 'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       'score': ['2', '1', '0', '0', '1', '2', '1', '1', 'X'],
       'hammer': True,
       'finalscore': '8'}}]



The `get_flat_boxscores` method can be used to return a list of (flat) nested list object of all the boxscore information on all the linescore pages.

```python
event.get_flat_boxscores()
```




    [[('Damien Villard',
       'event.php?view=Team&eventid=6400&teamid=144354&profileid=27373#1',
       True,
       ['0', '0', '0', '0', 'X'],
       '0',
       1,
       'Draw: 1',
       [True, True, True, True, True],
       [0, -1, -4, -6, -8],
       227597408989477916004520082463493572762),
      ('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       False,
       ['1', '3', '2', '2', 'X'],
       '8',
       1,
       'Draw: 1',
       [False, False, False, False, False],
       [0, 1, 4, 6, 8],
       227597408989477916004520082463493572762),
      ('Matthew Mepstead',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144356#1',
       False,
       ['0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'],
       '4',
       1,
       'Draw: 1',
       [False, False, True, False, False, True, False, False, False, True, False],
       [0, 0, -2, -1, 0, -1, 0, 0, 0, -1, 0],
       230481195381514558834165699232540581342),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
       True,
       ['0', '2', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
       '5',
       1,
       'Draw: 1',
       [True, True, False, True, True, False, True, True, True, False, True],
       [0, 0, 2, 1, 0, 1, 0, 0, 0, 1, 0],
       230481195381514558834165699232540581342),
      ('Jason March',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
       False,
       ['0', '2', '0', '1', '0', '2', '2', '0', '2', 'X'],
       '9',
       1,
       'Draw: 1',
       [False, False, False, False, False, True, False, False, True, False],
       [0, 0, 2, 2, 3, 2, 4, 6, 3, 5],
       123876478142928441769100783560984935273),
      ('Sam Steep',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144351&profileid=25978#1',
       True,
       ['0', '0', '0', '0', '1', '0', '0', '3', '0', 'X'],
       '4',
       1,
       'Draw: 1',
       [True, True, True, True, True, False, True, True, False, True],
       [0, 0, -2, -2, -3, -2, -4, -6, -3, -5],
       123876478142928441769100783560984935273)],
     [('Wayne Tuck Jr.',
       'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
       True,
       ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
       '5',
       2,
       'Draw: 2',
       [True, True, False, True, True, True, True, False, False, False],
       [0, 0, 2, -2, -2, -2, -3, -2, -1, 0],
       309985127892547751219643103116568617832),
      ('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       False,
       ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
       '7',
       2,
       'Draw: 2',
       [False, False, True, False, False, False, False, True, True, True],
       [0, 0, -2, 2, 2, 2, 3, 2, 1, 0],
       309985127892547751219643103116568617832),
      ('Dayna Deruelle',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1',
       False,
       ['0', '0', '1', '0', '0', '0', '0', 'X'],
       '1',
       2,
       'Draw: 2',
       [False, False, True, False, True, True, True, True],
       [0, 0, -2, -1, -3, -4, -5, -9],
       258827556868852829922619663221573707805),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
       True,
       ['0', '2', '0', '2', '1', '1', '4', 'X'],
       '10',
       2,
       'Draw: 2',
       [True, True, False, True, False, False, False, False],
       [0, 0, 2, 1, 3, 4, 5, 9],
       258827556868852829922619663221573707805),
      ('Mark Kean',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
       True,
       ['2', '0', '1', '0', '0', '0', '1', '3', 'X'],
       '7',
       2,
       'Draw: 2',
       [True, False, False, False, False, True, True, False, False],
       [0, 2, 2, 3, 3, 1, 0, 1, 4],
       196156262752898539339442275025527127066),
      ('Jason March',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
       False,
       ['0', '0', '0', '0', '2', '1', '0', '0', 'X'],
       '3',
       2,
       'Draw: 2',
       [False, True, True, True, True, False, False, True, True],
       [0, -2, -2, -3, -3, -1, 0, -1, -4],
       196156262752898539339442275025527127066),
      ('Richard Krell',
       'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1',
       True,
       ['2', '0', '1', '0', '2', '1', '1', 'X'],
       '7',
       2,
       'Draw: 2',
       [True, False, False, False, True, False, False, False],
       [0, 2, 2, 3, 2, 4, 5, 6],
       121058110285022966689701916848012130324),
      ('Rob Ainsley',
       'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       False,
       ['0', '0', '0', '1', '0', '0', '0', 'X'],
       '1',
       2,
       'Draw: 2',
       [False, True, True, True, False, True, True, True],
       [0, -2, -2, -3, -2, -4, -5, -6],
       121058110285022966689701916848012130324)],
     [('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       True,
       ['0', '0', '2', '1', '2', '1', '0', '2', 'X'],
       '8',
       3,
       'Draw: 3',
       [True, True, True, False, False, False, False, True, False],
       [0, 0, -1, 1, 2, 4, 5, 3, 5],
       167908611678356344738885531672086035216),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
       False,
       ['0', '1', '0', '0', '0', '0', '2', '0', 'X'],
       '3',
       3,
       'Draw: 3',
       [False, False, False, True, True, True, True, False, True],
       [0, 0, 1, -1, -2, -4, -5, -3, -5],
       167908611678356344738885531672086035216),
      ('Mark Kean',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
       True,
       ['0', '5', '0', '1', '1', '1', 'X'],
       '8',
       3,
       'Draw: 3',
       [True, True, False, True, False, False, False],
       [0, -1, 4, 3, 4, 5, 6],
       157383102330203138325358878297425755857),
      ('Richard Krell',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144349&profileid=25962#1',
       False,
       ['1', '0', '1', '0', '0', '0', 'X'],
       '2',
       3,
       'Draw: 3',
       [False, False, True, False, True, True, True],
       [0, 1, -4, -3, -4, -5, -6],
       157383102330203138325358878297425755857),
      ('Damien Villard',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144354&profileid=27373#1',
       True,
       ['2', '1', '0', '1', '0', '0', '1', '0', '0', '0'],
       '5',
       3,
       'Draw: 3',
       [True, False, False, True, False, True, True, False, True, True],
       [0, 2, 3, 2, 3, 1, 1, 2, 1, 0],
       197764335276159882538274022024920645468),
      ('Sam Steep',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144351&profileid=25978#1',
       False,
       ['0', '0', '1', '0', '2', '0', '0', '1', '1', '1'],
       '6',
       3,
       'Draw: 3',
       [False, True, True, False, True, False, False, True, False, False],
       [0, -2, -3, -2, -3, -1, -1, -2, -1, 0],
       197764335276159882538274022024920645468),
      ('Jason March',
       'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144350#1',
       True,
       ['1', '1', '0', '0', '0', '0', '2', '1', '2', 'X'],
       '7',
       3,
       'Draw: 3',
       [True, False, False, True, True, True, True, False, False, False],
       [0, 1, 2, 1, 0, 0, 0, 2, 3, 5],
       19248089004956668591585521441771100702),
      ('Matthew Mepstead',
       'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144356#1',
       False,
       ['0', '0', '1', '1', '0', '0', '0', '0', '0', 'X'],
       '2',
       3,
       'Draw: 3',
       [False, True, True, False, False, False, False, True, True, True],
       [0, -1, -2, -1, 0, 0, 0, -2, -3, -5],
       19248089004956668591585521441771100702),
      ('Wayne Tuck Jr.',
       'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144353&profileid=12486#1',
       False,
       ['0', '0', '0', '2', '0', '0', '0', '0', 'X'],
       '2',
       3,
       'Draw: 3',
       [False, True, True, True, False, True, True, True, True],
       [0, -2, -3, -3, -1, -2, -4, -5, -6],
       152642289275163622503053683522534226102),
      ('Rob Ainsley',
       'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       True,
       ['2', '1', '0', '0', '1', '2', '1', '1', 'X'],
       '8',
       3,
       'Draw: 3',
       [True, False, False, False, True, False, False, False, False],
       [0, 2, 3, 3, 1, 2, 4, 5, 6],
       152642289275163622503053683522534226102)],
     [('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       True,
       ['1', '0', '1', '0', '1', '0', '2', '0', '1', '0'],
       '6',
       4,
       'Draw: 4',
       [True, False, True, False, True, False, True, False, True, False],
       [0, 1, -1, 0, -2, -1, -2, 0, -1, 0],
       128520251865367755000080630810739466709),
      ('Mark Kean',
       'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961#1',
       False,
       ['0', '2', '0', '2', '0', '1', '0', '1', '0', '1'],
       '7',
       4,
       'Draw: 4',
       [False, True, False, True, False, True, False, True, False, True],
       [0, -1, 1, 0, 2, 1, 2, 0, 1, 0],
       128520251865367755000080630810739466709),
      ('Sam Steep',
       'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961&eventid=6400&teamid=144351&profileid=25978#1',
       False,
       ['1', '0', '0', '2', '0', '1', '1', '0', '1', '1'],
       '7',
       4,
       'Draw: 4',
       [False, False, True, True, False, True, False, False, True, False],
       [0, 1, 0, -2, 0, -2, -1, 0, -1, 0],
       164045326452654642850026023480637847801),
      ('Jason March',
       'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961&eventid=6400&teamid=144350#1',
       True,
       ['0', '1', '2', '0', '2', '0', '0', '1', '0', '0'],
       '6',
       4,
       'Draw: 4',
       [True, True, False, False, True, False, True, True, False, True],
       [0, -1, 0, 2, 0, 2, 1, 0, 1, 0],
       164045326452654642850026023480637847801),
      ('Dayna Deruelle',
       'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144346&profileid=26636#1',
       False,
       ['0', '2', '1', '1', '1', '0', '3', 'X'],
       '8',
       4,
       'Draw: 4',
       [False, True, False, False, False, False, True, False],
       [0, -1, 1, 2, 3, 4, 3, 6],
       76792983814886196713410396043046633915),
      ('Rob Ainsley',
       'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       True,
       ['1', '0', '0', '0', '0', '1', '0', 'X'],
       '2',
       4,
       'Draw: 4',
       [True, False, True, True, True, True, False, True],
       [0, 1, -1, -2, -3, -4, -3, -6],
       76792983814886196713410396043046633915)],
     [('Sam Steep',
       'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978#1',
       False,
       ['0', '1', '0', '0', '0', '2', '0', '2', '0', '0'],
       '5',
       5,
       'Draw: 5',
       [False, False, False, True, True, True, False, True, False, False],
       [0, 0, 1, 0, -1, -3, -1, -3, -1, -1],
       38480930669174444566426826324563146081),
      ('Richard Krell',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962#1',
       True,
       ['0', '0', '1', '1', '2', '0', '2', '0', '0', '1'],
       '7',
       5,
       'Draw: 5',
       [True, True, True, False, False, False, True, False, True, True],
       [0, 0, -1, 0, 1, 3, 1, 3, 1, 1],
       38480930669174444566426826324563146081),
      ('Dayna Deruelle',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144346&profileid=26636#1',
       False,
       ['0', '0', '1', '0', '0', '0', '1', '0', '3', '1', '0'],
       '6',
       5,
       'Draw: 5',
       [False, True, True, False, True, True, True, False, True, False, False],
       [0, -1, -1, 0, -1, -1, -3, -2, -4, -1, 0],
       153896726080791122415283970396986089830),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144352&profileid=12477#1',
       True,
       ['1', '0', '0', '1', '0', '2', '0', '2', '0', '0', '1'],
       '7',
       5,
       'Draw: 5',
       [True, False, False, True, False, False, False, True, False, True, True],
       [0, 1, 1, 0, 1, 1, 3, 2, 4, 1, 0],
       153896726080791122415283970396986089830)],
     [('Richard Krell',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962#1',
       False,
       ['0', '0', '1', '1', '0', '0', '1', '0', 'X'],
       '3',
       6,
       'Draw: 6',
       [False, False, True, False, False, True, True, False, True],
       [0, 0, -2, -1, 0, -2, -5, -4, -5],
       209637313717849892067917714730669554285),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
       True,
       ['0', '2', '0', '0', '2', '3', '0', '1', 'X'],
       '8',
       6,
       'Draw: 6',
       [True, True, False, True, True, False, False, True, False],
       [0, 0, 2, 1, 0, 2, 5, 4, 5],
       209637313717849892067917714730669554285)],
     [('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
       False,
       ['0', '0', '1', '1', '0', '3', '0', '0', '1', '0'],
       '6',
       7,
       'Draw: 7',
       [False, False, True, False, False, True, False, False, True, False],
       [0, 0, -1, 0, 1, -2, 1, 1, 0, 1],
       274892128276167031788079435153352244862),
      ('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       True,
       ['0', '1', '0', '0', '3', '0', '0', '1', '0', '2'],
       '7',
       7,
       'Draw: 7',
       [True, True, False, True, True, False, True, True, False, True],
       [0, 0, 1, 0, -1, 2, -1, -1, 0, -1],
       274892128276167031788079435153352244862)]]



```python
event.get_flat_boxscores()[0]
```




    [('Damien Villard',
      'event.php?view=Team&eventid=6400&teamid=144354&profileid=27373#1',
      True,
      ['0', '0', '0', '0', 'X'],
      '0',
      1,
      'Draw: 1',
      [True, True, True, True, True],
      [0, -1, -4, -6, -8],
      227597408989477916004520082463493572762),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      False,
      ['1', '3', '2', '2', 'X'],
      '8',
      1,
      'Draw: 1',
      [False, False, False, False, False],
      [0, 1, 4, 6, 8],
      227597408989477916004520082463493572762),
     ('Matthew Mepstead',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144356#1',
      False,
      ['0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'],
      '4',
      1,
      'Draw: 1',
      [False, False, True, False, False, True, False, False, False, True, False],
      [0, 0, -2, -1, 0, -1, 0, 0, 0, -1, 0],
      230481195381514558834165699232540581342),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['0', '2', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
      '5',
      1,
      'Draw: 1',
      [True, True, False, True, True, False, True, True, True, False, True],
      [0, 0, 2, 1, 0, 1, 0, 0, 0, 1, 0],
      230481195381514558834165699232540581342),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
      False,
      ['0', '2', '0', '1', '0', '2', '2', '0', '2', 'X'],
      '9',
      1,
      'Draw: 1',
      [False, False, False, False, False, True, False, False, True, False],
      [0, 0, 2, 2, 3, 2, 4, 6, 3, 5],
      123876478142928441769100783560984935273),
     ('Sam Steep',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144351&profileid=25978#1',
      True,
      ['0', '0', '0', '0', '1', '0', '0', '3', '0', 'X'],
      '4',
      1,
      'Draw: 1',
      [True, True, True, True, True, False, True, True, False, True],
      [0, 0, -2, -2, -3, -2, -4, -6, -3, -5],
      123876478142928441769100783560984935273)]



```python
event.get_flat_boxscores()[-1]
```




    [('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
      False,
      ['0', '0', '1', '1', '0', '3', '0', '0', '1', '0'],
      '6',
      7,
      'Draw: 7',
      [False, False, True, False, False, True, False, False, True, False],
      [0, 0, -1, 0, 1, -2, 1, 1, 0, 1],
      274892128276167031788079435153352244862),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      True,
      ['0', '1', '0', '0', '3', '0', '0', '1', '0', '2'],
      '7',
      7,
      'Draw: 7',
      [True, True, False, True, True, False, True, True, False, True],
      [0, 0, 1, 0, -1, 2, -1, -1, 0, -1],
      274892128276167031788079435153352244862)]



## About czapi
czapi is a Python library for scraping curling linescores.
