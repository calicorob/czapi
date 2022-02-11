# Welcome to czapi
> A basic API for scraping curling boxscores off of the popular <a href='https://www.curlingzone.com'>CurlingZone</a> website. 


## Install

Not implemented yet :)

## How to use

```
import czapi.api as api

game_result_dict = api.get_full_boxscore(cz_game_id = 271145)
game_result_dict
```




    {'Wayne Tuck Jr.': {'href': 'event.php?view=Team&eventid=6400&teamid=144353&profileid=12486#1',
      'hammer': True,
      'score': ['0', '2', '0', '0', '0', '0', '1', '1', '1', '0'],
      'finalscore': '5',
      'date': 'Jan 17 - 19, 2020',
      'event': 'Ontario Tankard - Open Qualifier',
      'hash': '91877086316aa83ea479d50515bddaaac92bcb34e4f6611c3b893de32dd8c9fe'},
     'Matthew Hall': {'href': 'event.php?view=Team&eventid=6400&teamid=144347&profileid=12435#1',
      'hammer': False,
      'score': ['0', '0', '4', '0', '0', '1', '0', '0', '0', '2'],
      'finalscore': '7',
      'date': 'Jan 17 - 19, 2020',
      'event': 'Ontario Tankard - Open Qualifier',
      'hash': '91877086316aa83ea479d50515bddaaac92bcb34e4f6611c3b893de32dd8c9fe'}}



> Output above should match the results from [here](https://curlingzone.com/game.php?1=1&showgameid=271145#1).

## About czapi
czapi is a Python library for scraping curling linescores.
