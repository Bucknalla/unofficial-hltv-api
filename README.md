# Unofficial-HLTV-API
My custom 'API' for hltv.org, allows the module to be imported and used with parameters to get data from certain aspects of the site.
This is still a work in progress with a few minor features not included, with bad requests the module will error and these should be caught, it will not raise custom exceptions at the moment partially to keep it compact, as well as complete match stats only works for bo3s and maybe higher at the moment, this will be fixed in a future release.

# Todo
- Option to have percentage breakdowns on player weapon usage.
- Fix player stats for a post match threads.

# Installation & Usage
<b>Install</b>

`pip3 install hltv`

<b>Usage</b>

`import hltv`

# Documentation

Still a work in progress.

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

---

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

All of a players careers stats over a time period or all time, can be modified on request with a lot of options for different analysis.

Player Requested:
- Required
- Giving First
- No Default
- HLTV Player ID Request, Integer given as string

Use Complex Stas:
- Not Required, Unless Using Filter Match, Time Filter or Ranking Filter
- Second
- Default is False
- Boolean, determins to return complex stats or not

Filter Match:
- Not Required
- Third
- Default is None
- String determins what to select matches by, options are 'Lan', 'Online', 'BigEvents', 'Majors'

Time Filter:
- Not Required
- Fourth
- Default is None
- String determines the time period to sort by, give a start date and a end date in a array

Ranking Filter:
- Not Required
- Fifth
- Default is None
- Determines the ranking of opposition

#### Request Format 1 of 5

Request

`hltv.player.stats(hltvPlayerId)`

Response

`{'rating_2': '0.99', 'kills_per_round': '0.63', 'headshot': '48.0', 'maps_played': '34', 'deaths_per_round': '0.66', 'rounds_contributed': '71.5'}`

#### Request Format 2 of 5

Request

`hltv.player.stats(hltvPlayerId, True)`

Response

`{'kills_per_round': 'KPR', 'headshot': 'HS%', 'deaths_per_round': 'DPR', 'total_kills': 'TOTAL_KILLS', 'total_deaths': 'TOTAL_DEATHS', 'kdr': 'KDR', 'adr': 'ADR', 'grenade_adr': 'NADE_ADR', 'rounds_played': 'ROUNDS_TOTAL', 'assists_per_round': 'APR', 'deaths_round': 'DPR', 'saved_by_teammate_per_round': 'SBTPR', 'saved_teammates_per_round': 'STPR', 'rating_1': 'RATING_1'}`

#### Request Format 3 of 5

Request

`hltv.player.stats(hltvPlayerId, True, Filter)`

Response

`{'kills_per_round': 'KPR', 'headshot': 'HS%', 'deaths_per_round': 'DPR', 'total_kills': 'TOTAL_KILLS', 'total_deaths': 'TOTAL_DEATHS', 'kdr': 'KDR', 'adr': 'ADR', 'grenade_adr': 'NADE_ADR', 'rounds_played': 'ROUNDS_TOTAL', 'assists_per_round': 'APR', 'deaths_round': 'DPR', 'saved_by_teammate_per_round': 'SBTPR', 'saved_teammates_per_round': 'STPR', 'rating_1': 'RATING_1'}`

#### Request Format 4 of 5


Request

`hltv.player.stats(hltvPlayerId, True, Filter, [Dates])`

Response

`{'kills_per_round': 'KPR', 'headshot': 'HS%', 'deaths_per_round': 'DPR', 'total_kills': 'TOTAL_KILLS', 'total_deaths': 'TOTAL_DEATHS', 'kdr': 'KDR', 'adr': 'ADR', 'grenade_adr': 'NADE_ADR', 'rounds_played': 'ROUNDS_TOTAL', 'assists_per_round': 'APR', 'deaths_round': 'DPR', 'saved_by_teammate_per_round': 'SBTPR', 'saved_teammates_per_round': 'STPR', 'rating_1': 'RATING_1'}`

#### Request Format 5 of 5


Request

`hltv.player.stats(hltvPlayerId, True, Filter, [Date], Ranking)`

Response

`{'kills_per_round': 'KPR', 'headshot': 'HS%', 'deaths_per_round': 'DPR', 'total_kills': 'TOTAL_KILLS', 'total_deaths': 'TOTAL_DEATHS', 'kdr': 'KDR', 'adr': 'ADR', 'grenade_adr': 'NADE_ADR', 'rounds_played': 'ROUNDS_TOTAL', 'assists_per_round': 'APR', 'deaths_round': 'DPR', 'saved_by_teammate_per_round': 'SBTPR', 'saved_teammates_per_round': 'STPR', 'rating_1': 'RATING_1'}`

---

### Clutches

Stats about a players clutching ability, such as win ratio in 1v1s, total differences, details on successful large clutches.

Player Requested:
- Required
- Giving First
- No Default
- HLTV Player ID Request, Integer given as string

Get Stats:
- Required if nothing else besides player ID
- Given Second
- False by Default
- Boolean value to see if the user wants stats detailed

Clutch Type:
- Required if nothing else besides player ID
- Given Third
- Default of 1v1
- can be set as a string number from 1v1 to 1v5

Get Details:
- Required if nothing else besides player ID
- Given Fourth
- Default of False
- Boolean, True or False to determine if details are desired

Details Limit: 
- Not Required
- Given Fifth
- Default of None
- Determins limit of details data to save time

#### Request Format 1 of 3

Request 

`hltv.player.clutches("7998", True, "1", True, None)`

Response

`{"losses": "LOSSES", "difference": "DIFFERENCE STARTS WITH +-", "wins": "WINS", "history": [{"date": "DD/MM YY", "team_one": "TEAM ONE", "team_two": "TEAM TWO", "map": "MAP FULL NAME", "status": "WON OR LOST", "round": "ROUND", "score": "FINAL SCORE"}, So on]`

#### Request Format 2 of 3

Request 

`hltv.player.clutches("7998", False, "1", True, None)`

Response

`{"history": [{"date": "DD/MM YY", "team_one": "TEAM ONE", "team_two": "TEAM TWO", "map": "MAP FULL NAME", "status": "WON OR LOST", "round": "ROUND", "score": "FINAL SCORE"}, So on]`

#### Request Format 3 of 3

Request 

`hltv.player.clutches("7998", True, "1", False, None)`

Response

`{"losses": "LOSSES", "difference": "DIFFERENCE STARTS WITH +-", "wins": "WINS"}`

---

### Individual Stats

Everything to do with a players individual stats over their respective career.

#### Parameters

Player Requested:
- Required
- Giving First
- No Default
- HLTV Player ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.player.individual(hltvPlayerId)`

Response

`{
    "0_kill_rounds": "0_KILL_ROUNDS",
    "1_kill_rounds": "1_KILL_ROUNDS",
    "2_kill_rounds": "2_KILL_ROUNDS",
    "3_kill_rounds": "3_KILL_ROUNDS",
    "4_kill_rounds": "4_KILL_ROUNDS",
    "5_kill_rounds": "ACES",
    "deaths": "TOTAL_DEATHS",
    "first_kill_in_won_rounds": "FIRST_KILL_PERCENT_IN_WON_ROUNDS",
    "grenade_kills": "HE_NADE_KILLS",
    "kd_diff": "KD DIFF",
    "kdr": "KDR",
    "kills": "TOTAL_KILLS",
    "kpr": "KILLS_PER_ROUND",
    "opening_deaths": "TIMES_DIED_FIRST",
    "opening_kdr": "KDR_IN_OPENINGS",
    "opening_kill_rating": "OPENING_KILL_RATING",
    "opening_kills": "OPENING_KILLS",
    "other_kills": "OTHER_KILLS",
    "pistol_kills": "PISTOL_KILLS",
    "rifle_kills": "RIFLE_KILLS",
    "rounds_with_kills": "ROUNDS_WITH_KILLS",
    "smg_kills": "SMG_KILLS",
    "sniper_kills": "SNIPER_KILLS",
    "team_win_percent_after_first_kill": "TEAM_WIN_PERCENT_AFTER_FIRST_KILL"
}`

---

### Career Matches

All of a players known matches over their entire career.


#### Parameters

Player Requested:
- Required
- Giving First
- No Default
- HLTV Player ID Request, Integer given as string

Match Stats:
- Not Required
- Given Second
- Default of False; disabled
- Determins whether or not to also include match stats from hltv in the response, Boolean

Limit Response
- Not Required
- Given Third
- Default of None
- Determins the limit of the amount of matches given, int or None type if disabled.

#### Request Format 1 of 1

Request

`hltv.player.matches(hltvPlayerID)`

Response

`[
    {
        "date": "DD/MM/YY",
        "kd": "KILLS - DEATHS",
        "kd_diff": "DIFFERENCE STARTS WITH +-",
        "map": "PRETTY NAME OF MAP",
        "rating": "RATING IF HAS ASTRIX AT END IT'S RATING 1.0 ELSE IT'S NOT",
        "score": "FINAL SCORE",
        "team_one": "TEAM ONE",
        "team_two": "TEAM TWO"
        },
        So on
]`

---

### Weapon Usage

Shows usage of a players weapons throughout their career, this is not in percentage but that should be easy enough to calculate for yourself, this returns the total kills with each weapon.

#### Parameters

Player Requested:
- Required
- Giving First
- No Default
- HLTV Player ID Request, Integer given as string

#### Request Format 1 of 1

Request

`hltv.player.weapons(hltvPlayerID)`

Response

`{
    "AK47": "KILLS",
    "AUG": "KILLS",
    "AWP": "KILLS",
    "Bayonet": "KILLS",
    "Bowie Knife": "KILLS",
    "Butterfly Knife": "KILLS",
    "CZ-75 Auto": "KILLS",
    "Default Knife": "KILLS",
    "Desert Eagle": "KILLS",
    "Dual Barettas": "KILLS",
    "FAMAS": "KILLS",
    "Falchion Knife": "KILLS",
    "Five-Seven": "KILLS",
    "Flip Knife": "KILLS",
    "G3SG1": "KILLS",
    "Galil": "KILLS",
    "Galil-AR": "KILLS",
    "Glock-18": "KILLS",
    "Gut Knife": "KILLS",
    "HE Grenade": "KILLS",
    "Huntsman Knife": "KILLS",
    "Karambit": "KILLS",
    "Knife": "KILLS",
    "M4A1-S": "KILLS",
    "M4A4": "KILLS",
    "M9 Bayonet": "KILLS",
    "MAC-10": "KILLS",
    "MAG7": "KILLS",
    "MP5-SD": "KILLS",
    "MP7": "KILLS",
    "MP9": "KILLS",
    "Molotov": "KILLS",
    "Negev": "KILLS",
    "Nova": "KILLS",
    "P-90": "KILLS",
    "P2000": "KILLS",
    "P250": "KILLS",
    "PP-Bizon": "KILLS",
    "R8 Revolver": "KILLS",
    "SCAR-20": "KILLS",
    "SG-553": "KILLS",
    "SSG-08": "KILLS",
    "Sawed Off": "KILLS",
    "Shadow Daggers": "KILLS",
    "Suicide": "KILLS",
    "Tec-9": "KILLS",
    "UMP-45": "KILLS",
    "USP-S": "893",
    "USP-S (Unsilenced)": "KILLS",
    "XM1014": "KILLS",
    "Zeus X27": "KILLS"
}
`

---

### Opponents

Shows all of a players individual stats versus every team they have played throughout their careers recorded on hltv.

### Achivements

Personal achivements of the player

## Hltv

All functions related exclusively to the hltv site, such as rankings custom site search, events, professional matches today and the results of matches played today.

### Global Rankings

Global ranking top 30.

### Query

The site has a custom search function, this will return everything related to the query and classify results.

### Events

Events listed on hltv, as active or up and coming.

### Upcoming Matches Today

Matches today that are yet to be played as of the time requesed.

### Todays Played Matches Results

Matches today that have already been played listed on the site.

## Match

Contains all functions related to scraping post match thread, such as final scores maps, vetoes, player scores and the roster of the two teams.

### Score

Final score, normal 16 - X in a bo1 or 2 - X in a bo3 for example.

### Rewatch

All rewatch links including GOTV and twitch if given and the nationality of those broadcasts, if it does not contain the GOTV or stream download it should not have it, to download the GOTV demo use the ID in the format: https://www.hltv.org/download/demo/DEMO_ID_HERE

### Veto

Contains all veto data given, can be kept with line breaks or not, if requested.

### Player Scores

All players information, scores and rating, at the moment will contain collective data and that of each map.

### Players in Match

List of all players participating in the match.

### Maps

All maps that have been played.
