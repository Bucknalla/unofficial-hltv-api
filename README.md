# Unofficial-HLTV-API
My custom 'API' for hltv.org, allows the module to be imported and used with parameters to get data from certain aspects of the site.

# Installation & Usage
<b>Install</b>

`pip3 install hltv`

<b>Usage</b>

`import hltv`

# Documentation

## Teams

Contains all functions related to team data, an example team page can be found <a href="https://www.hltv.org/team/4608/natus-vincere">here</a>.
This will be able to find all relevant data on that page and return in, the functions are listed and explained below.

------

### Roster

This will return the roster of the team requested, it can be used in a short form, giving simply the players or long form giving more complex data about the team.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

Complex Data:
- Not Required
- Given Second
- Default is Disabled
- Boolean variable to enable complex data

#### Request Format 1 of 2

Request

`hltv.teams.roster(hltvTeamId)`

Responce

`{'roster': ['examplePlayer0', 'examplePlayer1', 'examplePlayer2', 'examplePlayer3', 'examplePlayer4']}`

#### Request Format 2 of 2

Request

`hltv.teams.roster(hltvTeamId, True)`

Responce

`
{
    "kdr": "KDR",
    "maps_played": "MAPS_PLAYED",
    "roster": {
        "player0": {
            "alias": "NAME",
            "country": "COUNTRY",
            "id": "ID",
            "maps_played": "MAPS_PLAYED",
            "picture": "HTTP://IMAGE.JPG",
            "real_name": "REAL_NAME"
        },
        "player1": {
            "alias": "NAME",
            "country": "COUNTRY",
            "id": "ID",
            "maps_played": "MAPS_PLAYED",
            "picture": "HTTP://IMAGE.JPG",
            "real_name": "REAL_NAME"
        },
        "player2": {
            "alias": "NAME",
            "country": "COUNTRY",
            "id": "ID",
            "maps_played": "MAPS_PLAYED",
            "picture": "HTTP://IMAGE.JPG",
            "real_name": "REAL_NAME"
        },
        "player3": {
            "alias": "NAME",
            "country": "COUNTRY",
            "id": "ID",
            "maps_played": "MAPS_PLAYED",
            "picture": "HTTP://IMAGE.JPG",
            "real_name": "REAL_NAME"
        },
        "player4": {
            "alias": "NAME",
            "country": "COUNTRY",
            "id": "ID",
            "maps_played": "MAPS_PLAYED",
            "picture": "HTTP://IMAGE.JPG",
            "real_name": "REAL_NAME"
        },
    },
    "rounds_played": "RDS_PLAYED",
    "total_deaths": "TOTAL_DEATHS",
    "total_kills": "KILLS",
    "wdl": {
        "draw": "DRAWS",
        "loss": "LOSS",
        "win": "WIN"
    }
}
`

------

### Short Stats

Basic data, contains short but important information about the requested team, such as world ranking, weeks in the top 30 core, location and roster.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.teams.shortStats(hltvTeamId)`

Responce

`{'ranking': 'RANKING', 'weeks_in_top_30': 'WEEKS_IN_TOP_30', 'location': 'LOCATION_COUNTRY', 'roster': ['PLAYER', 'PLAYER', 'PLAYER', 'PLAYER', 'PLAYER']}`

----

### Long Stats

More complex stats and additional data about the team, it incorporates almost all team function into a single response, such as more complex roster data, rankings over time, collective team stats, as well as map data.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.teams.longStats("4608")`

Responce

`{'ranking': 'RANKING', 'weeks_in_top_30': 'WEEKS_IN_TOP_30', 'location': 'LOCATION_COUNTRY', 'roster': ['PLAYER', 'PLAYER', 'PLAYER', 'PLAYER', 'PLAYER'], 'upcoming_matches': [{'date': 'DD/MM', 'match': 'MATCH_TITLE', 'tournament': 'TOURNAMENT_NAME'}, MORE_HERE], 'recent_matches': [{'score': 'SCORE', 'match': 'MATCH TITLE', 'tournament': 'TOURNAMENT', 'status': 'W/D/L'}, MORE_HERE], 'peak': 'WORLD_RANKING_PEAK', 'weeks_at_peak': 'WEEKS_AT_PEAK', 'maps_played': 'MAPS_WITH_ROSTER', 'wdl': {'wins': 'WINS', 'draws': 'DRAWS', 'loss': 'LOSSES'}, 'total_kills': 'COLLECTIVE_KILLS', 'total_deaths': 'COLLECTIVE_DEATHS', 'maps': {'train': 'TRAIN_WIN_RATE', 'overpass': 'OVERPASS_WIN_RATE', 'mirage': 'MIRAGE_WIN_RATE', 'season': 'SEASON_WIN_RATE', 'dust2': 'DUST2_WIN_RATE', 'inferno': 'INFERNO_WIN_RATE', 'cobblestone': 'CBBL_WIN_RATE', 'nuke': 'NUKE_WIN_RATE', 'cache': 'CACHE_WIN_RATE'}}`

---

### Upcoming Matches

Returns an array with all upcoming matches listed on the team page of hltv.org from the requested team.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.teams.upcomingMatches(hltvTeamId)`

Response

`[{'date': 'DD/MM', 'match': 'MATCH_OFFICIAL_TITLE', 'tournament': 'TOURNAMENT_NAME'}, MORE_HERE]`

---

### Recent Results

Similar to Upcoming matches, however returns matches that the team has recently played, full match history is available on team ranking, however this is generally quicker to call if you only want a few recent matches.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.teams.recentResults(hltvTeamId)`

Response

`[{'score': 'FINAL_SCORE', 'match': 'MATCH_TITLE', 'tournament': 'TOURNAMENT_NAME', 'status': 'W/D/L'}, MORE_HERE]`

---

### Map Data

This will simply return each map in the mappool & maps the team has played before and give their win percentage on them, this can be useful to see how good a team is on a map or make prediction etc.
At the moment it supports no time period however in future it may.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

#### Request Format 1 of 1

Request
` hltv.teams.mapData(hltvTeamId)`

Response
`{'train': 'TRAIN_WIN_PERCENT', 'overpass': 'OVERPASS_WIN_PERCENT', 'mirage': 'MIRAGE_WIN_PERCENT', 'season': 'SEASON_WIN_PERCENT', 'dust2': 'D2_WIN_PERCENT', 'inferno': 'INFERNO_WIN_PERCENT', 'cobblestone': 'CBBL_WIN_PERCENT', 'nuke': 'NUKE_WIN_PERCENT', 'cache': 'CACHE_WIN_PERCENT'}`

---

### Match History

This can return the complete match history of a team, this process can return an extremly large amount of data, hence an additional parameter is given to limit the size of the response, by default however it is disabled.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

Reponse Limit:
- Not Required
- Given Second
- Default is None / Disabled
- Int variable used to limit size of response

#### Request Format 1 of 2

Request

`hltv.teams.matchHistory(HltvTeamId)`

Responce

`[{'date': 'DD/MM/YY', 'event': 'EVENT_TITLE', 'opponent': 'OPPONENT_NAME', 'map': 'MAP_FULL_NAME', 'score': 'SCORE', 'result': 'W/D/L'}, This goes on for a while, depends age of team of course]`

#### Request Format 1 of 2

Request

`hltv.teams.matchHistory(HltvTeamId, 5)`

Responce

`[{'date': 'DD/MM/YY', 'event': 'EVENT_TITLE', 'opponent': 'OPPONENT_NAME', 'map': 'MAP_FULL_NAME', 'score': 'SCORE', 'result': 'W/D/L'}, This goes on for 5 times per the request]`

---

### Team Ranking

Very simply returns the teams global ranking as of the time of the request, aquired from the latest possible hltv rankings.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.teams.ranking(hltvTeamId)`

Response

`{'ranking': 'TEAM_RANKING'}`

---

### Big Achivements

This shows all HLTV listed big achivements for a team, which is normally the event and their ranking, this is returned as a list.

#### Parameters

Team Requested:
- Required
- Giving First
- No Default
- HLTV Team ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.teams.bigAchivements(hltvTeamId)`

Response

`[{'event': ' EVENT_NAME', 'ranking': 'RANKING'}, And So On]`

---

## Player

This section will contain all stats related to individual stats and performances of a requested player, such as their general information, simple statistics, clutches, weapon usage, performance against different opposition and personal achivements such as event MVPs.

### Player Profile

This contains all short stats about a player from their profile, such as country, real name, team and times in the hltv top 20 rankings.

#### Parameters

Player Requested:
- Required
- Giving First
- No Default
- HLTV Player ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.player.profile(hltvPlayerId)`

Response

`{'alias': 'ALIAS', 'real_name': ' 'REAL_NAME', 'hltv_id': 'HLTV_ID', 'country': 'COUNTRY', 'profile_picture': 'HTTP://IMAGE.JPG', 'age': 'AGE_YEARS', 'current_team': 'CURRENT_TEAM', 'top_20': [{'year': 'YEAR', 'ranking': 'RANKING'}], 'achivements': ['EVENT_NAME_ACHIVEMENT_DETAILS_HERE']}`

---

### Stats

### Clutches

### Individual Stats

### Career Matches

### Weapon Usage

### Opponents

### Achivements

## Hltv

### Global Rankings

### Query

### Events

### Upcoming Matches Today

### Todays Played Matches Results

## Match

### Score

### Rewatch

### Veto

### Player Scores

### Players in Match

### Maps
