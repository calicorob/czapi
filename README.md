# Welcome to czapi
> A basic API for scraping curling boxscores off of the popular <a href='https://www.curlingzone.com'>CurlingZone</a> website. 


## Install

Not implemented yet :)

## How to use

```python
import czapi.api as api

game_result_dict = api.get_boxscore_from_game_id(cz_game_id = 271145)
game_result_dict
```




    defaultdict(list,
                {'Wayne Tuck Jr.': defaultdict(list,
                             {'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
                              'hammer': True,
                              'score': ['0',
                               '2',
                               '0',
                               '0',
                               '0',
                               '0',
                               '1',
                               '1',
                               '1',
                               '0'],
                              'finalscore': '5'}),
                 'Matthew Hall': defaultdict(list,
                             {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
                              'hammer': False,
                              'score': ['0',
                               '0',
                               '4',
                               '0',
                               '0',
                               '1',
                               '0',
                               '0',
                               '0',
                               '2'],
                              'finalscore': '7'})})



> Output above should match the results from [here](https://curlingzone.com/game.php?1=1&showgameid=271145#1).

## About czapi
czapi is a Python library for scraping curling linescores.
