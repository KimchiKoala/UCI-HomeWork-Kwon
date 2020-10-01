# Modules
import os
import csv


# Path to collect data from the Resources folder
budget_csv = os.path.join("Bank.csv")

# Lists

months = []

total_list = []

revenue = []


#  Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # read in the header data
    header = next(csvreader)
    

  

    # Initialize your variables
    net_total = 0

    total_change_profits = 0

    initial_profit = 0

    total = 0
   


    for row in csvreader:

         # Define functions

        revenue.append(int(row[1]))

        # creating a new list for months
        months.append(row[0])

        
        # for loop to calculate and store net total values
        # i is the index... j is the value
        
    for i,j in enumerate(revenue[:-1]):

        total_list.append(revenue[i+1] - revenue[i])






    # Added + 1 at the end in order to find the correct month according to logic
    # the correct month is technically the "second month" not the "first month"

    # Calculating the greatest increase in profits
    greatest_increase_profits = max(total_list)

    increase_date = months[total_list.index(greatest_increase_profits) + 1]


    # Calculating the greatest decrease in losses
    greatest_decrease_profits = min(total_list)

    decrease_date = months[total_list.index(greatest_decrease_profits) + 1]


    


# Print out output
print("------------$¯\_(ツ)_/¯$------------")
print("Financial Analysis")
print("------------$¯\_(ツ)_/¯$------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(revenue)}")




print(f'Average Change: ${round(sum(total_list)/len(total_list),2)}')



print(f"Greatest Increase in Profits : {increase_date} --> (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits : {decrease_date} --> (${greatest_decrease_profits})")        



# output text file
import os

text_output = os.path.join("..", "Analysis",'PyBank_Analysis.txt')

with open(text_output,'w') as text: 

    text.write ("------------$¯\_(ツ)_/¯$------------")
    text.write("\nFinancial Analysis")
    text.write("\n------------$¯\_(ツ)_/¯$------------")
    text.write(f"\nTotal Months: {len(months)}")
    text.write(f"\nTotal: ${sum(revenue)}")


  
    text.write(f'\nAverage Change: ${round(sum(total_list)/len(total_list),2)}')


    text.write(f"\nGreatest Increase in Profits : {increase_date} --> (${greatest_increase_profits})")
    text.write(f"\nGreatest Decrease in Profits : {decrease_date} --> (${greatest_decrease_profits})")  


    text.close()     






 