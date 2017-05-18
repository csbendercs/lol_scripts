import requests
from optItem.models import *

url_chalLeague = "https://na1.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=RGAPI-c393b0ed-c0d2-4968-b03e-dd4c93ea6164"
response = requests.get(url_chalLeague)

data1 = response.json()
playerNameList = []
playerIdList = []
leaguePointsList = []
winsList = []
lossList = []

playerName = ""
playerId = ""
leaguePoints = ""
wins = ""
loss = ""


for x in range(0, len(data1["entries"])):
    playerNameList.append(data1["entries"][x]["playerOrTeamName"])
    playerIdList.append(data1["entries"][x]["playerOrTeamId"])
    leaguePointsList.append(data1["entries"][x]["leaguePoints"])
    winsList.append(data1["entries"][x]["wins"])
    lossList.append(data1["entries"][x]["losses"])

for x in range(0, len(data1["entries"])):
    playerName = playerNameList[x]
    playerId = playerIdList[x]
    leaguePoints = leaguePointsList[x]
    wins = winsList[x]
    loss = lossList[x]

    temp = Summoner(sumid = playerId, name = playerName, rankPos = leaguePoints,)
    temp.save()



