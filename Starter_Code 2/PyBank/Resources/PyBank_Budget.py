import os
import csv
from collections import Counter

file_path=os.path.join(r'/Users/franciscohmc/Desktop/python-challenge/python-challenge/Starter_Code 2/PyBank/Resources/budget_data.csv','budget_data.csv')

# Function to analyze financial records
def analyze_financial_records(csvdata):
    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    profit_loss_changes = []  # Change to list
    dates = []  # Change to list
    # Read the CSV file
    with open(csvdata) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        # Skip the header row
        next(csvreader)
        # Loop through each row in the CSV
        for row in csvreader:
            # Extract date and profit/loss values
            date = row[0]
            profit_loss = int(row[1])
            # Calculate total months and net total
            total_months += 1
            net_total += profit_loss
            # Calculate profit/loss changes
            if total_months > 1:
                change = profit_loss - previous_profit_loss
                profit_loss_changes.append(change)
                dates.append(date)
            # Update previous profit/loss
            previous_profit_loss = profit_loss
    # Calculate average change
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)
    # Find the greatest increase and decrease
    greatest_increase = max(profit_loss_changes)
    greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]
    greatest_decrease = min(profit_loss_changes)
    greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]
    # Display results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    # Save results to a text file
    write_results_to_file("financial_results.txt", total_months, net_total, average_change, greatest_increase_date, greatest_increase, greatest_decrease_date, greatest_decrease)
def write_results_to_file(file_name, total_months, net_total, average_change, greatest_increase_date, greatest_increase, greatest_decrease_date, greatest_decrease):
    with open(file_name, "w") as text_file:
        text_file.write("Financial Analysis\n")
        text_file.write("------------------\n")
        text_file.write(f"Total Months: {total_months}\n")
        text_file.write(f"Total: ${net_total}\n")
        text_file.write(f"Average Change: ${round(average_change, 2)}\n")
        text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
# Call the function with the file path
analyze_financial_records(file_path)




                  