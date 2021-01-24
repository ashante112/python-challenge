# PyBank

# Import modules
import os
import csv

# Set path for file in variable csvpath
csvpath = os.path.join("Resources","budget_data.csv")

# Set lists for retrieval
months = []
# profit_loss = []
# profit_loss_changes = []

# Open file to read (in read mode)
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    # Read header in first row
    csv_header = next(csvreader)

    for n in csvreader:
        month = n[0]
        months.append(month)

    print(f"Financial Analysis")
    print(f"_______________________________")
    print(f"Total Months: {len(months)}")

total_months = len(months)

# Create Output file
output_path = os.path.join("output.txt")

output=(
    f"\nFinancial Analysis\n"
    f"_______________________________\n"
    f"Total Months: {total_months}\n"
    # f"Total: ${profit_loss}\n"
    # f"Average Change: ${profit_loss_changes}\n"
    # f"Greatest Increase In Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    # f"Greatest Decrease In Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

with open(output_path, 'w', newline="") as txtfile:
    txtfile.write(output)

#Print Output  
# txtfile.write(f"Financial Analysis")
# txtfile.write(f"__________________________________")
# txtfile.write(f"Total Months: ${total_months}")
# txtfile.write(f"Total: " + "$"net_total)
# txtfile.write(f"Average Change: " + avg_change)
# txtfile.write(f"Greatest Increase in Profits: " + gipDate + "($"gip")")
# txtfile.write(f"Greatest Decrease in Profits: " + gdpDate + "($"gdp")")
