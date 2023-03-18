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




    [{'Wayne Tuck Jr.': {'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
       'score': ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
       'hammer': True,
       'finalscore': '5'},
      'Matthew Hall': {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       'score': ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
       'hammer': False,
       'finalscore': '7'}},
     {'Dayna Deruelle': {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1',
       'score': ['0', '0', '1', '0', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '1'},
      'Tyler Stewart': {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
       'score': ['0', '2', '0', '2', '1', '1', '4', 'X'],
       'hammer': True,
       'finalscore': '10'}},
     {'Mark Kean': {'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
       'score': ['2', '0', '1', '0', '0', '0', '1', '3', 'X'],
       'hammer': True,
       'finalscore': '7'},
      'Jason March': {'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
       'score': ['0', '0', '0', '0', '2', '1', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '3'}},
     {'Richard Krell': {'href': 'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1',
       'score': ['2', '0', '1', '0', '2', '1', '1', 'X'],
       'hammer': True,
       'finalscore': '7'},
      'Rob Ainsley': {'href': 'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       'score': ['0', '0', '0', '1', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '1'}}]



A boxscore is returned as a dictionary of team names, game information dictionary key, value pairs.

Each game information dictionary contains:

* 'href' key with a corresponding string value of CurlingZone IDs identifying the team.
* 'hammer' key with corresponding boolean value of whether or not that team started the game with hammer.
* 'score' key with corresponding list of string value of end-by-end results for that team.
* 'finalscore' key with corresponding final score for the team.

Individual boxscores can be accessed through the `get_boxscore_from` method.

```python
boxscore = linescore_page.get_boxscore_from(cz_game_id = 1)
boxscore
```




    {'Wayne Tuck Jr.': {'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
      'score': ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
      'hammer': True,
      'finalscore': '5'},
     'Matthew Hall': {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      'score': ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
      'hammer': False,
      'finalscore': '7'}}



`cz_game_id` argument corresponds to the number the boxscore appears in on the linescore page.

The LinescorePage object contains these properties which details information on the boxscores:

* event_name
* event_date
* draw

```python
print(linescore_page.event_name,',',linescore_page.event_date,',' ,linescore_page.draw)
```

    Ontario Tankard - Open Qualifier , Jan 17 - 19, 2020 , Draw: 2


For convenience, upon instantiation of a `LinescorePage` object, a `NormalizedBoxscore` instance for each boxscore is created. A `NormalizedBoxscore` holds the same information as a boxscore dictionary with two new pieces of information added: 
1. The hammer progression for both teams throughout the game, i.e. who had hammer in what end.
2. Each team's relative score, i.e. who was up/down X after end Y.

```python
normalized_boxscore = linescore_page.get_normalized_boxscore_from(cz_game_id = 1)
normalized_boxscore
```




    NormalizedBoxscore(boxscore={'Wayne Tuck Jr.': {'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1', 'score': ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'], 'hammer': True, 'finalscore': '5'}, 'Matthew Hall': {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', 'score': ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'], 'hammer': False, 'finalscore': '7'}})



A `NormalizedBoxscore` object holds two `NormalizedHalfBoxscore` instances. 

```python
normalized_boxscore.normalized_half_boxscore_pair[0]
```




    NormalizedHalfBoxscore(team_name='Wayne Tuck Jr.', href='event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1', hammer=True, score=['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'], finalscore='5', hammer_progression=[True, True, False, True, True, True, True, False, False, False], normalized_score=[0, 2, -2, -2, -2, -3, -2, -1, 0, -2])



For Wayne Tuck Jr. the `hammer_progression` attribute can be interpreted as follows: 

* After end 1: Wayne had hammer
* After end 2: Wayne didn't have hammer
* After end 3: Wayne had hammer
* And so on and so forth..

```python
normalized_boxscore.normalized_half_boxscore_pair[-1]
```




    NormalizedHalfBoxscore(team_name='Matthew Hall', href='event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1', hammer=False, score=['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'], finalscore='7', hammer_progression=[False, False, True, False, False, False, False, True, True, True], normalized_score=[0, -2, 2, 2, 2, 3, 2, 1, 0, 2])



For Matthew Hall, the `normalized_score` attribute can be interpreted as follows:

* After end 1: Matthew was tied.
* After end 2: Matthew was down 2.
* After end 3: Matthew was up 2.
* And so on and so forth..

You'll also notice the `NormalizedBoxscore` object has a guid property which identifies that two `NormalizedHalfBoxscore` belong to the same game.

```python
normalized_boxscore.guid
```




    252991931913848772072809345195834379891



czapi's `get_flat_boxscores_from` function takes a `cz_event_id` and `cz_draw_id` as an arguments and returns a (flat) nested list object of all the boxscore information on the linescore page. This nested list object can be ingested into a pandas DataFrame or pushed to a SQL database.

```python
api.get_flat_boxscores_from(cz_event_id = 6400, cz_draw_id = 2)
```




    [('Wayne Tuck Jr.',
      'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
      True,
      ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
      '5',
      [True, True, False, True, True, True, True, False, False, False],
      [0, 2, -2, -2, -2, -3, -2, -1, 0, -2],
      299564467119177178972065881924464288266),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      False,
      ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
      '7',
      [False, False, True, False, False, False, False, True, True, True],
      [0, -2, 2, 2, 2, 3, 2, 1, 0, 2],
      299564467119177178972065881924464288266),
     ('Dayna Deruelle',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1',
      False,
      ['0', '0', '1', '0', '0', '0', '0', 'X'],
      '1',
      [False, False, True, False, True, True, True],
      [0, -2, -1, -3, -4, -5, -9],
      225166236441736262293031002646839082584),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['0', '2', '0', '2', '1', '1', '4', 'X'],
      '10',
      [True, True, False, True, False, False, False],
      [0, 2, 1, 3, 4, 5, 9],
      225166236441736262293031002646839082584),
     ('Mark Kean',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
      True,
      ['2', '0', '1', '0', '0', '0', '1', '3', 'X'],
      '7',
      [True, False, False, False, False, True, True, False],
      [2, 2, 3, 3, 1, 0, 1, 4],
      268926374079317223867984892115735644609),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
      False,
      ['0', '0', '0', '0', '2', '1', '0', '0', 'X'],
      '3',
      [False, True, True, True, True, False, False, True],
      [-2, -2, -3, -3, -1, 0, -1, -4],
      268926374079317223867984892115735644609),
     ('Richard Krell',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1',
      True,
      ['2', '0', '1', '0', '2', '1', '1', 'X'],
      '7',
      [True, False, False, False, True, False, False],
      [2, 2, 3, 2, 4, 5, 6],
      127589252033958326010669452541180740950),
     ('Rob Ainsley',
      'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
      False,
      ['0', '0', '0', '1', '0', '0', '0', 'X'],
      '1',
      [False, True, True, True, False, True, True],
      [-2, -2, -3, -2, -4, -5, -6],
      127589252033958326010669452541180740950)]



## Event

The `Event` object is a data structure which holds all of the `LinescorePage` objects which make up an entire event. 

An `Event` instance is created by passing a `cz_event_id`.

```python
event = api.Event(cz_event_id = 6400,delay=5,verbose=True)
event
```

    Scraping draw 1.
    Scraping draw 2.
    Scraping draw 3.
    Scraping draw 4.
    Scraping draw 5.
    Scraping draw 6.
    Scraping draw 7.





    Event(cz_event_id=6400, delay=5, verbose=True)



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




    [{'Matthew Hall': {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       'score': ['0', '0', '2', '1', '2', '1', '0', '2', 'X'],
       'hammer': True,
       'finalscore': '8'},
      'Tyler Stewart': {'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
       'score': ['0', '1', '0', '0', '0', '0', '2', '0', 'X'],
       'hammer': False,
       'finalscore': '3'}},
     {'Mark Kean': {'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
       'score': ['0', '5', '0', '1', '1', '1', 'X'],
       'hammer': True,
       'finalscore': '8'},
      'Richard Krell': {'href': 'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144349&profileid=25962#1',
       'score': ['1', '0', '1', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '2'}},
     {'Damien Villard': {'href': 'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144354&profileid=27373#1',
       'score': ['2', '1', '0', '1', '0', '0', '1', '0', '0', '0'],
       'hammer': True,
       'finalscore': '5'},
      'Sam Steep': {'href': 'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144351&profileid=25978#1',
       'score': ['0', '0', '1', '0', '2', '0', '0', '1', '1', '1'],
       'hammer': False,
       'finalscore': '6'}},
     {'Jason March': {'href': 'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144350#1',
       'score': ['1', '1', '0', '0', '0', '0', '2', '1', '2', 'X'],
       'hammer': True,
       'finalscore': '7'},
      'Matthew Mepstead': {'href': 'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144356#1',
       'score': ['0', '0', '1', '1', '0', '0', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '2'}},
     {'Wayne Tuck Jr.': {'href': 'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144353&profileid=12486#1',
       'score': ['0', '0', '0', '2', '0', '0', '0', '0', 'X'],
       'hammer': False,
       'finalscore': '2'},
      'Rob Ainsley': {'href': 'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
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
       [True, True, True, True],
       [-1, -4, -6, -8],
       92557652136658576678412699092377882692),
      ('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       False,
       ['1', '3', '2', '2', 'X'],
       '8',
       [False, False, False, False],
       [1, 4, 6, 8],
       92557652136658576678412699092377882692),
      ('Matthew Mepstead',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144356#1',
       False,
       ['0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'],
       '4',
       [False, False, True, False, False, True, False, False, False, True, False],
       [0, -2, -1, 0, -1, 0, 0, 0, -1, 0, -1],
       74505835530428901598709612439134825027),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
       True,
       ['0', '2', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
       '5',
       [True, True, False, True, True, False, True, True, True, False, True],
       [0, 2, 1, 0, 1, 0, 0, 0, 1, 0, 1],
       74505835530428901598709612439134825027),
      ('Jason March',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
       False,
       ['0', '2', '0', '1', '0', '2', '2', '0', '2', 'X'],
       '9',
       [False, False, False, False, False, True, False, False, True],
       [0, 2, 2, 3, 2, 4, 6, 3, 5],
       42581081463875970061015035008045933248),
      ('Sam Steep',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144351&profileid=25978#1',
       True,
       ['0', '0', '0', '0', '1', '0', '0', '3', '0', 'X'],
       '4',
       [True, True, True, True, True, False, True, True, False],
       [0, -2, -2, -3, -2, -4, -6, -3, -5],
       42581081463875970061015035008045933248)],
     [('Wayne Tuck Jr.',
       'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
       True,
       ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
       '5',
       [True, True, False, True, True, True, True, False, False, False],
       [0, 2, -2, -2, -2, -3, -2, -1, 0, -2],
       67107954024391153327206922837074465185),
      ('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       False,
       ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
       '7',
       [False, False, True, False, False, False, False, True, True, True],
       [0, -2, 2, 2, 2, 3, 2, 1, 0, 2],
       67107954024391153327206922837074465185),
      ('Dayna Deruelle',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144346&profileid=26636#1',
       False,
       ['0', '0', '1', '0', '0', '0', '0', 'X'],
       '1',
       [False, False, True, False, True, True, True],
       [0, -2, -1, -3, -4, -5, -9],
       174790955766132023378787171289976973883),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
       True,
       ['0', '2', '0', '2', '1', '1', '4', 'X'],
       '10',
       [True, True, False, True, False, False, False],
       [0, 2, 1, 3, 4, 5, 9],
       174790955766132023378787171289976973883),
      ('Mark Kean',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
       True,
       ['2', '0', '1', '0', '0', '0', '1', '3', 'X'],
       '7',
       [True, False, False, False, False, True, True, False],
       [2, 2, 3, 3, 1, 0, 1, 4],
       272159760578274287088902305331625102314),
      ('Jason March',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
       False,
       ['0', '0', '0', '0', '2', '1', '0', '0', 'X'],
       '3',
       [False, True, True, True, True, False, False, True],
       [-2, -2, -3, -3, -1, 0, -1, -4],
       272159760578274287088902305331625102314),
      ('Richard Krell',
       'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144349&profileid=25962#1',
       True,
       ['2', '0', '1', '0', '2', '1', '1', 'X'],
       '7',
       [True, False, False, False, True, False, False],
       [2, 2, 3, 2, 4, 5, 6],
       243919144346090251121838190768057531471),
      ('Rob Ainsley',
       'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       False,
       ['0', '0', '0', '1', '0', '0', '0', 'X'],
       '1',
       [False, True, True, True, False, True, True],
       [-2, -2, -3, -2, -4, -5, -6],
       243919144346090251121838190768057531471)],
     [('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       True,
       ['0', '0', '2', '1', '2', '1', '0', '2', 'X'],
       '8',
       [True, True, True, False, False, False, False, True],
       [0, -1, 1, 2, 4, 5, 3, 5],
       335406458745785025688024582237718303771),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
       False,
       ['0', '1', '0', '0', '0', '0', '2', '0', 'X'],
       '3',
       [False, False, False, True, True, True, True, False],
       [0, 1, -1, -2, -4, -5, -3, -5],
       335406458745785025688024582237718303771),
      ('Mark Kean',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144348&profileid=25961#1',
       True,
       ['0', '5', '0', '1', '1', '1', 'X'],
       '8',
       [True, True, False, True, False, False],
       [-1, 4, 3, 4, 5, 6],
       3357439244714183352725794717881628513),
      ('Richard Krell',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144349&profileid=25962#1',
       False,
       ['1', '0', '1', '0', '0', '0', 'X'],
       '2',
       [False, False, True, False, True, True],
       [1, -4, -3, -4, -5, -6],
       3357439244714183352725794717881628513),
      ('Damien Villard',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144354&profileid=27373#1',
       True,
       ['2', '1', '0', '1', '0', '0', '1', '0', '0', '0'],
       '5',
       [True, False, False, True, False, True, True, False, True, True],
       [2, 3, 2, 3, 1, 1, 2, 1, 0, -1],
       210455801410133174375994499476912196801),
      ('Sam Steep',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144351&profileid=25978#1',
       False,
       ['0', '0', '1', '0', '2', '0', '0', '1', '1', '1'],
       '6',
       [False, True, True, False, True, False, False, True, False, False],
       [-2, -3, -2, -3, -1, -1, -2, -1, 0, 1],
       210455801410133174375994499476912196801),
      ('Jason March',
       'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144350#1',
       True,
       ['1', '1', '0', '0', '0', '0', '2', '1', '2', 'X'],
       '7',
       [True, False, False, True, True, True, True, False, False],
       [1, 2, 1, 0, 0, 0, 2, 3, 5],
       243087565248420153757039504090677676604),
      ('Matthew Mepstead',
       'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978&eventid=6400&teamid=144356#1',
       False,
       ['0', '0', '1', '1', '0', '0', '0', '0', '0', 'X'],
       '2',
       [False, True, True, False, False, False, False, True, True],
       [-1, -2, -1, 0, 0, 0, -2, -3, -5],
       243087565248420153757039504090677676604),
      ('Wayne Tuck Jr.',
       'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144353&profileid=12486#1',
       False,
       ['0', '0', '0', '2', '0', '0', '0', '0', 'X'],
       '2',
       [False, True, True, True, False, True, True, True],
       [-2, -3, -3, -1, -2, -4, -5, -6],
       137931898261054906956754355272618841462),
      ('Rob Ainsley',
       'event.php?view=Team&eventid=6400&teamid=144356&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       True,
       ['2', '1', '0', '0', '1', '2', '1', '1', 'X'],
       '8',
       [True, False, False, False, True, False, False, False],
       [2, 3, 3, 1, 2, 4, 5, 6],
       137931898261054906956754355272618841462)],
     [('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       True,
       ['1', '0', '1', '0', '1', '0', '2', '0', '1', '0'],
       '6',
       [True, False, True, False, True, False, True, False, True, False],
       [1, -1, 0, -2, -1, -2, 0, -1, 0, -1],
       317958622457967356642328117515298869332),
      ('Mark Kean',
       'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961#1',
       False,
       ['0', '2', '0', '2', '0', '1', '0', '1', '0', '1'],
       '7',
       [False, True, False, True, False, True, False, True, False, True],
       [-1, 1, 0, 2, 1, 2, 0, 1, 0, 1],
       317958622457967356642328117515298869332),
      ('Sam Steep',
       'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961&eventid=6400&teamid=144351&profileid=25978#1',
       False,
       ['1', '0', '0', '2', '0', '1', '1', '0', '1', '1'],
       '7',
       [False, False, True, True, False, True, False, False, True, False],
       [1, 0, -2, 0, -2, -1, 0, -1, 0, 1],
       51799212557424957269051274857957470538),
      ('Jason March',
       'event.php?view=Team&eventid=6400&teamid=144348&profileid=25961&eventid=6400&teamid=144350#1',
       True,
       ['0', '1', '2', '0', '2', '0', '0', '1', '0', '0'],
       '6',
       [True, True, False, False, True, False, True, True, False, True],
       [-1, 0, 2, 0, 2, 1, 0, 1, 0, -1],
       51799212557424957269051274857957470538),
      ('Dayna Deruelle',
       'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144346&profileid=26636#1',
       False,
       ['0', '2', '1', '1', '1', '0', '3', 'X'],
       '8',
       [False, True, False, False, False, False, True],
       [-1, 1, 2, 3, 4, 3, 6],
       194657289779722731927805558345645496540),
      ('Rob Ainsley',
       'event.php?view=Team&eventid=6400&teamid=144350&profileid=0&eventid=6400&teamid=144345&profileid=15779#1',
       True,
       ['1', '0', '0', '0', '0', '1', '0', 'X'],
       '2',
       [True, False, True, True, True, True, False],
       [1, -1, -2, -3, -4, -3, -6],
       194657289779722731927805558345645496540)],
     [('Sam Steep',
       'event.php?view=Team&eventid=6400&teamid=144351&profileid=25978#1',
       False,
       ['0', '1', '0', '0', '0', '2', '0', '2', '0', '0'],
       '5',
       [False, False, False, True, True, True, False, True, False, False],
       [0, 1, 0, -1, -3, -1, -3, -1, -1, -2],
       167330822751632288338617747925261926914),
      ('Richard Krell',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962#1',
       True,
       ['0', '0', '1', '1', '2', '0', '2', '0', '0', '1'],
       '7',
       [True, True, True, False, False, False, True, False, True, True],
       [0, -1, 0, 1, 3, 1, 3, 1, 1, 2],
       167330822751632288338617747925261926914),
      ('Dayna Deruelle',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144346&profileid=26636#1',
       False,
       ['0', '0', '1', '0', '0', '0', '1', '0', '3', '1', '0'],
       '6',
       [False, True, True, False, True, True, True, False, True, False, False],
       [-1, -1, 0, -1, -1, -3, -2, -4, -1, 0, -1],
       337821161345022954627983701079777872530),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962&eventid=6400&teamid=144352&profileid=12477#1',
       True,
       ['1', '0', '0', '1', '0', '2', '0', '2', '0', '0', '1'],
       '7',
       [True, False, False, True, False, False, False, True, False, True, True],
       [1, 1, 0, 1, 1, 3, 2, 4, 1, 0, 1],
       337821161345022954627983701079777872530)],
     [('Richard Krell',
       'event.php?view=Team&eventid=6400&teamid=144349&profileid=25962#1',
       False,
       ['0', '0', '1', '1', '0', '0', '1', '0', 'X'],
       '3',
       [False, False, True, False, False, True, True, False],
       [0, -2, -1, 0, -2, -5, -4, -5],
       41205107010607414736022727949465576436),
      ('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
       True,
       ['0', '2', '0', '0', '2', '3', '0', '1', 'X'],
       '8',
       [True, True, False, True, True, False, False, True],
       [0, 2, 1, 0, 2, 5, 4, 5],
       41205107010607414736022727949465576436)],
     [('Tyler Stewart',
       'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
       False,
       ['0', '0', '1', '1', '0', '3', '0', '0', '1', '0'],
       '6',
       [False, False, True, False, False, True, False, False, True, False],
       [0, -1, 0, 1, -2, 1, 1, 0, 1, -1],
       337656267050323493383665822966511297443),
      ('Matthew Hall',
       'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
       True,
       ['0', '1', '0', '0', '3', '0', '0', '1', '0', '2'],
       '7',
       [True, True, False, True, True, False, True, True, False, True],
       [0, 1, 0, -1, 2, -1, -1, 0, -1, 1],
       337656267050323493383665822966511297443)]]



```python
event.get_flat_boxscores()[0]
```




    [('Damien Villard',
      'event.php?view=Team&eventid=6400&teamid=144354&profileid=27373#1',
      True,
      ['0', '0', '0', '0', 'X'],
      '0',
      [True, True, True, True],
      [-1, -4, -6, -8],
      92557652136658576678412699092377882692),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      False,
      ['1', '3', '2', '2', 'X'],
      '8',
      [False, False, False, False],
      [1, 4, 6, 8],
      92557652136658576678412699092377882692),
     ('Matthew Mepstead',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144356#1',
      False,
      ['0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '0'],
      '4',
      [False, False, True, False, False, True, False, False, False, True, False],
      [0, -2, -1, 0, -1, 0, 0, 0, -1, 0, -1],
      74505835530428901598709612439134825027),
     ('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435&eventid=6400&teamid=144352&profileid=12477#1',
      True,
      ['0', '2', '0', '0', '1', '0', '0', '0', '1', '0', '1'],
      '5',
      [True, True, False, True, True, False, True, True, True, False, True],
      [0, 2, 1, 0, 1, 0, 0, 0, 1, 0, 1],
      74505835530428901598709612439134825027),
     ('Jason March',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144350#1',
      False,
      ['0', '2', '0', '1', '0', '2', '2', '0', '2', 'X'],
      '9',
      [False, False, False, False, False, True, False, False, True],
      [0, 2, 2, 3, 2, 4, 6, 3, 5],
      42581081463875970061015035008045933248),
     ('Sam Steep',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477&eventid=6400&teamid=144351&profileid=25978#1',
      True,
      ['0', '0', '0', '0', '1', '0', '0', '3', '0', 'X'],
      '4',
      [True, True, True, True, True, False, True, True, False],
      [0, -2, -2, -3, -2, -4, -6, -3, -5],
      42581081463875970061015035008045933248)]



```python
event.get_flat_boxscores()[-1]
```




    [('Tyler Stewart',
      'event.php?view=Team&eventid=6400&teamid=144352&profileid=12477#1',
      False,
      ['0', '0', '1', '1', '0', '3', '0', '0', '1', '0'],
      '6',
      [False, False, True, False, False, True, False, False, True, False],
      [0, -1, 0, 1, -2, 1, 1, 0, 1, -1],
      337656267050323493383665822966511297443),
     ('Matthew Hall',
      'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      True,
      ['0', '1', '0', '0', '3', '0', '0', '1', '0', '2'],
      '7',
      [True, True, False, True, True, False, True, True, False, True],
      [0, 1, 0, -1, 2, -1, -1, 0, -1, 1],
      337656267050323493383665822966511297443)]



## About czapi
czapi is a Python library for scraping curling linescores.
