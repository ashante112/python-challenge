# PyBank

# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join('Resources','budget_data.csv')

# Open file to read (in read mode)
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    # Read header in first row
    csv_header = next (csvreader)
        
    #Starts reading at 2nd line, each row is now a list
    for row in csvreader:
        print(len(int(csvreader)))

# Create Output file

# Print Output  
# txtfile.write(f"Financial Analysis")
# txtfile.write(f"__________________________________")
# txtfile.write(f"Total Months: " + "$"total_months)
# txtfile.write(f"Total: " + "$"net_total)
# txtfile.write(f"Average Change: " + avg_change)
# txtfile.write(f"GReatest Increase in Profits: " + gipDate + "($"gip")")
# txtfile.write(f"Greatest Decrease in Profits: " + gdpDate + "($"gdp")")
          