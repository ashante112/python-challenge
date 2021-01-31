# PyPoll
# Import modules
import os
import csv
import numpy

# Set path for file
csvpath = os.path.join('Resources/election_data.csv')

# Set lists to fill
voter_ids = []
candidates = []

# Open file to read
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    # Read header in first row
    csv_header = next(csvreader)

    # Create candidate dictionary
    candidate_dict = {}
    
    #Starts reading at 2nd line, each row is now a list
    for n in csvreader:
  
        # Defines the index for each header
        voter_id = n[0]
        county = n[1]

        # Appends each row to create the list
        voter_ids.append(voter_id)
        
        # Condition to fill candidate counts in dictionary
        if n[2] not in candidate_dict:
            candidate_dict[n[2]] = 1
        else:
            candidate_dict[n[2]] += 1
       
#Calculate number of votes cast and store in variable
total_votes = len(voter_ids)

# Initialize max_count value
max_count = 0

# Print report results
print(f"Election Results")
print(f"_______________________________")
print(f"Total Votes: {total_votes}")
print(f"_______________________________")
# Print the results for candidate data
for key,val in candidate_dict.items():
    print(f"{key}: {round(val/total_votes*100,2)}% ({val})")
    if val > max_count:
        max_count = val
        winner = key
print(f"_______________________________")
print(f"Winner: {winner}")
print(f"_______________________________")

# Create output file
output_path = os.path.join("Analysis","output.txt")

# Print to Report to output file
with open(output_path, 'w', newline="") as txtfile:
    txtfile.write(f"\nElection Results\n")
    txtfile.write("_______________________________\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"_______________________________\n")
    
    # Print the results for candidates
    for key,val in candidate_dict.items():
        txtfile.write(f"{key}: {round(val/total_votes*100,2)}% ({val})\n")
    txtfile.write(f"_______________________________\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"_______________________________")
