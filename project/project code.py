### This project aims to predict the winner of FIFA 2022 World Cup games using
###     the dataset "international_matches.csv" available on Kaggle, 
###     which comprises of international soccer results from 1872 to 2022.
### The idea is inspired by the current FIFA in Qatar as well as a Kaggle post:
###     https://www.kaggle.com/code/sslp23/predicting-fifa-2022-world-cup-with-ml
### Dataset available from: https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017

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

#the file should contain the following useful data columns:
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
    
#function to obtain the historical results of a particular country    
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
    
    if(menu_option == "HR"):    #- obtain history results of a particular country
        chosen_country = input("Which country would you like to choose? ")
        if(check_country(chosen_country)):
            numbers = histresults(chosen_country)
            
            ###visualization of the plot
            
            #################################################################        
            ###### the following function about //matplotlib - barplot// 
            ###### is referenced from matplotlib website            
            result = ["Win","Loss","Draw"]
            count = numbers
            #create bars and choose color
            plt.bar(result, count, color = (0.5,0.1,0.5,0.6))
            #add titles and axis labels
            plt.title("Historical results of " + str(chosen_country))
            plt.xlabel("Win vs. Loss")
            plt.ylabel("Count")        
            plt.show()       
            #################################################################        
            
            #extension - add another country to compare winning/losing results!!
            
            another = input("Would you like to add another country to compare the results? (Y/N) ")
            if(another == 'Y'):
                chosen_country2 = input("Which country would you like to choose for your 2nd option? ")
                if(check_country(chosen_country2)):                
                    numbers2 = histresults(chosen_country2)
                
                    ###visualization of the comparison of results
                
                    #################################################################        
                    ###### the following function about //matplotlib - barplot// 
                    ###### is referenced from matplotlib website                      
                    labels = ["Win","Loss","Draw"]
                    cc1 = numbers
                    cc2 = numbers2
                
                    x = np.arange(len(labels))  # the label locations
                    width = 0.35  # the width of the bars
                
                    fig, ax = plt.subplots()
                    rects1 = ax.bar(x - width/2, cc1, width, label= chosen_country)
                    rects2 = ax.bar(x + width/2, cc2, width, label= chosen_country2)
                
                    # Add some text for labels, title and custom x-axis tick labels, etc.
                    ax.set_ylabel("count")
                    ax.set_title('Comparison of Historical Results')
                    ax.set_xticks(x, labels)
                    ax.legend()
                
                    ax.bar_label(rects1, padding=3)
                    ax.bar_label(rects2, padding=3)
                
                    fig.tight_layout()
                    plt.show()     
                    #################################################################
                    
            else:
                print("Thank you")            
                                
        
    elif(menu_option == "TT"):
            #save file as total scores of world cup 
            #home team and away team score
            win_team = ''
            
            #################################################################        
            ###### the following function about //pandas-loc[]// is referenced from:
            ###### https://pandas.pydata.org/docs/reference/frame.html              
            file_FIFA.loc[file_FIFA['home_team_result']=='Win','win_team'] = file_FIFA.loc[file_FIFA['home_team_result']=='Win','home_team']
            file_FIFA.loc[file_FIFA['home_team_result']=='Lose','win_team'] = file_FIFA.loc[file_FIFA['home_team_result']=='Lose','away_team']
            file_FIFA.loc[file_FIFA['home_team_result']=='Draw','win_team'] = "Draw"
            file_FIFA.head()
            #################################################################
            
            ###visualize the ranking and the scores in bar plot
            diagram_present = input("Please press 'p' to print diagram for top 20 teams \nPress 't' for total score each teams scored: ")
            
            #################################################################        
            ###### the following function about //matplotlib - barplot // is referenced from:
            ###### https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py  
            
            if(diagram_present=='p'):
                #sort the values by win_teams (a column from the given excel)
                s = file_FIFA.groupby('win_team')['win_team'].count()
                s.sort_values(ascending =False, inplace=True)
                s.drop(labels=['Draw'],inplace=True)
                s.sort_values(ascending=True,inplace=True)
                s.tail(20).plot(kind='barh',figsize=(10,6),title='Top 20 winners of world cup since 1993', color = ['r', 'b', 'g', 'y', 'orange', 'purple', 'k', 'm'])
                
            elif(diagram_present == 't'):
                #sort the teams by total scores
                file_score_home_20 =file_FIFA[['home_team','home_team_score']]
                column_update = ['teams','score']
                file_score_home_20.columns = column_update
                file_score_away_20 = file_FIFA[['away_team','away_team_score']]
                file_score_away_20.columns = column_update
                file_score_20 = pd.concat([file_score_home_20,file_score_away_20],ignore_index = True)
                s_score_20 = file_score_20.groupby('teams')['score'].sum()
                s_score_20.sort_values(ascending = True, inplace = True)
                s_score_20.sort_values(ascending = True, inplace = True)
                s_score_20.tail(20).plot(kind = 'barh',figsize=(8,12),title ='Top 20 in Total Scores of World Cup since 1993', color = ['r', 'b', 'g', 'y', 'orange', 'purple', 'k', 'm']) 
            ###############################################################
            
            else:
                input("Please start over and input a valid key. (p/t) ")
                
    elif(menu_option == 'PR'): 
        #predict the winner between two input countries based on their previous avg scores
        country1 = input("What is the first country in this match? ")
        while not(check_country(country1)): #check if the country name is valid
            country1 = input("What is the first country in this match? ")
        country2 = input("What is the second country in this match? ")
        while not(check_country(country2)):
            country2 = input("What is the second country in this match? ")        
        
        #call historical results function to get the number of win, loss, and draw for the input countries            
        country1_results = histresults(country1)
        country2_results = histresults(country2)
        #print(country1_results)
        #print(country2_results)
        
        #multiple win by 3 and draw by 1 to get total scores of each country            
        country1_scores = int(country1_results[0]) * 3 + int(country1_results[2]) * 1
        country2_scores = int(country2_results[0]) * 3 + int(country2_results[2]) * 1
        
        #get avg scores            
        country1_avg = country1_scores / (int(country1_results[0]) + int(country1_results[1]) + int(country1_results[2]))
        country2_avg = country2_scores / (int(country2_results[0]) + int(country2_results[1]) + int(country2_results[2]))
                    
        #print(country1_avg)
        #print(country2_avg)
        
        #get probability            
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
                
    elif(menu_option == "ADD"):    #- add new resuls as the 2022 matches are ongoing
        with open('international_matches.csv', 'r') as file:
            reader = csv.DictReader(file)
    
            #list of column names
            fieldnames = reader.fieldnames
            #print(fieldnames)
    
            #convert column names to dictionary with empty values so we could add on later
            fieldnames_dict = dict.fromkeys(fieldnames)
            #print(fieldnames_dict)
    
            date = input('On what date was the match? (YYYY/MM/DD) ')
            home_team = input('Who was the home team？ ')
            away_team = input('Who was the away team？ ')
            home_team_continent = input('Where is the home team from? ')
            away_team_continent = input('Where is the away team from? ')
            home_team_score = input('What did the home team score? ')
            away_team_score = input('What did the away team score? ')
    
            # Dictionary that we want to add as a new row
            fieldnames_dict = {'date': date, 'home_team': home_team, 'away_team': away_team,
                               'home_team_continent': home_team_continent, 'away_team_continent': away_team_continent,
                               'home_team_score': home_team_score, 'away_team_score': away_team_score,
                               'tournament' : 'FIFA World Cup qualification', 'city': 'Doha', 'country': 'Qatar'}
            
            #################################################################        
            ###### the following function about //append rows to csv files// is referenced from:
            ###### https://www.geeksforgeeks.org/how-to-append-a-new-row-to-an-existing-csv-file/            
            # Open CSV file in append mode
            # Create a file object for this file
            with open('international_matches.csv', 'a') as f_object:
     
                # Pass the file object and a list
                # of column names to DictWriter()
                # You will get a object of DictWriter
                dictwriter_object = csv.DictWriter(f_object, fieldnames=fieldnames_dict)
     
                # Pass the dictionary as an argument to the Writerow()
                dictwriter_object.writerow(fieldnames_dict)
     
                # Close the file object
                f_object.close() 
            #################################################################
            
        file.close()   