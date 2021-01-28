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
        
    count_correy = 0
    count_khan = 0
    count_li = 0
    count_otooley = 0
    count_remaining = 0
    
    #Starts reading at 2nd line, each row is now a list
    for n in csvreader:
  
        # Defines the index for each header
        voter_id = n[0]
        county = n[1]
        candidate = n[2]

        # Appends each row to create the list
        voter_ids.append(voter_id)
        candidates.append(candidate)

        if candidate == 'Correy':
            count_correy = count_correy + 1

        elif candidate == 'Khan':
            count_khan = count_khan + 1
                
        elif candidate == 'Li':
            count_li = count_li + 1

        elif candidate == "O'Tooley":
            count_otooley = count_otooley + 1

        else: 
            count_remaining = count_remaining + 1

#Calculate number of votes cast and store in variable
total_votes = len(voter_ids)
num_candidates =  numpy.unique(candidates)
correy = num_candidates[0]
khan = num_candidates[1]
li = num_candidates[2]
otooley = num_candidates[3]

#Calculate the percentage of vote for each candidate

pct_correy = (count_correy/total_votes)*100
pct_khan = (count_khan/total_votes)*100
pct_li = (count_li/total_votes)*100
pct_otooley = (count_otooley/total_votes)*100

winner = max(pct_khan, pct_correy, pct_li, pct_otooley)

# Print the results report
print(f"Election Results")
print(f"_______________________________")
print(f"Total Votes: {total_votes}")
print(f"_______________________________")
print(f"{correy}: {pct_correy} ({count_correy})")
print(f"{li}: {pct_li} ({count_li})")
print(f"{khan}: {pct_khan} ({count_khan})")
print(f"{otooley}: {pct_otooley} ({count_otooley})")
print(f"_______________________________")
print(f"Winner: {winner}")
print(f"_______________________________")

# Create Output file
output_path = os.path.join("Analysis","output.txt")

output=(
f"\nElection Results\n"
f"_______________________________\n"
f"Total Votes: {total_votes}\n"
f"_______________________________\n"
f"{correy}: {pct_correy} ({count_correy})\n"
f"{li}: {pct_li} ({count_li})\n"
f"{khan}: {pct_khan} ({count_khan})\n"
f"{otooley}: {pct_otooley} ({count_otooley})\n"
f"_______________________________\n"
f"Winner: {winner}\n"
f"_______________________________"
)

with open(output_path, 'w', newline="") as txtfile:
    txtfile.write(output)

