# Modules
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Bank.csv")


#  Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    

    header = next(csvreader)


def print_data(budget_data):

    date = str(budget_data[0])
    
   


    # Total number of months

    Total_Months = date


    # print out data

    print("Total Months:", len(Total_Months))




