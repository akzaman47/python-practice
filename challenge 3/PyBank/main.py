import os

#  Creating a function that will read the CSV file

import csv

# Here I am trying to create the path for the file on my computer

filepath = os.path.join('Resources', 'budget_data.csv')

# This line of code will create a Report.txt file for me with the output

my_report = open('Analysis/Report.txt', 'w')

# Here I am reading the CSV file and storing it

with open(filepath) as csvfile:

    reader = csv.DictReader(csvfile)  

# Here I am creating and initialzing the variables I need 

    total_rev = 0
    months = 0
    pre_rev = 0
    total_ch = 0
    increase = ['',0]
    decrease = ['',0]

# This is my coniditional loop that allows me to iterate and store new values
    
    for row in reader:
        rev = int(row['Profit/Losses'])    # Creating the rev variable to store the int values
        months+=1                          # We want to get to keep iterating through all the months
        total_rev+=rev                     # total revenue will be determined by the constant summation of the previous revenue value

        change = rev - pre_rev             # To determine change we subtract previous rev from revenue
        if (pre_rev == 0):                 # conditional to loop
            change = 0                     # if prev_rev = 0 then change is 0
        
        pre_rev = rev                      # since prev_rev is not 0, it will be filled with the next rev value
        total_ch+=change                   # total change is now filled with the change = rev - pre_rev

        # This is my conditional for greatest increase and greatest decrease
        if(change>increase[1]):            
            increase[1] = change
            increase[0] = row['Date']

        if(change<decrease[1]):
            decrease[1] = change 
            decrease[0] = row['Date']
                                           # TA should me a way to style the outputs like this and it made printing easier
output = f'''                              
    Financial Analysis
----------------------------
Total Months: {months}
Total: ${total_rev:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {increase[0]} (${increase[1]:,})
Greatest Decrease in Profits: {decrease[0]} (${decrease[1]:,})
'''

print(output)
my_report.write(output)
