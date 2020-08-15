#Import Modules & dependencies
import os
import csv 

#Set Path to the input file
#FILES TO LOAD OR INPUT
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#Set Variables
total_months = 0
netot_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Opening and reading csv file 
with open(csvpath) as csvfile:

    #specifying deliminter and variable storing content
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header row first and skip step if no header
    csv_header = next(csvreader)
    row = next(csvreader)

    #Calculate total number of months included, net amount of "Profit/Losses" adn set variables for rows
    total_months += 1
    previous_row = int(row[1])
    netot_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    # MONTH IS ZERO BECAUSE IS IN THE FIRST COLUMN

    #Calculate each data row after header
    for row in csvreader:
        
        #Calculate total # of months in dataset
        total_months += 1
        #Calculate net amount of Profit & Losses over the period
        netot_amount += int(row[1])

        #Calculate change -current month vs previous-
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])

        #Calculate Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #Calculate Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]    

    #Calculate averages and dates
    average_change = sum(monthly_change)/ len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

#Printing values
print(f'Financial Analysis')
print(f'-------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${netot_amount}')
print(f'Average Change: ${average_change:.2f}') 
#Average chage 2 decimals float OK. http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/float.html
print(f'Greatest Increase in profits:, {greatest_increase_month}, (${highest})')
print(f'Greatest Decrease in profits:, {greatest_decrease_month}, (${lowest})')

#Output file -write into txt-
#FILES TO OUTCOME OR OUTPUT
output_file = os.path.join("..", "PyBank", "Analysis", "budget_data_Analysis.text")
with open(output_file, "w",) as txtfile:

#Writing data on file
    txtfile.write(f'Financial Analysis\n') #\n pasa al siguiente renglon
    txtfile.write(f'-------------------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${netot_amount}\n')
    txtfile.write(f'Average Change: ${average_change:.2f}\n')
    txtfile.write(f'Greatest Increase in profits: {greatest_increase_month}, (${highest})\n')
    txtfile.write(f'Greatest Decrease in profits: {greatest_decrease_month}, (${lowest})\n')




    

    





   

