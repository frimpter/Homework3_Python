# HW3.2 PyPoll

import os
import csv

# Make sure the current working directory is same as .py file location
path = os.path.abspath(os.path.dirname(__file__))

# Set path for files
polling1_csv = os.path.join(path, "election_data_1.csv")
polling2_csv = os.path.join(path, "election_data_2.csv")

# Create list of files to perform the set of actions for each one
files = [polling1_csv, polling2_csv]

total_votes = 0 # Initialize the total votes counter
tally = {} # Initialize dictionary to store and count candidate:votes pairs

for file in files:
    with open(file, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile) # Skip the header row
        for row in csvreader:
            total_votes += 1 # Accumulate the total number of votes
            tally[row[2]] = tally.get(row[2], 0) + 1 # For each candidate, add 1 vote

# Collate, print and export the results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
most_votes = 0 # Initialize the variable to hold the candidate with the most votes
for candidate, votes in tally.items():
    votes = int(votes) # Cast the votes as an integer
    percent_votes = round(votes / int(total_votes), 2) * 100 # Calculate the percentage for each candidate
    if votes > most_votes: # Identify the candidate with the most votes
        most_votes = votes
        winner = candidate
    print(str(candidate) + ": " + str(votes) + " (" + str(percent_votes) + "%)")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

# Export output to a .txt file
filename_path = os.path.join(path, "PyPoll_Results.txt")
with open(filename_path, "w") as output:
    output.write("\nElection Results")
    output.write("\n-------------------------")
    output.write("\nTotal Votes: " + str(total_votes))
    output.write("\n-------------------------")
    most_votes = 0
    for candidate, votes in tally.items():
        votes = int(votes)
        percent_votes = round(votes / int(total_votes), 2) * 100 # Recalculate this otherwise it is left over from the last candidate in the loop
        output.write("\n" + str(candidate) + ": " + str(votes) + " (" + str(percent_votes) + "%)")
    output.write("\n-------------------------")
    output.write("\nWinner: " + str(winner))
    output.write("\n-------------------------")
