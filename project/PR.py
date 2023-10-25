###This project aims to predict the winner of FIFA 2022 World Cup games using
###the dataset "international_matches.csv" available on Kaggle, 
###which comprises of international soccer results from 1872 to 2022.
###Dataset available from: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from csv import reader
from csv import writer

#################################################################
###### the following code about module pandas (read_csv) is referenced from:
###### https://pandas.pydata.org/docs/reference/frame.html
           
###read the matches result file
file = pd.read_csv('international_matches.csv')
#print(file.head())   #check whether the import is successful
###obtain all data on FIFA-related matches
file_FIFA = file[file['tournament'].str.contains("FIFA", regex = True)]
file_FIFA = file_FIFA[file_FIFA['tournament'] == 'FIFA World Cup']
#print(file_FIFA.head())
#################################################################



#the file should contain the following data columns:
    #date
    #home_team
    #away_team
    #home_score
    #away_score
    #tournament
    #city
    #neutral
 
#function to check whether the input country is part of the csv file
def check_country(chosen_country):
        #################################################################        
        ###### the following function about //pandas-iterate rows// is referenced from:
        ###### https://pandas.pydata.org/docs/reference/frame.html          
    ht_list = []
    for i, row in file.iterrows():
        ht = row['home_team']
        row_list = [ht]
        ht_list.append(row_list)
        #print(ht_list)
        #################################################################
            
    chosen_country_list = [chosen_country] 
            #change the country name to a list object to find matches in ht_list
    if(chosen_country_list in ht_list):
        print("Thank you")
        return True
    else:
        print("Country not found, please enter a valid country name.")
        return False 
 
   
def histresults(chosen_country):
    
    df = file[(file["home_team"] == str(chosen_country)) | (file["away_team"] == str(chosen_country))]
    ##omit useless columns
    df_teams = df.drop(['date', 'home_team_continent', 'away_team_continent', 'home_team_fifa_rank',
                            'away_team_fifa_rank', 'home_team_total_fifa_points', 'away_team_total_fifa_points', 'home_team_score', 
                            'away_team_score', 'tournament', 'city', 'country', 'neutral_location', 'shoot_out',
                            'home_team_goalkeeper_score', 'away_team_goalkeeper_score', 'home_team_mean_defense_score',
                            'home_team_mean_offense_score', 'home_team_mean_midfield_score', 'away_team_mean_defense_score',
                            'away_team_mean_offense_score', 'away_team_mean_midfield_score'], axis=1)
    df_teams.tail()
    #print(df_teams)
                    
    #create a list to store the results of the chosen country
    emptylist_cc = []
    
    #################################################################    
    ###### the following function about //pandas-iterate rows// is referenced from:
    ###### https://pandas.pydata.org/docs/reference/frame.html    
    for i, row in df_teams.iterrows():
        #print(row)
        ht = row['home_team']
        #at = row['away_team']
        result = row['home_team_result']
        row_list = [ht, result]
        #print(ht, at, result)
        emptylist_cc.append(row_list)
    #print(emptylist_cc)
    #################################################################
    
            
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
    number_results = [win, loss, draw]
    return(number_results)

    
###user input 

menu_option = 'X'
#loop until the user chooses to end
while(menu_option != 'E'):
    menu_string = """
    HR = Historical Results of a Particular Country
    TT = Total Scores of World Cup / Top 20
    PR = Predict Winner of FIFA 2022 matches
    ADD = Add New Results of FIFA 2022
    E = End program
    Choose an option:
    """
    menu_option = input(menu_string)
    
    if(menu_option == 'PR'):
        country1 = input("What is the first country in this match? ")
        while not(check_country(country1)):
            country1 = input("What is the first country in this match? ")
        country2 = input("What is the second country in this match? ")
        while not(check_country(country2)):
            country2 = input("What is the second country in this match? ")        
        
        country1_results = histresults(country1)
        country2_results = histresults(country2)
        #print(country1_results)
        #print(country2_results)
        
        country1_scores = int(country1_results[0]) * 3 + int(country1_results[2]) * 1
        country2_scores = int(country2_results[0]) * 3 + int(country2_results[2]) * 1
        
        country1_avg = country1_scores / (int(country1_results[0]) + int(country1_results[1]) + int(country1_results[2]))
        country2_avg = country2_scores / (int(country2_results[0]) + int(country2_results[1]) + int(country2_results[2]))
        
        #print(country1_avg)
        #print(country2_avg)
        
        country1_winning_prob = country1_avg / (country1_avg + country2_avg)
        country2_winning_prob = country2_avg / (country1_avg + country2_avg)
        
        print(country1 + "'s probability to win: " + str(country1_winning_prob))
        print(country2 + "'s probability to win: " + str(country2_winning_prob))
        
        if(country1_winning_prob > country2_winning_prob):
            print(country1 + " has a higher probability to win. ")
        if(country1_winning_prob < country2_winning_prob):
            print(country2 + " has a higher probability to win. ")
        if(country1_winning_prob == country2_winning_prob):
            print(country1 + " ties with " + country2)        
        
        