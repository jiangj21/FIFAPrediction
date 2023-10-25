###This project aims to predict the winner of FIFA 2022 World Cup games using
###the dataset "international_matches.csv" available on Kaggle, 
###which comprises of international soccer results from 1872 to 2022.
###Dataset available from: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017


import pandas as pd
import matplotlib.pyplot as plt
import csv
from csv import reader


###read the matches result file
file = pd.read_csv('international_matches.csv')
#print(file.head())   #check whether the import is successful

###obtain all data on FIFA-related matches
file_FIFA = file[file['tournament'].str.contains("FIFA", regex = True)]
file_FIFA = file_FIFA[file_FIFA['tournament'] == 'FIFA World Cup']
#print(file_FIFA.head())

def winning_team(file_FIFA):
  winners =[]
  for i, row in file.iterrows():
    if row['home_team_result']=='Win':
      winners.append(row['home_team'])
    elif row['home_team_result']=='Lose':
      winners.append(row['away_team'])
    else:
      winners.append("Draw")
  return winners
'''
file_FIFA['winners']=winning_team(file_FIFA)
file_FIFA.head()
  '''
#the file should contain the following data columns:
    #date
    #home_team
    #away_team
    #home_score
    #away_score
    #tournament
    #city
    #neutral
    
###user input 

menu_option = 'HR'
#loop until the user chooses to end
while(menu_option != 'E'):
    menu_string = """
    HR = Historical Results of a Particular Country
    TT = Total Scores of World Cup / Top 20
    PR = Predict Winner of FIFA 2022
    ADD = Add This year's data to the file
    E = End program
    Choose an option:
    """
    menu_option = input(menu_string)
    
    if(menu_option == "TT"):
          #save file as total scores of world cup 
          #home team and away team score
          win_team = ''
          file_FIFA.loc[file_FIFA['home_team_result']=='Win','win_team'] = file_FIFA.loc[file_FIFA['home_team_result']=='Win','home_team']
          file_FIFA.loc[file_FIFA['home_team_result']=='Lose','win_team'] = file_FIFA.loc[file_FIFA['home_team_result']=='Lose','away_team']
          file_FIFA.loc[file_FIFA['home_team_result']=='Draw','win_team'] = "Draw"
          file_FIFA.head()
          
          """
          if home_team_result = 'Win'
            home_team_win +=1
          if home_team_result = 'Lose'
            away_team_win +=1
            """
          diagram_present = input("Please press p to print diagram for present all team/t for top 20 rank teams: ")
          if(diagram_present=='p'):
            s = file_FIFA.groupby('win_team')['win_team'].count()
            s.sort_values(ascending =False, inplace=True)
            s.drop(labels=['Draw'],inplace=True)
            s.sort_values(ascending=True,inplace=True)
            s.tail(20).plot(kind='barh',figsize=(10,6),title='Top 20 winners of world cup', color = ['r', 'b', 'g', 'y', 'orange', 'purple', 'k', 'm'])
            

        