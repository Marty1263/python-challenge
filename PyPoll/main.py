#import
import os 
import csv

#variables
total_vote = 0
Khan_vote = 0
Correy_vote = 0
Li_vote = 0
OTooley_vote = 0

#set path
csvpath = os.path.join('.','Resorces','election_data.csv')

#read csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in csvreader:
        


        #calc total votes
        total_vote += 1
        #calc total vote each candidate won
        if (row[2] == "Khan"):
            Khan_vote += 1
        elif (row[2] == "Correy"):
            Correy_vote += 1
        elif (row[2] == "Li"):
            Li_vote +=1
        else:
            OTooley_vote += 1
            
    #calc percentage each candidate
    Khan_precent = Khan_vote / total_vote
    Correy_precent = Correy_vote / total_vote
    Li_precent = Li_vote / total_vote
    OTooley_precent = OTooley_vote / total_vote
    
    #calc winner
    
    winner = max(Khan_vote, Correy_vote, Li_vote, OTooley_vote)
    if winner == Khan_vote:
        winner_name = "Khan"
    elif winner == Correy_vote:
        winner_name = "Correy"
    elif winner == Li_vote:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"
#print analysis
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_vote}")
print("---------------------------")
print(f"Kahn: {Khan_precent:.3%}({Khan_vote})")
print(f"Correy: {Correy_precent:.3%}({Correy_vote})")
print(f"Li: {Li_precent:.3%}({Li_vote})")
print(f"O'Tooley: {OTooley_precent:.3%}({OTooley_vote})")
print("---------------------------")
print(f"Winner: {winner_name}")
print("---------------------------")

#output file
export_file = os.path.join('.','Resorces','new_data_vote.text')

with open(export_file, 'w',) as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_vote}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {Khan_precent:.3%}({Khan_vote})\n")
    txtfile.write(f"Correy: {Correy_precent:.3%}({Correy_vote})\n")
    txtfile.write(f"Li: {Li_precent:.3%}({Li_vote})\n")
    txtfile.write(f"O'Tooley: {OTooley_precent:.3%}({OTooley_vote})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")
        