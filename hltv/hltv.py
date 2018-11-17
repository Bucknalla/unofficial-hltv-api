#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from re import sub
from numpy import array
from bs4 import BeautifulSoup
from datetime import datetime

# Weapon name resolver & map resolver
weaponsRef = {"awp": "AWP","ak47": "AK47","m4a1_silencer": "M4A1-S","m4a1": "M4A4","deagle": "Desert Eagle","usp_silencer": "USP-S","p250": "P250","glock": "Glock-18","cz75a": "CZ-75 Auto","ump45": "UMP-45","ssg08": "SSG-08","famas": "FAMAS","hkp2000": "P2000","mp7": "MP7","galilar": "Galil-AR","fiveseven": "Five-Seven","tec9": "Tec-9","hegrenade": "HE Grenade","mac10": "MAC-10","mp9": "MP9","mag7": "MAG7","inferno": "Molotov","p90": "P-90","knife_default_ct": "Default Knife","knife_karambit": "Karambit","knife_butterfly": "Butterfly Knife","knife_flip": "Flip Knife","xm1014": "XM1014","knife_t": "Default Knife","elite": "Dual Barettas","knife_m9_bayonet": "M9 Bayonet","usp_silencer_off": "USP-S (Unsilenced)","aug": "AUG","bayonet": "Bayonet","scar20": "SCAR-20","world": "Suicide","knife_push": "Shadow Daggers","sawedoff": "Sawed Off","nova": "Nova","bizon": "PP-Bizon","taser": "Zeus X27","sg556": "SG-553","knife": "Knife","knife_gut": "Gut Knife","knife_survival_bowie": "Bowie Knife","knife_falchion": "Falchion Knife","negev": "Negev","knife_tactical": "Huntsman Knife","revolver": "R8 Revolver","gallil": "Galil","mp5sd": "MP5-SD","g3sg1": "G3SG1"}
mapResolver = {"d2": "Dust 2", "cch": "Cache", "ovp": "Overpass", "mrg": "Mirage", "nuke": "Nuke", "inf": "Inferno", "trn": "Train", "cbl": "Cobblestone", "bo1": "bo1", "bo3": "bo3", "bo5": "bo5"}

#Fakes header otherwise 403 & Formats Request w/ URL & Fake Headers Otherwise Denied & Decodes Response as Usually contains unicode characters  & Loads Beautiful Soup & Returns
webWorker = lambda teamLink: BeautifulSoup(urllib.request.urlopen(urllib.request.Request(teamLink, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})).read().decode("utf-8"), 'html.parser') # Loads data in BS

def getId(teamRequest):
    try:
        int(teamRequest) == int(teamRequest)
        return teamRequest
    except ValueError:
        raise ValueError("Unknown ID Reference, use a number.")

def matchIdResolver(matchRequest):
    if (matchRequest[0:4] == "http"):
        return matchRequest
    else:
        try:
            int(matchRequest) == int(matchRequest)
            return "https://www.hltv.org/matches/" + matchRequest + "/bots"

        except ValueError:
            raise ValueError("Invalid Match Id Type")

class teams():

    def roster(self, teamRequest, complex=False):
        teamId = getId(teamRequest)
        
        if (complex):
            data = {"roster": {"player0": {},"player1": {},"player2": {},"player3": {},"player4": {}},"wdl": {}}

            # Have to find the player IDs before this can be used
            playerIds = [i.get("href").split("/")[2] for i in webWorker("https://www.hltv.org/team/" + teamId + "/bot").find("div", {"class": "bodyshot-team"}).findAll("a")]

            try:
                bsData = webWorker("https://www.hltv.org/stats/lineup?lineup=" + playerIds[0] + "&lineup=" + playerIds[1] + "&lineup=" + playerIds[2] + "&lineup=" + playerIds[3] + "&lineup=" + playerIds[4] + "&minLineupMatch=5")
            except IndexError:
                raise ValueError("Unable to get team data on request.")

            bsData0 = bsData.findAll("div", {"class": "teammate-info standard-box"})
            bsData1 = bsData.findAll("img") # Ugly but works very well

            for i in range(len(bsData0)):

                data["roster"]["player" + str(i)]["alias"] = bsData0[i].find("div", {"class": "text-ellipsis"}).text # Player Alias
                data["roster"]["player" + str(i)]["country"] = bsData0[i].find("img").get("title") # Contains Country Name
                data["roster"]["player" + str(i)]["id"] = playerIds[i] # Simple Called from Reference
                data["roster"]["player" + str(i)]["maps_played"] = list(filter(None, ('').join(list(filter(None, bsData0[i].text.split(" ")))).split("\n")))[2][:-4] # Gets Text -> Removes Escape Characters & Spaces -> Into Array -> Gets Map Data from Array -> Leaves only map played number
                data["roster"]["player" + str(i)]["picture"] = bsData1[3 + (i * 2)].get("src") # Players Images @ 3, 5, 7, 9, 11
                data["roster"]["player" + str(i)]["real_name"] = bsData1[3 + (i * 2)].get("alt").split("'")[0] + bsData1[3 + (i * 2)].get("alt").split("'")[-1][1:] # Gets Alt Which is First Name 'Alias' Last Name -> Splits to Array -> Places Together First and Last name -> Removes any addition spaces

            data["maps_played"] = bsData.findAll("div", {"class": "columns"})[0].findAll("div", {"class": "large-strong"})[0].text
            data["wdl"]["win"] = "".join(bsData.findAll("div", {"class": "columns"})[0].findAll("div", {"class": "large-strong"})[1].text.split()).split("/")[0]
            data["wdl"]["draw"] = "".join(bsData.findAll("div", {"class": "columns"})[0].findAll("div", {"class": "large-strong"})[1].text.split()).split("/")[1]
            data["wdl"]["loss"] = "".join(bsData.findAll("div", {"class": "columns"})[0].findAll("div", {"class": "large-strong"})[1].text.split()).split("/")[2]
            data["total_kills"] = bsData.findAll("div", {"class": "columns"})[0].findAll("div", {"class": "large-strong"})[2].text
            data["total_deaths"] = bsData.findAll("div", {"class": "columns"})[1].findAll("div", {"class": "large-strong"})[0].text
            data["rounds_played"] = bsData.findAll("div", {"class": "columns"})[1].findAll("div", {"class": "large-strong"})[1].text
            data["kdr"] = bsData.findAll("div", {"class": "columns"})[1].findAll("div", {"class": "large-strong"})[2].text

            return data


        else:

            data = {"roster": []}

            bsData = webWorker("https://www.hltv.org/team/" + teamId + "/bot") # Web Requests
            bsData = bsData.findAll('div', {"class": "bodyshot-team"}) # Locates Roster Information Section
            
            bsData = ('').join(list(filter(None, bsData[0].text.split(" ")))) # Their names have a trailing space when processed, this removes it
            data["roster"] = list(filter(None, bsData.split("\n"))) # Contains escape characters, removed and sorted into array

            return data

    def shortStats(self, teamRequest):
        # Ranking || Weeks in Top 30 || Location || Basic Roster
        bsData = webWorker("https://www.hltv.org/team/" + getId(teamRequest) + "/bot")
        data = {"ranking": self.ranking(teamRequest)["ranking"],"roster": self.roster(teamRequest, False)["roster"]}
        data["weeks_in_top_30"] = bsData.findAll("div", {"class": "profile-team-stat"})[1].text[23:]
        data["location"] = bsData.findAll("div", {"class": "team-country"})[0].text[1:]
        return data

    def longStats(self, teamRequest):

        shortStatsInc = self.shortStats(teamRequest)
        mapData = self.mapData(teamRequest)
        rosterStats = self.roster(teamRequest, True)
        bsData0 = webWorker("https://www.hltv.org/team/" + getId(teamRequest) + "/bot")

        return {"ranking": shortStatsInc["ranking"], "weeks_in_top_30": shortStatsInc["weeks_in_top_30"], "location": shortStatsInc["location"], "roster": self.roster(teamRequest, False)["roster"], "upcoming_matches": self.upcomingMatches(teamRequest), "recent_matches": self.recentResults(teamRequest), "peak": bsData0.findAll("span", {"class": "value"})[1].text[1:], "weeks_at_peak": bsData0.findAll("span", {"class": "value"})[2].text[:-5], "maps_played": rosterStats["maps_played"], "wdl": { "wins": rosterStats["wdl"]["win"], "draws": rosterStats["wdl"]["draw"], "loss": rosterStats["wdl"]["loss"]}, "total_kills": rosterStats["total_kills"], "total_deaths": rosterStats["total_deaths"], "maps": {"train": mapData["train"], "overpass": mapData["overpass"], "mirage": mapData["mirage"], "season": mapData["season"], "dust2": mapData["dust2"], "inferno": mapData["inferno"], "cobblestone": mapData["cobblestone"], "nuke": mapData["nuke"], "cache": mapData["cache"]}}

    def upcomingMatches(self, teamRequest):
        # Upcoming Matches Only
        bsData = webWorker("https://www.hltv.org/team/" + getId(teamRequest) + "/bot").findAll("div", {"class": "standard-box upcoming-match"})
        data = [{"date": list(filter(None, bsData[i].text.split("\n")))[0], "match": list(filter(None, bsData[i].text.split("\n")))[1] + " " + list(filter(None, bsData[i].text.split("\n")))[2] + " " + list(filter(None, bsData[i].text.split("\n")))[3], "tournament": list(filter(None, bsData[i].text.split("\n")))[4]} for i in range(len(bsData))]

        return data

    def recentResults(self, teamRequest):
        # Quick Recent Matches

        bsData = webWorker("https://www.hltv.org/team/" + getId(teamRequest) + "/bot")
        bsData0 = bsData.findAll("div", {"class": "standard-box result result-won"})
        bsData1 = bsData.findAll("div", {"class": "standard-box result result-lost"})

        # Essentially Comes in two section, wins and losses, same method for both, finds them all, parses and combines array
        data = [{"score": list(filter(None, bsData0[i].text.split("\n")))[0], "match": list(filter(None, bsData0[i].text.split("\n")))[1] + " " + list(filter(None, bsData0[i].text.split("\n")))[2] + " " + list(filter(None, bsData0[i].text.split("\n")))[3], "tournament": list(filter(None, bsData0[i].text.split("\n")))[4], "status": "won"} for i in range(len(bsData0))] + [{"score": list(filter(None, bsData1[i].text.split("\n")))[0], "match": list(filter(None, bsData1[i].text.split("\n")))[1] + " " + list(filter(None, bsData1[i].text.split("\n")))[2] + " " + list(filter(None, bsData1[i].text.split("\n")))[3], "tournament": list(filter(None, bsData1[i].text.split("\n")))[4], "status": "loss"} for i in range(len(bsData1))]

        return data

    def mapData(self, teamRequest):
        # Map Stats: https://www.hltv.org/stats/teams/maps/6665/Astralis
        
        data = {}

        bsData = webWorker("https://www.hltv.org/stats/teams/maps/" + getId(teamRequest) + "/bot").findAll("div", {"class", "map-pool-map-name"})

        # Can't really be sorted
        for mapIndex in range(int(len(bsData) / 2)):
            data[bsData[mapIndex].text.split("-")[0][:-1].lower()] = bsData[mapIndex].text.split("-")[1][:-1][1:]
        
        return data

    def matchHistory(self, teamRequest, requestLimit=None):
        # Match History: https://www.hltv.org/stats/teams/matches/6665/Astralis
        bsData = list(filter(None, webWorker("https://www.hltv.org/stats/teams/matches/" + getId(teamRequest) + "/bot").findAll("table", {"class": "stats-table no-sort"})[0].text.split("\n")))[6:]

        if (requestLimit is None):

            data = [{"date": bsData[0::7][i], "event": bsData[1::7][i], "opponent": bsData[3::7][i], "map": bsData[4::7][i], "score": bsData[5::7][i], "result": {"W": "victory", "L": "loss", "T": "draw"}[bsData[6::7][i]]} for i in range(int(len(bsData) / 7))]

        else:

            if (requestLimit > len(bsData) / 7):
                requestLimit = len(bsData) / 7

            data = [{"date": bsData[0::7][i], "event": bsData[1::7][i], "opponent": bsData[3::7][i], "map": bsData[4::7][i], "score": bsData[5::7][i], "result": {"W": "victory", "L": "loss", "T": "draw"}[bsData[6::7][i]]} for i in range(requestLimit)]

        return data

    ranking = lambda teamRequest: {"ranking": str(webWorker("https://www.hltv.org/team/" + getId(teamRequest) + "/bot").findAll('div', {"class": "profile-team-stat"})[0].find("a").text[-1:])} # Finds relevant data

    bigAchivements = lambda teamRequest: [{"event": achivement.text.split("at")[1], "ranking": achivement.text.split("at")[0][:-1]} for achivement in webWorker("https://www.hltv.org/team/" + getId(teamRequest) + "/bot").findAll("div", {"class": "cell text-ellipsis achievement "})]

class player():

    def profile(self, playerRequest):

        bsData = webWorker("https://www.hltv.org/player/" + getId(playerRequest) + "/bot")

        return {"alias": bsData.find("div", {"class": "player-nick text-ellipsis"}).text, "real_name": bsData.find("div", {"class": "player-realname"}).text, "hltv_id": getId(playerRequest), "country": bsData.find("img", {"class": "flag"}).get("alt"), "profile_picture": bsData.find("img", {"class": "bodyshot-img"}).get("src"), "age": sub("[^0-9]", "", bsData.find("span", {"class": "profile-player-stat-value"}).text), "current_team": bsData.find("img", {"class": "profile-player-stat-team-logo"}).get("alt"), "top_20": [{"year": "20" + sub("[^0-9]", "", ranking.split("(")[1]),"ranking": sub("[^0-9]", "", ranking.split("(")[0])} for ranking in bsData.find("span", {"class": "profile-player-stat-value right"}).text.split(",")], "achivements": player.achivements(playerRequest)}

    def stats(self, playerRequest, _complex=False, filterMatch=None, timeFilter=None, rankingFilter=None):
        
        if (_complex):
            # https://www.hltv.org/stats/players/ id /bot
            customRequestString = "https://www.hltv.org/stats/players/" + getId(playerRequest) + "/bot"
            useChar = "?" # Uses for manipulating PHP $_GET requests
            if (filterMatch is not None):
                customRequestString += useChar + "matchType=" + filterMatch
                useChar = '&'
            if (timeFilter is not None):
                customRequestString += useChar + "startDate=" + timeFilter[0] + "&endDate=" + timeFilter[1]
                useChar = '&'
            if (rankingFilter is not None):
                customRequestString += useChar + "rankingFilter=Top" + rankingFilter

            stats = [sub("[^0-9.]", "", stat.text) for stat in webWorker("https://www.hltv.org/stats/players/" + getId(playerRequest) + "/bot").findAll("div", {"class": "stats-row"})] # Essentially sorts the data, removes unneeded text etc.
            return {"kills_per_round": stats[7], "headshot": stats[1], "deaths_per_round": stats[10], "total_kills": stats[0], "total_deaths": stats[2], "kdr": stats[3], "adr": stats[4], "grenade_adr": stats[5], "rounds_played": stats[6], "assists_per_round": stats[9], "deaths_round": stats[10], "saved_by_teammate_per_round": stats[11], "saved_teammates_per_round": stats[12], "rating_1": stats[13][3:]}

        else:

            # Basic Data
            bsData = webWorker("https://www.hltv.org/player/" + getId(playerRequest) + "/bot").findAll("span", {"class": "statsVal"})
            return {"rating_2": bsData[0].text, "kills_per_round": bsData[1].text, "headshot": bsData[2].text[:-1], "maps_played": bsData[3].text, "deaths_per_round": bsData[4].text, "rounds_contributed": bsData[5].text[:-1],}

    def clutches(self, usp_silencer_off, playerRequest, getStats=False, clutchType="1", getDetails=False, detailsLimit=None):
        
        if (getStats == False and getDetails == False):
            # Asking for no data essentially
            return None

        else:
            # Looks like the data function could be compressed more but the statements aren't mutually exclusive
            bsData, data = webWorker("https://www.hltv.org/stats/players/clutches/" + getId(playerRequest) + "/1on" + clutchType + "/bot"), {}

            if (getStats):

                if (clutchType == "1"):
                    # Slightly More Complex Data
                    data["losses"] = (sub("[^0-9]", "", bsData.findAll("div", {"class": "summary-box standard-box "})[0].text))
                    data["difference"] = (sub("[^0-9+-]", "", bsData.findAll("div", {"class": "summary-box standard-box "})[1].text))

                    if (data["difference"][0] == "+"):
                        data["wins"] = str(int(data["losses"]) + int(data["difference"][1:]))
                    else:
                        data["wins"] = str(int(data["losses"]) - int(data["difference"][1:]))

                else:
                    # Less complicated
                    data["wins"] = bsData.find("div", {"class": "summary-box standard-box"}).find("div", {"class": "value"}).text

            if (getDetails):

                detailsData, clutchHistory = [], []
                detailsData = [list(filter(None, i.text.split("\n"))) for i in bsData.findAll("tr")][1:]

                for i in detailsData:
                    i.pop(3)
                    i.append(sub("[^0-9]", "", i[1]) + " - " + sub("[^0-9]", "", i[2]))
                    i[1] = i[1].split("(")[0][:-1]
                    i[2] = i[2].split("(")[0][:-1]

                if (detailsLimit is None):
                    clutchHistory = [{"date": detailsData[i][0], "team_one": detailsData[i][1], "team_two": detailsData[i][2], "map": detailsData[i][3], "status": detailsData[i][4], "round": detailsData[i][5], "score": detailsData[i][6]} for i in range(len(detailsData))] 

                else:

                    if detailsLimit > len(detailsData):
                        detailsLimit = len(detailsData)

                    clutchHistory = {"history": [{"date": detailsData[i][0], "team_one": detailsData[i][1], "team_two": detailsData[i][2], "map": detailsData[i][3], "status": detailsData[i][4], "round": detailsData[i][5], "score": detailsData[i][6]} for i in range(detailsLimit)]}

                data["history"] = clutchHistory

            return data

    def individual(self, playerRequest):
        
        bsData = webWorker("https://www.hltv.org/stats/players/individual/" + getId(playerRequest) + "/bot").findAll("div", {"class": "stats-row"})
        return {"kills": bsData[0].text[5:], "deaths": bsData[1].text[6:], "kdr": bsData[2].text[12:], "kpr": bsData[3].text[12:], "rounds_with_kills": bsData[4].text[17:], "kd_diff": bsData[5].text[33:], "opening_kills": bsData[6].text[19:], "opening_deaths": bsData[7].text[20:], "opening_kdr": bsData[8].text[18:], "opening_kill_rating": bsData[9].text[19:], "team_win_percent_after_first_kill": bsData[10].text[33:][:-1], "first_kill_in_won_rounds": bsData[11].text[24:][:-1], "0_kill_rounds": bsData[12].text[13:], "1_kill_rounds": bsData[13].text[13:], "2_kill_rounds": bsData[14].text[13:], "3_kill_rounds": bsData[15].text[13:], "4_kill_rounds": bsData[16].text[13:], "5_kill_rounds": bsData[17].text[13:], "rifle_kills": bsData[18].text[11:], "sniper_kills": bsData[19].text[12:], "smg_kills": bsData[20].text[9:], "pistol_kills": bsData[21].text[12:], "grenade_kills": bsData[22].text[7:], "other_kills": bsData[23].text[5:]}

    def matches(self, playerRequest, Limit=None):

        bsData = [list(filter(None, i.text.split("\n"))) for i in webWorker("https://www.hltv.org/stats/players/matches/" + getId(playerRequest) + "/bot").findAll("tr")][1:]

        for item in bsData:
            item.append(item[1].split("(")[1][:-1] + " - " + item[2].split("(")[1][:-1])
            item[1] = item[1].split("(")[0][:-1]
            item[2] = item[2].split("(")[0][:-1]
            item[3] = mapResolver[item[3]]

        if (Limit is None):

            return [{"date": bsData[i][0], "team_one": bsData[i][1], "team_two": bsData[i][2], "map": bsData[i][3], "kd": bsData[i][4], "kd_diff": bsData[i][5], "rating": bsData[i][6], "score": bsData[i][7]} for i in range(len(bsData))]

        else:

            if (Limit > len(bsData)):
                Limit = len(bsData)

            return [{"date": bsData[i][0], "team_one": bsData[i][1], "team_two": bsData[i][2], "map": bsData[i][3], "kd": bsData[i][4], "kd_diff": bsData[i][5], "rating": bsData[i][6], "score": bsData[i][7]} for i in range(Limit)]

    def weapons(self, playerRequest):

        data = {}

        dataList = [list(filter(None, i.text.split("\n"))) for i in webWorker("https://www.hltv.org/stats/players/weapon/" + getId(playerRequest) + "/bot").findAll("div", {"class": "stats-row"})]
        
        for i in dataList:
            i[0] = weaponsRef[i[0].split(".")[1][1:]]
            data[i[0]] = i[1]

        return data

    opponents = lambda playerRequest: [{"opponent": i[0], "maps_played": i[1], "kd_diff": i[2], "kdr": i[3], "rating_1": i[4]} for i in [list(filter(None, i.text.split("\n"))) for i in webWorker("https://www.hltv.org/stats/players/opponents/team/" + getId(playerRequest) + "/bot").find("table", {"class": "stats-table player-ratings-table sortable-table"}).findAll("tr")][1:]]

    achivements = lambda playerRequest: [trophy.get("title") for trophy in webWorker("https://www.hltv.org/player/" + getId(playerRequest) + "/bot").findAll("span", {"class": "trophyDescription"})]

class hltv(object):
    def __init__(self, matchID):
        self.bsData_events = webWorker("https://www.hltv.org/events")
        self.bsData_teams = webWorker("https://www.hltv.org/ranking/teams/") 

    def rankings(self, searchSpecific=False, customYear=datetime.now().year, customMonth=datetime.now().strftime("%B").lower(), customDay=datetime.now().day):
    # Slightly more complex, as the link is dynamic hence it is only updated live from the main site.
        if (customYear == datetime.now().year and customMonth == datetime.now().strftime("%B").lower() and customDay == datetime.now().day):
            # Latest date
            bsData = webWorker("https://www.hltv.org/ranking/teams/")            
        else:
            bsData = webWorker("https://www.hltv.org/ranking/teams/" + str(customYear) + "/" + str(customMonth) + "/" + str(customDay))

        data = [{"ranking": teamData[0][1:], "points": sub("[^0-9]", "", teamData[1].split("(")[1]), "team": teamData[1].split("(")[0],"roster": teamData[2:][:-1],"recent_change": teamData[-1]} for teamData in [list(filter(None, i.text.split("\n"))) for i in [i.find("div", {"class": "bg-holder"}).find("div", {"class": "ranking-header"}) for i in bsData.findAll("div", {"class": "ranked-team standard-box"})]]]
        datetime.now()
        if (searchSpecific):
            return data[searchSpecific-1]

        else:
            return data
    
    def query(self, query):
            
            data, references = {}, ["players", "teams", "events"]
            bsData = webWorker("https://www.hltv.org/search?query=" + query).findAll("table", {"class": "table"})

            for i in range(3):
                data[references[i]] = [{references[i][:-1]: list(filter(None, bsData[i].text.split("\n")))[1:][j], "hltv_id": [i.get("href").split("/")[-2] for i in bsData[i].findAll("a")][j]} for j in range(len(list(filter(None, bsData[i].text.split("\n")))[1:]))]

            topics = [list(filter(None, bsData[3].text.split("\n")))[3:][i*3:i*3+3] for i in range(int(len(list(filter(None, bsData[3].text.split("\n")))[3:]) / 3))]

            data["topics"] = [{"topic": topics[i][0],"date": topics[i][1], "forum": topics[i][2], "event_id": [i.get("href").split("/")[-2] for i in bsData[3].findAll("a")][i]} for i in range(len(topics))]
            return data

    events = lambda: [{"event": event[0], "dates": event[1]} for event in [list(filter(None, i.text.split("\n"))) for i in webWorker("https://www.hltv.org/events").findAll("div", {"class": "content standard-box"})]]

    upcomingMatches = lambda: [{"time": matchDetails[0][0], "match": (' ').join(matchDetails[0][1:4]), "event": matchDetails[0][4], "map": mapResolver[matchDetails[0][5]], "match_id":matchDetails[1].split("/")[2], "match_url":("https://www.hltv.org"+matchDetails[1])} for matchDetails in [(list(filter(None, i.text.split("\n"))), i["href"]) for i in webWorker("https://www.hltv.org/matches").find("div", {"class": "match-day"}).findAll("a", {"class": "a-reset block upcoming-match standard-box"}, href=True)]]
    
    todaysResults = lambda: [{"team_one": match[0], "team_two": match[2], "score": match[1], "tournament": match[3], "map": mapResolver[match[4]]} for match in [list(filter(None, i.text.split("\n"))) for i in webWorker("https://www.hltv.org/results?content=vod").find("div", {"class": "results-sublist"}).findAll("div", {"class": "result"})]]

class match(object):
    def __init__(self, matchID):
        self.matchID = matchID
        self.bsData = webWorker(matchIdResolver(self.matchID))
        self.players = lambda : {"players": [(''.join(i)) for i in list(filter(None, [list(filter(None, i.text.split("\n"))) for i in self.bsData.findAll("td", {"class": "player"})]))]}
        self.maps = lambda : [i.text for i in self.bsData.findAll("div", {"class": "mapname"})]
        pass

    def teams(self):
        team_1 = self.bsData.find("div", {"class": "standard-box teamsBox"}).find("div", {"class": "team1-gradient"}).find("div", {"class": "teamName"}).text
        team_1_id = self.bsData.find("div", {"class": "standard-box teamsBox"}).find("div", {"class": "team1-gradient"}).find("a")["href"].split('/')[2]
        team_2 = self.bsData.find("div", {"class": "standard-box teamsBox"}).find("div", {"class": "team2-gradient"}).find("div", {"class": "teamName"}).text
        team_2_id = self.bsData.find("div", {"class": "standard-box teamsBox"}).find("div", {"class": "team2-gradient"}).find("a")["href"].split('/')[2]
        return {"team_1":(team_1,team_1_id),"team_2":(team_2, team_2_id)}

    def odds(self):
        bet_table = self.bsData.find("div", {"class": "betting standard-box"})
        bets = bet_table.findAll("tr", {"class": "betting_provider"})
        bet_list = []
        for index, _ in enumerate(bets):    
            classes = bets[index].get("class")
            if (any("geoprovider" in string for string in classes) and not "hidden" in classes):
                if not "night" in classes:
                    odds = bets[index].findAll("td", {"class" : "odds-cell border-left"})
                    odd_holder = []
                    for odd in odds:
                        if(odd.text is not None):
                            odd_holder.append(odd.text)
                    indices = int([i for i, s in enumerate(classes) if 'geoprovider' in s][0])
                    provider = classes[indices].split("_")[1]
                    if odd_holder:
                        bet_list.append((provider, odd_holder[0], odd_holder[2]))
        return(bet_list)

    def score(self):
        return {"winner_score": self.bsData.find("div", {"class": "won"}).text, "loser_score": self.bsData.find("div", {"class": "lost"}).text}

    def rewatch(self):
        bsData, data = self.bsData.findAll("div", {"class": "stream-box"}), {}
        if (bsData[0].find("a").get("href").split("/")[-1] is not None):
            
            data["gotvId"] = bsData[0].find("a").get("href").split("/")[-1]
            bsData = bsData[1:]

        data["watch"] = [{"link": i.get("data-stream-embed"), "broadcast_title": i.find("span", {"class": "spoiler"}).text, "broadcast_country": i.find("img", {"class": "stream-flag flag"}).get("alt")} for i in bsData]
        return data

    def veto(self, keepLineBreaks=False):
        if (keepLineBreaks):
            return {"veto_details": self.bsData.findAll("div", {"class": "standard-box veto-box"})[0].text, "veto": self.bsData.findAll("div", {"class": "standard-box veto-box"})[1].text}
        else:
            return {"veto_details": self.bsData.findAll("div", {"class": "standard-box veto-box"})[0].text.replace('\n',' '), "veto": self.bsData.findAll("div", {"class": "standard-box veto-box"})[1].text.replace('\n',' ')}

    def playerScores(self):
        # Declare All Initial Arrays
        references, referenceKeys = ["collective"] + ["map_" + str(i) for i in range(9)], [["players", "players"], ["kd", "kd text-center"], ["adr", "adr text-center "], ["kast", "kast text-center"], ["rating", "rating text-center"]]
        workingData, prettyData, moreData = {"players": [], "kd": [], "adr": [], "kast": [], "rating": []}, {"players": [], "kd": [], "kd_diff": [], "adr": [], "kast": [], "rating": []}, {"players": [], "kast": [], "kd": [], "kd_diff": [], "rating": []}
        bsData, data = self.bsData, {"collective": {"players": []}}
        
        for i in range(len(referenceKeys)):
            workingData[referenceKeys[i][0]] = [list(filter(None, i.text.split("\n"))) for i in bsData.findAll("td", {"class": referenceKeys[i][1]})]

        # It's like Data, Data, Data, Data, Data, Title, this removes the title
        for i in range(len(workingData["players"])):
            if (i % 6 != 0):
                moreData["players"].append({
                    "player": workingData["players"][i][1],
                    "real_name": workingData["players"][i][0].split("'")[0] + workingData["players"][i][0].split("'")[2][1:]
                    })

                moreData["kast"].append(workingData["kast"][i])
                moreData["kd"].append(workingData["kd"][i])
                moreData["rating"].append(workingData["rating"][i])

        # Formats it neatly
        for i in range(len(moreData["players"]) // 5):
            prettyData["players"].append( moreData["players"][i*5:(i*5) + 5])
            prettyData["kast"].append( moreData["kast"][i*5:(i*5) + 5])
            prettyData["kd"].append( moreData["kd"][i*5:(i*5) + 5])
            moreData["kd_diff"] = [eval(i) for i in array(moreData["kd"]).flat]
            prettyData["kd_diff"].append(moreData["kd_diff"][i*5:(i*5) + 5])
            prettyData["rating"].append( moreData["rating"][i*5:(i*5) + 5] )
            prettyData["adr"].append( workingData["adr"][i*5:(i*5) + 5] ) # Complicated but adds in groups of 5 elements esssentially


        # Need to quickly get the map data to piece together the map data
        maps = [i.text for i in bsData.findAll("div", {"class": "mapname"})] # Quicker than calling the function

        # Assumes Each Found Set of 10 Players Equates to a Map -> Iterate Through Players and Add
        for i in range( (len(prettyData)-1) //2 ):

            data["map_" + str(i)] = {"players": []}
            data["map_" + str(i)]["map_name"] = maps[i]

        # Processes and adds data in teams & players
        for i in range(len(data)):

            data[references[i]]["players"] = [{"real_name": prettyData["players"][(i*2) + j][k]["real_name"], "alias": prettyData["players"][(i*2) + j][k]["player"], "rating": ('').join(prettyData["rating"][(i*2) + j][k]), "kast": ('').join(prettyData["kast"][(i*2) + j][k]), "kd": ('').join(prettyData["kd"][(i*2) + j][k]), "kd_diff": prettyData["kd_diff"][(i*2) + j][k], "adr": ('').join(prettyData["adr"][(i*2) + j][k])} for k in range(5) for j in range(2)]

        return data
    
  