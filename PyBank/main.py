#Import modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

# Open file to read
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    