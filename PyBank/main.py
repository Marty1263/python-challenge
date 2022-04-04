#Import CSV fiole
import os
import csv


#Set CSV path
csvpath = os.path.join('..','python-challenge','budget_data.csv')

#Variables

total_months = 0
month_count = []
month_change = []
total_amount = 0
profit = 0
profit_month = 0
lost = 0
lost_month = 0

#Read CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, deliomiter=',')
    #read the header if no header skip it
    csv_header = next(csvreader)
    row = next(csvreader)

# Calculat number of months, amount of profit/ losses, set variables for rows
    previous_row = int(row[1])
    total_months += 1
    total_amount += int(row[1])
    profit = int(row[1])
    profit_month = row[0]
    
    for row in csvreader:
        total_months += 1
        total_amount += int(row[1])
        #calc change from current month to previuos month
        
        profit_change = int(row[1]) - previous_row
        month_change.append(profit_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        #calc greatest increase
        if int(row[1]) > profit:
            profit = int(row[1])
            profit_month = row[0]
        
        #calc greatest decrease
        if int(row[1]) < lost:
            lost = int(row[1])
            lost_month = row[0]
            
    #calc average and date
    average_change = sum(month_change) / len(month_change)
    
    highest = max(month_change)
    lowest = min(month_change)
    
# Print analysis
print("Financial Analysis")
print("------------------------")
print("Total Months: {total_months}")
print("Total: $ {total_amount}")
print("Average Change: $ {average_change:.2f}")
print("Greatest Increase in Profits:, {profit_month}, (${highest})")
print("Greatest Decrease in Profits:,{lost_month}, (${lowest})")
