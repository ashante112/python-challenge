# PyBank

# Import modules
import os
import csv

# Set path for file in variable csvpath
csvpath = os.path.join("Resources","budget_data.csv")

# Set lists for retrieval
months = []
profit_losses = []
changes_in_profit_losses = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]

# Open file to read (in read mode)
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    # Read header in first row
    csv_header = next(csvreader)
    first_row = next(csvreader)
    initial_net = int(first_row[1])

    for n in csvreader:
        month = n[0]
        months.append(month)
        
        profit_loss = int(n[1])
        profit_losses.append(profit_loss)

        net_change = profit_loss - initial_net
        initial_net = int(n[1])
        changes_in_profit_losses.append(net_change)

        if net_change > greatest_increase[1]:
            greatest_increase[0] = n[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = n[0]
            greatest_decrease[1] = net_change

total_months = len(months)
net_profit_losses = sum(profit_losses)
net_monthly_average = sum(changes_in_profit_losses)/len(changes_in_profit_losses)

print(f"Financial Analysis")
print(f"_______________________________")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_losses}")
print(f"Average Change: ${net_monthly_average}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Create Output file
output_path = os.path.join("Analysis","output.txt")

output=(
    f"\nFinancial Analysis\n"
    f"_______________________________\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit_losses}\n"
    f"Average Change: ${net_monthly_average}\n"
    f"Greatest Increase In Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease In Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

with open(output_path, 'w', newline="") as txtfile:
    txtfile.write(output)