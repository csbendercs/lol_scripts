from riotwatcher import *
import json
import requests
import pandas as pd
region = "na1"
key = "RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"
summoner = "booboow"
#summoner info
url_sumi = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/"+ summoner +"?api_key=" + key
url_champ = "https://na1.api.riotgames.com/lol/static-data/v3/champions?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"

url_recent = "https://na.api.riotgames.com/api/lol/NA/v1.3/game/by-summoner/22700629/recent?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"

url_item = "https://na1.api.riotgames.com/lol/static-data/v3/items?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"

url_chalLeague = "https://na1.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"



response = requests.get(url_chalLeague)

#response2 = requests.get(url_sumi)
data1 = response.json()

playerNameList = []
playerIdList = []
leaguePointsList = []
winsList = []
lossList = []


for x in range(0, 10):
    playerNameList.append(data1["entries"][x]["playerOrTeamName"])
    playerIdList.append(data1["entries"][x]["playerOrTeamId"])
    leaguePointsList.append(data1["entries"][x]["leaguePoints"])
    winsList.append(data1["entries"][x]["wins"])
    lossList.append(data1["entries"][x]["losses"])



print(playerNameList)
print(leaguePointsList)
#print(data2)

#from app.models import *
#Model.objects.create()

#print(test1.head(), index = [])

#print(data1["games"][0]["gameId"])

#print(len(data1["games"]))
#print(json.dumps(data1,indent = 4))