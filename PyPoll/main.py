import os
import csv

#Set Path to the input file
#FILES TO LOAD OR INPUT
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#Set Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
#winner = [] QUE DIRIA?

#Opening and reading csv file
with open(csvpath) as csvfile:

    #specifying delimiter and variable storing content
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header row first and skip step if no header
    csv_header = next(csvfile)
    

    #Calculate each data row after header
    for row in csvreader:

        #Calculate Total number of votes cast
        total_votes += 1
        #total_votes plus one. cada que el row baja suma

        #Calculate Total number of votes each candidate won        
        if (row[2] == 'Khan'):
            khan_votes += 1
        #IS 2 BECAUSE LIST STARTS WITH ZERO
        
        elif (row[2] == 'Correy'): # COMPARING EACH VALUE SAME COLUMN DIFFERENT ROW
            correy_votes += 1

        elif (row[2] == 'Li'):
            li_votes += 1
        
        else:
            otooley_votes += 1

    #Calculate % of votes each candidate won
    khan_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    #ASSIGNATION RIGHT SIDE WITH LEFT SIDE

#Calculate the winner of the election based on popular vote
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)#THEY ARE NOT NAMES BUT VARIABLES, THATS WHY NO A LIST

    if winner == khan_votes: #IS NOT WITH PARENTHESIS BECAUSE IS A VARIABLE
        winner_name = "Khan"#ASSIGNING STRING VALUE ASSIGNED TO WINER VALUE 
    
    elif winner == correy_votes:
        winner_name = "Correy"

    elif winner == li_votes:
        winner_name = "Li"

    else:
        winner_name = "O'Tooley"


#Print Analysis
print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------")
print(f"Khan: {khan_percent:.3%} ({khan_votes})") #.3% Tres decimales y signo%
print(f"Correy: {correy_percent:.3%} ({correy_votes})")
print(f"Li: {li_percent:.3%} ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%} ({otooley_votes})")
print(f"------------------------")
print(f"Winner: {winner_name}")
print(f"------------------------")

#Output file -writ ino txt-
#FILES TO OUTCOME OR OUTPUT
output_file = os.path.join("..", "PyPoll", "Analysis", "election_data_Analysis.text")
with open(output_file,"w") as txtfile:

#Writing data on file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Khan: {khan_percent:.3%} ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%} ({otooley_votes})\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"------------------------\n")




