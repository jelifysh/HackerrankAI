import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

dota = pd.read_csv('trainingdata.txt', header=None)

team1wins = dota[dota[10] == 1]
team1wins = team1wins.drop(columns=[5, 6, 7, 8, 9, 10])
team1wins = pd.DataFrame(team1wins.values.flatten())
charactersTeam1 = team1wins[0].value_counts()

team2wins = dota[dota[10] == 2]
team2wins = team2wins.drop(columns=[0, 1, 2, 3, 4, 10])
team2wins = pd.DataFrame(team2wins.values.flatten())
charactersTeam2 = team2wins[0].value_counts()

characterWins1 = pd.DataFrame(charactersTeam1)
characterWins2 = pd.DataFrame(charactersTeam2)
characterWins = pd.merge(characterWins1, characterWins2, left_index=True, right_index=True, how='outer' )
characterWins.rename(columns={'0_x':'Team_One','0_y':'Team_Two'}, inplace=True)
characterWins['Total'] = characterWins['Team_One'] + characterWins['Team_Two']

dota2 = dota.drop(columns=10)
dota2 = pd.DataFrame(dota2.values.flatten())
totalPlayedChar = dota2[0].value_counts()
totalPlayedChar = pd.DataFrame(totalPlayedChar)
characterWins = pd.merge(characterWins, totalPlayedChar, left_index=True, right_index=True, how='outer' )
characterWins['Win_Rate'] = characterWins['Total'] / characterWins[0]
characterWins.drop(columns=['Team_One','Team_Two','Total',0], inplace=True)
winRate = characterWins['Win_Rate'].to_dict()
dota[0] = dota[0].map(winRate)
dota[1] = dota[1].map(winRate)
dota[2] = dota[2].map(winRate)
dota[3] = dota[3].map(winRate)
dota[4] = dota[4].map(winRate)
dota[5] = -dota[5].map(winRate)
dota[6] = -dota[6].map(winRate)
dota[7] = -dota[7].map(winRate)
dota[8] = -dota[8].map(winRate)
dota[9] = -dota[9].map(winRate)

target = dota[10]
dota.drop(columns=10, inplace=True)

# User input
K = int(input())
userInput = pd.DataFrame([[j for j in input().split(',')] for i in range(K)])
userInput[0] = userInput[0].map(winRate)
userInput[1] = userInput[1].map(winRate)
userInput[2] = userInput[2].map(winRate)
userInput[3] = userInput[3].map(winRate)
userInput[4] = userInput[4].map(winRate)
userInput[5] = -userInput[5].map(winRate)
userInput[6] = -userInput[6].map(winRate)
userInput[7] = -userInput[7].map(winRate)
userInput[8] = -userInput[8].map(winRate)
userInput[9] = -userInput[9].map(winRate)

model = RandomForestClassifier(n_estimators=150, random_state=0)
model.fit(dota, target)

prediction = model.predict(userInput)
for i in prediction:
    print(i)
