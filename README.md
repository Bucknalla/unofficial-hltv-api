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

#### Request Format 1

Request

`hltv.teams.roster(hltvTeamId)`

Responce

`{'roster': ['examplePlayer0', 'examplePlayer1', 'examplePlayer2', 'examplePlayer3', 'examplePlayer4']}`

#### Request Format 2

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

### Long Stats

### Upcoming Matches

### Recent Results

### Map Data

### Match History

### Team Ranking

### Big Achivements

## Player

### Player Profile

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
