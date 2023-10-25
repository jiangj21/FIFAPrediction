import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from csv import reader

file = pd.read_csv('international_matches.csv')

def histresults(chosen_country):
    df = file[(file["home_team"] == str(chosen_country)) | (file["away_team"] == str(chosen_country))]
    ##omit useless columns
    df_teams = df.drop(['date', 'home_team_continent', 'away_team_continent', 'home_team_fifa_rank',
                            'away_team_fifa_rank', 'home_team_total_fifa_points', 'away_team_total_fifa_points', 'home_team_score', 'away_team_score', 
                            'tournament', 'city', 'country', 'neutral_location', 'shoot_out',
                            'home_team_goalkeeper_score', 'away_team_goalkeeper_score', 'home_team_mean_defense_score',
                            'home_team_mean_offense_score', 'home_team_mean_midfield_score', 'away_team_mean_defense_score',
                            'away_team_mean_offense_score', 'away_team_mean_midfield_score'], axis=1)
    df_teams.tail()
    #print(df_teams)        
        
    #else:
        #print("Please enter a valid country name.")
                
    #create a list to store the results of the chosen country
    emptylist_cc = []
    for i, row in df_teams.iterrows():
        #print(row)
        ht = row['home_team']
        #at = row['away_team']
        result = row['home_team_result']
        row_list = [ht, result]
        #print(ht, at, result)
        emptylist_cc.append(row_list)
    #print(emptylist_cc)
        
    ##  To visualize historical results,
    ##  we first count the number of wins, losses, and draws
    win = 0
    loss = 0
    draw = 0
        
    ## loop through the emptylist_cc to get result
    for each_row in emptylist_cc:
            #print(each_row)
        if((chosen_country in each_row) and ('Win' in each_row)):
            win += 1
        elif((chosen_country not in each_row) and ('Win' in each_row)):
            loss += 1
        elif('Draw' in each_row):
            draw += 1
    #print(win, loss, draw)
    number_results = [win, loss, draw]
    return(number_results)

print(histresults('Argentina'))