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




    254872352347969208886538144781320061225



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
      110977284151530368674865625905288531344),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      False,
      ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
      '7',
      2,
      'Draw: 2',
      [False, False, True, False, False, False, False, True, True, True],
      [0, 0, -2, 2, 2, 2, 3, 2, 1, 0],
      110977284151530368674865625905288531344),
     ('Dayna Deruelle',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1',
      False,
      ['0', '0', '1', '0', '0', '0', '0', 'X'],
      '1',
      2,
      'Draw: 2',
      [False, False, True, False, True, True, True, True],
      [0, 0, -2, -1, -3, -4, -5, -9],
      281037030105321216581538059786156947039),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['0', '2', '0', '2', '1', '1', '4', 'X'],
      '10',
      2,
      'Draw: 2',
      [True, True, False, True, False, False, False, False],
      [0, 0, 2, 1, 3, 4, 5, 9],
      281037030105321216581538059786156947039),
     ('Mark Kean',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
      True,
      ['2', '0', '1', '0', '0', '0', '1', '3', 'X'],
      '7',
      2,
      'Draw: 2',
      [True, False, False, False, False, True, True, False, False],
      [0, 2, 2, 3, 3, 1, 0, 1, 4],
      303564892705226366466039024191702968265),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
      False,
      ['0', '0', '0', '0', '2', '1', '0', '0', 'X'],
      '3',
      2,
      'Draw: 2',
      [False, True, True, True, True, False, False, True, True],
      [0, -2, -2, -3, -3, -1, 0, -1, -4],
      303564892705226366466039024191702968265),
     ('Richard Krell',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1',
      True,
      ['2', '0', '1', '0', '2', '1', '1', 'X'],
      '7',
      2,
      'Draw: 2',
      [True, False, False, False, True, False, False, False],
      [0, 2, 2, 3, 2, 4, 5, 6],
      166631958339420315484541615590740859900),
     ('Rob Ainsley',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
      False,
      ['0', '0', '0', '1', '0', '0', '0', 'X'],
      '1',
      2,
      'Draw: 2',
      [False, True, True, True, False, True, True, True],
      [0, -2, -2, -3, -2, -4, -5, -6],
      166631958339420315484541615590740859900)]



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



The `get_flat_boxscores` method can be used to return a list of tuples of all the boxscore information on all the linescore pages.

```python
event.get_flat_boxscores(flat=True)
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
      43389014760302404335281282239904734529),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      False,
      ['1', '3', '2', '2', 'X'],
      '8',
      1,
      'Draw: 1',
      [False, False, False, False, False],
      [0, 1, 4, 6, 8],
      43389014760302404335281282239904734529),
     ('Matthew Mepstead',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144356#1',
      False,
      ['0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'],
      '4',
      1,
      'Draw: 1',
      [False, False, True, False, False, True, False, False, False, True, False],
      [0, 0, -2, -1, 0, -1, 0, 0, 0, -1, 0],
      6662255676714105164637017444793308623),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['0', '2', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
      '5',
      1,
      'Draw: 1',
      [True, True, False, True, True, False, True, True, True, False, True],
      [0, 0, 2, 1, 0, 1, 0, 0, 0, 1, 0],
      6662255676714105164637017444793308623),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
      False,
      ['0', '2', '0', '1', '0', '2', '2', '0', '2', 'X'],
      '9',
      1,
      'Draw: 1',
      [False, False, False, False, False, True, False, False, True, False],
      [0, 0, 2, 2, 3, 2, 4, 6, 3, 5],
      17030269709905985666285035488407089412),
     ('Sam Steep',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144351&profileid=25978#1',
      True,
      ['0', '0', '0', '0', '1', '0', '0', '3', '0', 'X'],
      '4',
      1,
      'Draw: 1',
      [True, True, True, True, True, False, True, True, False, True],
      [0, 0, -2, -2, -3, -2, -4, -6, -3, -5],
      17030269709905985666285035488407089412),
     ('Wayne Tuck Jr.',
      'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
      True,
      ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
      '5',
      2,
      'Draw: 2',
      [True, True, False, True, True, True, True, False, False, False],
      [0, 0, 2, -2, -2, -2, -3, -2, -1, 0],
      313404218084099692187707048891717611105),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      False,
      ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
      '7',
      2,
      'Draw: 2',
      [False, False, True, False, False, False, False, True, True, True],
      [0, 0, -2, 2, 2, 2, 3, 2, 1, 0],
      313404218084099692187707048891717611105),
     ('Dayna Deruelle',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1',
      False,
      ['0', '0', '1', '0', '0', '0', '0', 'X'],
      '1',
      2,
      'Draw: 2',
      [False, False, True, False, True, True, True, True],
      [0, 0, -2, -1, -3, -4, -5, -9],
      224977155232527024595381121941485598994),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['0', '2', '0', '2', '1', '1', '4', 'X'],
      '10',
      2,
      'Draw: 2',
      [True, True, False, True, False, False, False, False],
      [0, 0, 2, 1, 3, 4, 5, 9],
      224977155232527024595381121941485598994),
     ('Mark Kean',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
      True,
      ['2', '0', '1', '0', '0', '0', '1', '3', 'X'],
      '7',
      2,
      'Draw: 2',
      [True, False, False, False, False, True, True, False, False],
      [0, 2, 2, 3, 3, 1, 0, 1, 4],
      268773209381266610704731254952653425860),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
      False,
      ['0', '0', '0', '0', '2', '1', '0', '0', 'X'],
      '3',
      2,
      'Draw: 2',
      [False, True, True, True, True, False, False, True, True],
      [0, -2, -2, -3, -3, -1, 0, -1, -4],
      268773209381266610704731254952653425860),
     ('Richard Krell',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1',
      True,
      ['2', '0', '1', '0', '2', '1', '1', 'X'],
      '7',
      2,
      'Draw: 2',
      [True, False, False, False, True, False, False, False],
      [0, 2, 2, 3, 2, 4, 5, 6],
      336248271082593576004107249057533701469),
     ('Rob Ainsley',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
      False,
      ['0', '0', '0', '1', '0', '0', '0', 'X'],
      '1',
      2,
      'Draw: 2',
      [False, True, True, True, False, True, True, True],
      [0, -2, -2, -3, -2, -4, -5, -6],
      336248271082593576004107249057533701469),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      True,
      ['0', '0', '2', '1', '2', '1', '0', '2', 'X'],
      '8',
      3,
      'Draw: 3',
      [True, True, True, False, False, False, False, True, False],
      [0, 0, -1, 1, 2, 4, 5, 3, 5],
      80394010565261168427833483594968521544),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
      False,
      ['0', '1', '0', '0', '0', '0', '2', '0', 'X'],
      '3',
      3,
      'Draw: 3',
      [False, False, False, True, True, True, True, False, True],
      [0, 0, 1, -1, -2, -4, -5, -3, -5],
      80394010565261168427833483594968521544),
     ('Mark Kean',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
      True,
      ['0', '5', '0', '1', '1', '1', 'X'],
      '8',
      3,
      'Draw: 3',
      [True, True, False, True, False, False, False],
      [0, -1, 4, 3, 4, 5, 6],
      119576955346708354006974538451792040897),
     ('Richard Krell',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144349&profileid=25962#1',
      False,
      ['1', '0', '1', '0', '0', '0', 'X'],
      '2',
      3,
      'Draw: 3',
      [False, False, True, False, True, True, True],
      [0, 1, -4, -3, -4, -5, -6],
      119576955346708354006974538451792040897),
     ('Damien Villard',
      'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144354&profileid=27373#1',
      True,
      ['2', '1', '0', '1', '0', '0', '1', '0', '0', '0'],
      '5',
      3,
      'Draw: 3',
      [True, False, False, True, False, True, True, False, True, True],
      [0, 2, 3, 2, 3, 1, 1, 2, 1, 0],
      249838339623785495055373784217174441445),
     ('Sam Steep',
      'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144351&profileid=25978#1',
      False,
      ['0', '0', '1', '0', '2', '0', '0', '1', '1', '1'],
      '6',
      3,
      'Draw: 3',
      [False, True, True, False, True, False, False, True, False, False],
      [0, -2, -3, -2, -3, -1, -1, -2, -1, 0],
      249838339623785495055373784217174441445),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144350#1',
      True,
      ['1', '1', '0', '0', '0', '0', '2', '1', '2', 'X'],
      '7',
      3,
      'Draw: 3',
      [True, False, False, True, True, True, True, False, False, False],
      [0, 1, 2, 1, 0, 0, 0, 2, 3, 5],
      210696644732545105346666426932076387851),
     ('Matthew Mepstead',
      'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144356#1',
      False,
      ['0', '0', '1', '1', '0', '0', '0', '0', '0', 'X'],
      '2',
      3,
      'Draw: 3',
      [False, True, True, False, False, False, False, True, True, True],
      [0, -1, -2, -1, 0, 0, 0, -2, -3, -5],
      210696644732545105346666426932076387851),
     ('Wayne Tuck Jr.',
      'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144353&profileid=12486#1',
      False,
      ['0', '0', '0', '2', '0', '0', '0', '0', 'X'],
      '2',
      3,
      'Draw: 3',
      [False, True, True, True, False, True, True, True, True],
      [0, -2, -3, -3, -1, -2, -4, -5, -6],
      241487067026802204703372136757699352731),
     ('Rob Ainsley',
      'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
      True,
      ['2', '1', '0', '0', '1', '2', '1', '1', 'X'],
      '8',
      3,
      'Draw: 3',
      [True, False, False, False, True, False, False, False, False],
      [0, 2, 3, 3, 1, 2, 4, 5, 6],
      241487067026802204703372136757699352731),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      True,
      ['1', '0', '1', '0', '1', '0', '2', '0', '1', '0'],
      '6',
      4,
      'Draw: 4',
      [True, False, True, False, True, False, True, False, True, False],
      [0, 1, -1, 0, -2, -1, -2, 0, -1, 0],
      270312357553095148414284107284214840026),
     ('Mark Kean',
      'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961#1',
      False,
      ['0', '2', '0', '2', '0', '1', '0', '1', '0', '1'],
      '7',
      4,
      'Draw: 4',
      [False, True, False, True, False, True, False, True, False, True],
      [0, -1, 1, 0, 2, 1, 2, 0, 1, 0],
      270312357553095148414284107284214840026),
     ('Sam Steep',
      'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961&eventid=6400&teamid=144351&profileid=25978#1',
      False,
      ['1', '0', '0', '2', '0', '1', '1', '0', '1', '1'],
      '7',
      4,
      'Draw: 4',
      [False, False, True, True, False, True, False, False, True, False],
      [0, 1, 0, -2, 0, -2, -1, 0, -1, 0],
      184794641996927884703702998465135153852),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961&eventid=6400&teamid=144350#1',
      True,
      ['0', '1', '2', '0', '2', '0', '0', '1', '0', '0'],
      '6',
      4,
      'Draw: 4',
      [True, True, False, False, True, False, True, True, False, True],
      [0, -1, 0, 2, 0, 2, 1, 0, 1, 0],
      184794641996927884703702998465135153852),
     ('Dayna Deruelle',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144346&profileid=26636#1',
      False,
      ['0', '2', '1', '1', '1', '0', '3', 'X'],
      '8',
      4,
      'Draw: 4',
      [False, True, False, False, False, False, True, False],
      [0, -1, 1, 2, 3, 4, 3, 6],
      266895758911458277527113999576025156800),
     ('Rob Ainsley',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
      True,
      ['1', '0', '0', '0', '0', '1', '0', 'X'],
      '2',
      4,
      'Draw: 4',
      [True, False, True, True, True, True, False, True],
      [0, 1, -1, -2, -3, -4, -3, -6],
      266895758911458277527113999576025156800),
     ('Sam Steep',
      'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978#1',
      False,
      ['0', '1', '0', '0', '0', '2', '0', '2', '0', '0'],
      '5',
      5,
      'Draw: 5',
      [False, False, False, True, True, True, False, True, False, False],
      [0, 0, 1, 0, -1, -3, -1, -3, -1, -1],
      136987304340129398442436470707928288628),
     ('Richard Krell',
      'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962#1',
      True,
      ['0', '0', '1', '1', '2', '0', '2', '0', '0', '1'],
      '7',
      5,
      'Draw: 5',
      [True, True, True, False, False, False, True, False, True, True],
      [0, 0, -1, 0, 1, 3, 1, 3, 1, 1],
      136987304340129398442436470707928288628),
     ('Dayna Deruelle',
      'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144346&profileid=26636#1',
      False,
      ['0', '0', '1', '0', '0', '0', '1', '0', '3', '1', '0'],
      '6',
      5,
      'Draw: 5',
      [False, True, True, False, True, True, True, False, True, False, False],
      [0, -1, -1, 0, -1, -1, -3, -2, -4, -1, 0],
      177734897905324649583176141792839670599),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['1', '0', '0', '1', '0', '2', '0', '2', '0', '0', '1'],
      '7',
      5,
      'Draw: 5',
      [True, False, False, True, False, False, False, True, False, True, True],
      [0, 1, 1, 0, 1, 1, 3, 2, 4, 1, 0],
      177734897905324649583176141792839670599),
     ('Richard Krell',
      'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962#1',
      False,
      ['0', '0', '1', '1', '0', '0', '1', '0', 'X'],
      '3',
      6,
      'Draw: 6',
      [False, False, True, False, False, True, True, False, True],
      [0, 0, -2, -1, 0, -2, -5, -4, -5],
      14986686141022873231469018358016050284),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['0', '2', '0', '0', '2', '3', '0', '1', 'X'],
      '8',
      6,
      'Draw: 6',
      [True, True, False, True, True, False, False, True, False],
      [0, 0, 2, 1, 0, 2, 5, 4, 5],
      14986686141022873231469018358016050284),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
      False,
      ['0', '0', '1', '1', '0', '3', '0', '0', '1', '0'],
      '6',
      7,
      'Draw: 7',
      [False, False, True, False, False, True, False, False, True, False],
      [0, 0, -1, 0, 1, -2, 1, 1, 0, 1],
      33575543948478163326703320936787390518),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      True,
      ['0', '1', '0', '0', '3', '0', '0', '1', '0', '2'],
      '7',
      7,
      'Draw: 7',
      [True, True, False, True, True, False, True, True, False, True],
      [0, 0, 1, 0, -1, 2, -1, -1, 0, -1],
      33575543948478163326703320936787390518)]



The `get_flat_boxscores` method can also be used to return a list of `Boxscore` objects for convenience. 

```python
event.get_flat_boxscores(flat=False)
```




    [Boxscore(team_name='Damien Villard', href='event.php?view=Team&eventid=6400&teamid=144354&profileid=27373#1', hammer_start=True, score=['0', '0', '0', '0', 'X'], final_score='0', draw_num=1, draw='Draw: 1', hammer_progression=[True, True, True, True, True], relative_score=[0, -1, -4, -6, -8], guid=43389014760302404335281282239904734529),
     Boxscore(team_name='Matthew Hall', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', hammer_start=False, score=['1', '3', '2', '2', 'X'], final_score='8', draw_num=1, draw='Draw: 1', hammer_progression=[False, False, False, False, False], relative_score=[0, 1, 4, 6, 8], guid=43389014760302404335281282239904734529),
     Boxscore(team_name='Matthew Mepstead', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144356#1', hammer_start=False, score=['0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'], final_score='4', draw_num=1, draw='Draw: 1', hammer_progression=[False, False, True, False, False, True, False, False, False, True, False], relative_score=[0, 0, -2, -1, 0, -1, 0, 0, 0, -1, 0], guid=6662255676714105164637017444793308623),
     Boxscore(team_name='Tyler Stewart', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1', hammer_start=True, score=['0', '2', '0', '0', '1', '0', '0', '0', '1', '0', '1'], final_score='5', draw_num=1, draw='Draw: 1', hammer_progression=[True, True, False, True, True, False, True, True, True, False, True], relative_score=[0, 0, 2, 1, 0, 1, 0, 0, 0, 1, 0], guid=6662255676714105164637017444793308623),
     Boxscore(team_name='Jason March', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1', hammer_start=False, score=['0', '2', '0', '1', '0', '2', '2', '0', '2', 'X'], final_score='9', draw_num=1, draw='Draw: 1', hammer_progression=[False, False, False, False, False, True, False, False, True, False], relative_score=[0, 0, 2, 2, 3, 2, 4, 6, 3, 5], guid=17030269709905985666285035488407089412),
     Boxscore(team_name='Sam Steep', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144351&profileid=25978#1', hammer_start=True, score=['0', '0', '0', '0', '1', '0', '0', '3', '0', 'X'], final_score='4', draw_num=1, draw='Draw: 1', hammer_progression=[True, True, True, True, True, False, True, True, False, True], relative_score=[0, 0, -2, -2, -3, -2, -4, -6, -3, -5], guid=17030269709905985666285035488407089412),
     Boxscore(team_name='Wayne Tuck Jr.', href='event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1', hammer_start=True, score=['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'], final_score='5', draw_num=2, draw='Draw: 2', hammer_progression=[True, True, False, True, True, True, True, False, False, False], relative_score=[0, 0, 2, -2, -2, -2, -3, -2, -1, 0], guid=313404218084099692187707048891717611105),
     Boxscore(team_name='Matthew Hall', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', hammer_start=False, score=['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'], final_score='7', draw_num=2, draw='Draw: 2', hammer_progression=[False, False, True, False, False, False, False, True, True, True], relative_score=[0, 0, -2, 2, 2, 2, 3, 2, 1, 0], guid=313404218084099692187707048891717611105),
     Boxscore(team_name='Dayna Deruelle', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1', hammer_start=False, score=['0', '0', '1', '0', '0', '0', '0', 'X'], final_score='1', draw_num=2, draw='Draw: 2', hammer_progression=[False, False, True, False, True, True, True, True], relative_score=[0, 0, -2, -1, -3, -4, -5, -9], guid=224977155232527024595381121941485598994),
     Boxscore(team_name='Tyler Stewart', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1', hammer_start=True, score=['0', '2', '0', '2', '1', '1', '4', 'X'], final_score='10', draw_num=2, draw='Draw: 2', hammer_progression=[True, True, False, True, False, False, False, False], relative_score=[0, 0, 2, 1, 3, 4, 5, 9], guid=224977155232527024595381121941485598994),
     Boxscore(team_name='Mark Kean', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1', hammer_start=True, score=['2', '0', '1', '0', '0', '0', '1', '3', 'X'], final_score='7', draw_num=2, draw='Draw: 2', hammer_progression=[True, False, False, False, False, True, True, False, False], relative_score=[0, 2, 2, 3, 3, 1, 0, 1, 4], guid=268773209381266610704731254952653425860),
     Boxscore(team_name='Jason March', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1', hammer_start=False, score=['0', '0', '0', '0', '2', '1', '0', '0', 'X'], final_score='3', draw_num=2, draw='Draw: 2', hammer_progression=[False, True, True, True, True, False, False, True, True], relative_score=[0, -2, -2, -3, -3, -1, 0, -1, -4], guid=268773209381266610704731254952653425860),
     Boxscore(team_name='Richard Krell', href='event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1', hammer_start=True, score=['2', '0', '1', '0', '2', '1', '1', 'X'], final_score='7', draw_num=2, draw='Draw: 2', hammer_progression=[True, False, False, False, True, False, False, False], relative_score=[0, 2, 2, 3, 2, 4, 5, 6], guid=336248271082593576004107249057533701469),
     Boxscore(team_name='Rob Ainsley', href='event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1', hammer_start=False, score=['0', '0', '0', '1', '0', '0', '0', 'X'], final_score='1', draw_num=2, draw='Draw: 2', hammer_progression=[False, True, True, True, False, True, True, True], relative_score=[0, -2, -2, -3, -2, -4, -5, -6], guid=336248271082593576004107249057533701469),
     Boxscore(team_name='Matthew Hall', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', hammer_start=True, score=['0', '0', '2', '1', '2', '1', '0', '2', 'X'], final_score='8', draw_num=3, draw='Draw: 3', hammer_progression=[True, True, True, False, False, False, False, True, False], relative_score=[0, 0, -1, 1, 2, 4, 5, 3, 5], guid=80394010565261168427833483594968521544),
     Boxscore(team_name='Tyler Stewart', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1', hammer_start=False, score=['0', '1', '0', '0', '0', '0', '2', '0', 'X'], final_score='3', draw_num=3, draw='Draw: 3', hammer_progression=[False, False, False, True, True, True, True, False, True], relative_score=[0, 0, 1, -1, -2, -4, -5, -3, -5], guid=80394010565261168427833483594968521544),
     Boxscore(team_name='Mark Kean', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1', hammer_start=True, score=['0', '5', '0', '1', '1', '1', 'X'], final_score='8', draw_num=3, draw='Draw: 3', hammer_progression=[True, True, False, True, False, False, False], relative_score=[0, -1, 4, 3, 4, 5, 6], guid=119576955346708354006974538451792040897),
     Boxscore(team_name='Richard Krell', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144349&profileid=25962#1', hammer_start=False, score=['1', '0', '1', '0', '0', '0', 'X'], final_score='2', draw_num=3, draw='Draw: 3', hammer_progression=[False, False, True, False, True, True, True], relative_score=[0, 1, -4, -3, -4, -5, -6], guid=119576955346708354006974538451792040897),
     Boxscore(team_name='Damien Villard', href='event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144354&profileid=27373#1', hammer_start=True, score=['2', '1', '0', '1', '0', '0', '1', '0', '0', '0'], final_score='5', draw_num=3, draw='Draw: 3', hammer_progression=[True, False, False, True, False, True, True, False, True, True], relative_score=[0, 2, 3, 2, 3, 1, 1, 2, 1, 0], guid=249838339623785495055373784217174441445),
     Boxscore(team_name='Sam Steep', href='event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144351&profileid=25978#1', hammer_start=False, score=['0', '0', '1', '0', '2', '0', '0', '1', '1', '1'], final_score='6', draw_num=3, draw='Draw: 3', hammer_progression=[False, True, True, False, True, False, False, True, False, False], relative_score=[0, -2, -3, -2, -3, -1, -1, -2, -1, 0], guid=249838339623785495055373784217174441445),
     Boxscore(team_name='Jason March', href='event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144350#1', hammer_start=True, score=['1', '1', '0', '0', '0', '0', '2', '1', '2', 'X'], final_score='7', draw_num=3, draw='Draw: 3', hammer_progression=[True, False, False, True, True, True, True, False, False, False], relative_score=[0, 1, 2, 1, 0, 0, 0, 2, 3, 5], guid=210696644732545105346666426932076387851),
     Boxscore(team_name='Matthew Mepstead', href='event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144356#1', hammer_start=False, score=['0', '0', '1', '1', '0', '0', '0', '0', '0', 'X'], final_score='2', draw_num=3, draw='Draw: 3', hammer_progression=[False, True, True, False, False, False, False, True, True, True], relative_score=[0, -1, -2, -1, 0, 0, 0, -2, -3, -5], guid=210696644732545105346666426932076387851),
     Boxscore(team_name='Wayne Tuck Jr.', href='event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144353&profileid=12486#1', hammer_start=False, score=['0', '0', '0', '2', '0', '0', '0', '0', 'X'], final_score='2', draw_num=3, draw='Draw: 3', hammer_progression=[False, True, True, True, False, True, True, True, True], relative_score=[0, -2, -3, -3, -1, -2, -4, -5, -6], guid=241487067026802204703372136757699352731),
     Boxscore(team_name='Rob Ainsley', href='event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144345&profileid=15779#1', hammer_start=True, score=['2', '1', '0', '0', '1', '2', '1', '1', 'X'], final_score='8', draw_num=3, draw='Draw: 3', hammer_progression=[True, False, False, False, True, False, False, False, False], relative_score=[0, 2, 3, 3, 1, 2, 4, 5, 6], guid=241487067026802204703372136757699352731),
     Boxscore(team_name='Matthew Hall', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', hammer_start=True, score=['1', '0', '1', '0', '1', '0', '2', '0', '1', '0'], final_score='6', draw_num=4, draw='Draw: 4', hammer_progression=[True, False, True, False, True, False, True, False, True, False], relative_score=[0, 1, -1, 0, -2, -1, -2, 0, -1, 0], guid=270312357553095148414284107284214840026),
     Boxscore(team_name='Mark Kean', href='event.php?view=Team&eventid=6400&teamid=144348&profileid=25961#1', hammer_start=False, score=['0', '2', '0', '2', '0', '1', '0', '1', '0', '1'], final_score='7', draw_num=4, draw='Draw: 4', hammer_progression=[False, True, False, True, False, True, False, True, False, True], relative_score=[0, -1, 1, 0, 2, 1, 2, 0, 1, 0], guid=270312357553095148414284107284214840026),
     Boxscore(team_name='Sam Steep', href='event.php?view=Team&eventid=6400&teamid=144348&profileid=25961&eventid=6400&teamid=144351&profileid=25978#1', hammer_start=False, score=['1', '0', '0', '2', '0', '1', '1', '0', '1', '1'], final_score='7', draw_num=4, draw='Draw: 4', hammer_progression=[False, False, True, True, False, True, False, False, True, False], relative_score=[0, 1, 0, -2, 0, -2, -1, 0, -1, 0], guid=184794641996927884703702998465135153852),
     Boxscore(team_name='Jason March', href='event.php?view=Team&eventid=6400&teamid=144348&profileid=25961&eventid=6400&teamid=144350#1', hammer_start=True, score=['0', '1', '2', '0', '2', '0', '0', '1', '0', '0'], final_score='6', draw_num=4, draw='Draw: 4', hammer_progression=[True, True, False, False, True, False, True, True, False, True], relative_score=[0, -1, 0, 2, 0, 2, 1, 0, 1, 0], guid=184794641996927884703702998465135153852),
     Boxscore(team_name='Dayna Deruelle', href='event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144346&profileid=26636#1', hammer_start=False, score=['0', '2', '1', '1', '1', '0', '3', 'X'], final_score='8', draw_num=4, draw='Draw: 4', hammer_progression=[False, True, False, False, False, False, True, False], relative_score=[0, -1, 1, 2, 3, 4, 3, 6], guid=266895758911458277527113999576025156800),
     Boxscore(team_name='Rob Ainsley', href='event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1', hammer_start=True, score=['1', '0', '0', '0', '0', '1', '0', 'X'], final_score='2', draw_num=4, draw='Draw: 4', hammer_progression=[True, False, True, True, True, True, False, True], relative_score=[0, 1, -1, -2, -3, -4, -3, -6], guid=266895758911458277527113999576025156800),
     Boxscore(team_name='Sam Steep', href='event.php?view=Team&eventid=6400&teamid=144351&profileid=25978#1', hammer_start=False, score=['0', '1', '0', '0', '0', '2', '0', '2', '0', '0'], final_score='5', draw_num=5, draw='Draw: 5', hammer_progression=[False, False, False, True, True, True, False, True, False, False], relative_score=[0, 0, 1, 0, -1, -3, -1, -3, -1, -1], guid=136987304340129398442436470707928288628),
     Boxscore(team_name='Richard Krell', href='event.php?view=Team&eventid=6400&teamid=144349&profileid=25962#1', hammer_start=True, score=['0', '0', '1', '1', '2', '0', '2', '0', '0', '1'], final_score='7', draw_num=5, draw='Draw: 5', hammer_progression=[True, True, True, False, False, False, True, False, True, True], relative_score=[0, 0, -1, 0, 1, 3, 1, 3, 1, 1], guid=136987304340129398442436470707928288628),
     Boxscore(team_name='Dayna Deruelle', href='event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144346&profileid=26636#1', hammer_start=False, score=['0', '0', '1', '0', '0', '0', '1', '0', '3', '1', '0'], final_score='6', draw_num=5, draw='Draw: 5', hammer_progression=[False, True, True, False, True, True, True, False, True, False, False], relative_score=[0, -1, -1, 0, -1, -1, -3, -2, -4, -1, 0], guid=177734897905324649583176141792839670599),
     Boxscore(team_name='Tyler Stewart', href='event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144352&profileid=12477#1', hammer_start=True, score=['1', '0', '0', '1', '0', '2', '0', '2', '0', '0', '1'], final_score='7', draw_num=5, draw='Draw: 5', hammer_progression=[True, False, False, True, False, False, False, True, False, True, True], relative_score=[0, 1, 1, 0, 1, 1, 3, 2, 4, 1, 0], guid=177734897905324649583176141792839670599),
     Boxscore(team_name='Richard Krell', href='event.php?view=Team&eventid=6400&teamid=144349&profileid=25962#1', hammer_start=False, score=['0', '0', '1', '1', '0', '0', '1', '0', 'X'], final_score='3', draw_num=6, draw='Draw: 6', hammer_progression=[False, False, True, False, False, True, True, False, True], relative_score=[0, 0, -2, -1, 0, -2, -5, -4, -5], guid=14986686141022873231469018358016050284),
     Boxscore(team_name='Tyler Stewart', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1', hammer_start=True, score=['0', '2', '0', '0', '2', '3', '0', '1', 'X'], final_score='8', draw_num=6, draw='Draw: 6', hammer_progression=[True, True, False, True, True, False, False, True, False], relative_score=[0, 0, 2, 1, 0, 2, 5, 4, 5], guid=14986686141022873231469018358016050284),
     Boxscore(team_name='Tyler Stewart', href='event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1', hammer_start=False, score=['0', '0', '1', '1', '0', '3', '0', '0', '1', '0'], final_score='6', draw_num=7, draw='Draw: 7', hammer_progression=[False, False, True, False, False, True, False, False, True, False], relative_score=[0, 0, -1, 0, 1, -2, 1, 1, 0, 1], guid=33575543948478163326703320936787390518),
     Boxscore(team_name='Matthew Hall', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', hammer_start=True, score=['0', '1', '0', '0', '3', '0', '0', '1', '0', '2'], final_score='7', draw_num=7, draw='Draw: 7', hammer_progression=[True, True, False, True, True, False, True, True, False, True], relative_score=[0, 0, 1, 0, -1, 2, -1, -1, 0, -1], guid=33575543948478163326703320936787390518)]



```python
event.get_flat_boxscores()[0]
```




    Boxscore(team_name='Damien Villard', href='event.php?view=Team&eventid=6400&teamid=144354&profileid=27373#1', hammer_start=True, score=['0', '0', '0', '0', 'X'], final_score='0', draw_num=1, draw='Draw: 1', hammer_progression=[True, True, True, True, True], relative_score=[0, -1, -4, -6, -8], guid=43389014760302404335281282239904734529)



```python
event.get_flat_boxscores()[-1]
```




    Boxscore(team_name='Matthew Hall', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', hammer_start=True, score=['0', '1', '0', '0', '3', '0', '0', '1', '0', '2'], final_score='7', draw_num=7, draw='Draw: 7', hammer_progression=[True, True, False, True, True, False, True, True, False, True], relative_score=[0, 0, 1, 0, -1, 2, -1, -1, 0, -1], guid=33575543948478163326703320936787390518)



## About czapi
czapi is a Python library for scraping curling linescores.
