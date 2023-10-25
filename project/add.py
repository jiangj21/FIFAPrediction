import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from csv import reader
from csv import writer


with open('international_matches.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    #list of column names
    fieldnames = reader.fieldnames
    #print(fieldnames)
    
    #convert column names to dictionary with empty values so we could add on later
    fieldnames_dict = dict.fromkeys(fieldnames)
    print(fieldnames_dict)
    
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
     
    # Open CSV file in append mode
    # Create a file object for this file
    with open('international_matches.csv', 'a') as f_object:
     
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
     
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(fieldnames_dict)
     
        # Close the file object
        f_object.close() 
file.close()
       