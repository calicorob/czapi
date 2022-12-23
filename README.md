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

```python
linescore_page = api.LinescorePage(cz_event_id = 5000, cz_draw_id = 1)

linescore_page.boxscores
```




    [defaultdict(list,
                 {'Rob Retchless': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114936&profileid=9625#1',
                               'hammer': True,
                               'score': ['2', '0', '0', '0', 'X', '', '', ''],
                               'finalscore': '2'}),
                  'Jordan Chandler': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114942&profileid=9627#1',
                               'hammer': False,
                               'score': ['0', '1', '3', '3', 'X', '', '', ''],
                               'finalscore': '7'})}),
     defaultdict(list,
                 {'Charlie Robert': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114939&profileid=10028#1',
                               'hammer': True,
                               'score': ['1', '0', '0', '0', '1', 'X', 'X', ''],
                               'finalscore': '2'}),
                  'Brent Ross': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114949&profileid=9887#1',
                               'hammer': False,
                               'score': ['0', '2', '1', '1', '0', 'X', 'X', ''],
                               'finalscore': '4'})}),
     defaultdict(list,
                 {'John Willsey': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114940&profileid=9707#1',
                               'hammer': False,
                               'score': ['0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '3',
                                '0',
                                '1',
                                'X'],
                               'finalscore': '5'}),
                  'ShopWoodstock.com': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114952&profileid=9703#1',
                               'hammer': True,
                               'score': ['0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                'X'],
                               'finalscore': '2'})}),
     defaultdict(list,
                 {'Wayne Tuck Jr.': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114937&profileid=9716#1',
                               'hammer': False,
                               'score': ['0', '0', '2', '2', '0', '0', '2', 'X'],
                               'finalscore': '6'}),
                  'Charlie Richard': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114958#1',
                               'hammer': True,
                               'score': ['0', '2', '0', '0', '0', '2', '0', 'X'],
                               'finalscore': '4'})}),
     defaultdict(list,
                 {'Connor Duhaime': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114946&profileid=9629#1',
                               'hammer': False,
                               'score': ['0', '0', '0', '0', 'X', '', '', ''],
                               'finalscore': '0'}),
                  'Daryl Shane': defaultdict(list,
                              {'href': 'event.php?view=Team&eventid=5000&teamid=114941&profileid=9762#1',
                               'hammer': True,
                               'score': ['1', '1', '3', '1', 'X', '', '', ''],
                               'finalscore': '6'})})]



## About czapi
czapi is a Python library for scraping curling linescores.
