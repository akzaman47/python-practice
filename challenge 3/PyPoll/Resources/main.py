import os

#  Creating a function that will read the CSV file

import csv

# Here I am trying to create the path for the file on my computer

filepath = os.path.join('Resources', 'election_data.csv')

# This line of code will create a Report.txt file for me with the output

my_report = open('Analysis/Report.txt', 'w')

# Here I am reading the CSV file and storing it

with open(filepath) as csvfile:

    reader = csv.DictReader(csvfile)

    candidates_list = [candidate[2] for candidate in reader]  

    # Function to determine the total votes
    total_vote = len(candidates_list)

    # Here I am creating the list of unique candidates that appear in the csv
    info = [[candidate,candidates_list.count(candidate)] for candidate in set(candidates_list)]

    # Here I am sorting the list to store the value of the winner
    info = sorted(info, key=lambda x: x[1], reverse=True)
     
    # Here I am setting up the function to determine the percentage 
    for candidate in info:
    percent = (candidate[1] / total_vote) * 100
    print(f'{candidate[0]}: {percent:6.3f}% ({candidate[1]})')
 

                                # TA should me a way to style the outputs like this and it made printing easier
output = f'''                              
 Election Results
-------------------------
Total Votes: {total_vote:,}
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: {info[0][0]}
-------------------------
'''

print(output)
my_report.write(output)
