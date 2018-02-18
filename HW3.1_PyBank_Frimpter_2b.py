#HW3.1 PyBank

import os
import csv

# Make sure the current working directory is same as .py file location
path = os.path.abspath(os.path.dirname(__file__))

# Set path for files
budget1_csv = os.path.join(path, "budget_data_1.csv")
budget2_csv = os.path.join(path, "budget_data_2.csv")

# Create list of files to perform the set of actions for each one
files = [budget1_csv, budget2_csv]

for file in files:
    name = file.split("/")[7] # Retrieve the file name from path
    with open(file, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile) # Skip the header row
        # Define/initialize variables
        months = 0
        total_revenue = 0
        sum_change = 0
        prior_rev = 0 # Store the revenue from the prior month (to calculate monthly change)
        revenues = {} # Initialize a dictionary to hold month/revenue for later use
        for row in csvreader:
            row[1] = int(row[1]) # Cast revenue an integer
            months += 1 # Count month
            total_revenue += row[1] # Accumulate total revenue
            change = row[1] - prior_rev # Calculate the revenue change vs. prior month
            sum_change += change # Accumulate monthly changes
            prior_rev = row[1] # Assign month's revenue to be the prior month for next iteration
            revenues[row[0]] = row[1] # Populate the month:revenue in dictionary
        avg_change = round((sum_change / months),2) # Calculate the average monthly revenue change
        max_rev = 0 
        min_rev = 0
        for date, revenue in revenues.items(): # Loop through date/revenue pairs
            revenue = int(revenue) # Cast revenue as integer
            if revenue > max_rev: 
                max_rev = revenue # Collect the biggest revenue value
                max_month = date # Collect the corresponding month
            if revenue < min_rev:
                min_rev = revenue # Collect the smallest revenue value
                min_month = date # Collect the corresponding month

    print("\n\nFinancial Analysis for " + str(name))
    print("------------------------------------------------------")
    print("Total Months: " + str(months))
    print("Total Revenue: $" + str(total_revenue))
    print("Average Monthly Change: $" + str(avg_change))
    print("Greatest Single Revenue Increase: " + str(max_month) + " ($" + str(max_rev) + ")")
    print("Greatest Single Revenue Decrease: " + str(min_month) + " ($" + str(min_rev) + ")")

    # Export output to a .txt file
    filename_path = os.path.join(path, name + "_output.txt")  
    with open(filename_path, "w") as output:
        output.write("\n\nFinancial Analysis for " + str(name))
        output.write("\n------------------------------------------------------")
        output.write("\nTotal Months: " + str(months))
        output.write("\nTotal Revenue: $" + str(total_revenue))
        output.write("\nAverage Monthly Change: $" + str(avg_change))
        output.write("\nGreatest Single Revenue Increase: " + str(max_month) + " ($" + str(max_rev) + ")")
        output.write("\nGreatest Single Revenue Decrease: " + str(min_month) + " ($" + str(min_rev) + ")")
