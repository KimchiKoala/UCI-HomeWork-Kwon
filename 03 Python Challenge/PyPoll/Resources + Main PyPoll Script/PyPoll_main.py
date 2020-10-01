# Modules
import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join("Poll.csv")

# Create lists and initialize variables

total_votes = 0

candidate_list = []

vote_count = []

Winner_Vote_Count = 0

#  Read in the CSV file
with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # read in the header data
    header = next(csvreader)


    # for loop

    for row in csvreader:
        # Count the total number of votes using increment feature

        total_votes += 1

       #Creating a list of unique candidates 
        if(row[2] not in candidate_list):

            candidate_list.append(row[2])

            vote_count.append(0)

        #Getting the Index in candidate list 
        candidate_index = candidate_list.index(row[2])


        #Using the same Index to increment count of votes for the candidate
        vote_count[candidate_index] += 1

# print the good stuff
print("---(>'-')> <('-'<) ^('-')^ v('-')v(>'-')>")
print("ELECTION RESULTS")   
print("---(>'-')> <('-'<) ^('-')^ v('-')v(>'-')>")
print("-----------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------")



# finding out winner and winner percentage

for x in range(len(candidate_list)):

    vote_percent = round((vote_count[x]/total_votes)*100,3)

    print(f"{candidate_list[x]}: {vote_percent}% ({vote_count[x]})")

  
print("-----------------------------------------")

Winner_Vote_Count = max(vote_count)

Winner = candidate_list[vote_count.index(Winner_Vote_Count)]

print(f"Winner: {Winner}")

print("-----------------------------------------")

# output text file
import os

text_output = os.path.join("..", "Analysis",'PyPoll_Analysis.txt')

with open(text_output,'w') as text:

    text.write("\n---(>'-')> <('-'<) ^('-')^ v('-')v(>'-')>")
    text.write("\nELECTION RESULTS")
    text.write("\n---(>'-')> <('-'<) ^('-')^ v('-')v(>'-')>")
    text.write(f"\nTotal Votes: {total_votes}")
    text.write("\n-----------------------------------------")

    for x in range(len(candidate_list)):

        vote_percent = round((vote_count[x]/total_votes)*100,3)
        
        text.write(f"\n{candidate_list[x]}: {vote_percent}% ({vote_count[x]})")

    text.write("\n-----------------------------------------")

    text.write(f"\nWinner: {Winner}")

    text.write("\n-----------------------------------------")

    text.close()



