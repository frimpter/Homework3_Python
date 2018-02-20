# HW3.3 PyBoss

import os
import csv

# Make sure the current working directory is same as .py file location
path = os.path.abspath(os.path.dirname(__file__))

# Set path for files
employee1_csv = os.path.join(path, "employee_data1.csv")
employee2_csv = os.path.join(path, "employee_data2.csv")

# Create list of files to perform the set of actions for each one
files = [employee1_csv, employee2_csv]

EmpID = []
Name = []
first_name = []
last_name = []
DOB = []
NewDOB = []
SSN = []
NewSSN = []
State = []
NewState = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

for file in files:
    with open(file, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvfile) # Skip the header row
        for row in csvreader:
            EmpID.append(row[0])
            Name.append(row[1])
            DOB.append(row[2])
            SSN.append(row[3])
            State.append(row[4])

#Modify name entries
for name in Name:
    new_name = name.split(" ")
    first_name.append(new_name[0])
    last_name.append(new_name[1])

#Modify date entries
for date in DOB:
    new_date = date.split("-")
    new_DOB = new_date[1] + "/" + new_date[2] + "/" + new_date[0]
    NewDOB.append(new_DOB)

#Modify SSN entries
for ssn in SSN:
    new = ssn.split("-")
    new_SSN = "***-**-" + new[2]
    NewSSN.append(new_SSN)

#Modify state entries
for state in State:
    for long, short in us_state_abbrev.items():
        if state == long:
            new_state = short
    NewState.append(new_state)

#Bring the new lists together
new_file = zip(EmpID, first_name, last_name, NewDOB, NewSSN, NewState)

output_file = os.path.join(path, "PyBoss_Results.csv")

with open(output_file, "w", newline="") as output:
    writer = csv.writer(output)
    writer.writerow(["EmpID", "First Name", "Last Name", "DOB", "SSN", "State"]) # Make the header row
    writer.writerows(new_file)
