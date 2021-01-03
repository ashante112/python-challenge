# PyPoll
# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources/election_data.csv')

# Open file to read (in read mode)
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    # Read header in first row
    csv_header = next (csvreader)
        
        #Starts reading at 2nd line, each row is now a list
        for csv_header[0] 