# PyPoll.py

# import module to allow creating file paths across operating systems
import pathlib

# import module for reading CSV files
import csv

# Set path for CSV file
csvpath = pathlib.Path("Resources", "election_data.csv")

# Open and read the CSV
with open(csvpath) as csvfile:
    #print(csvreader)
    
    # Read header row
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")
 
    #Define variables as empty lists
    
    Votes = []
    Candidates = []

    # Find total number of votes
    for row in csvreader:
        Votes.append(row[0])
        Candidates.append(row[2])
        Total_Votes = (len(Votes))

    # Find the number of vote for each candidate

    Votes_for_Khan = int(Candidates.count("Khan"))
    # print(Votes_for_Khan)
    Votes_for_Correy = int(Candidates.count("Correy"))
    Votes_for_Li = int(Candidates.count("Li"))
    Votes_for_O_Tooley = int(Candidates.count("O\'Tooley"))
    # print(Votes_for_O_Tooley)

    # Calculate the vote percentage for each candidate

    Votes_Percentage_Khan = (Votes_for_Khan / Total_Votes) * 100
    #print(Votes_Percentage_Khan)
    Votes_Percentage_Correy = (Votes_for_Correy / Total_Votes) * 100
    Votes_Percentage_Li = (Votes_for_Li / Total_Votes) * 100
    Votes_Percentage_O_Tooley = (Votes_for_O_Tooley / Total_Votes) * 100

    # Select winner with highest votes
    # Create a list of votes of each candidate
    Votes = [Votes_for_Khan, Votes_for_Correy, Votes_for_Li, Votes_for_O_Tooley]
    # if the maximum of votes corresponds to an index from the list of votes, the object with that index is winner 
    if Votes.index(max(Votes)) == 0:
        Winner = "Khan"
    elif Votes.index(max(Votes)) == 1:
        Winner = "Correy"
    elif Votes.index(max(Votes)) == 2:
        Winner = "Li"
    else:
        Winner = "O'Tooley"


    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {Total_Votes}")
    print("---------------------")
    print(f"Khan: {Votes_Percentage_Khan:.3f}% ({Votes_for_Khan})")
    print(f"Correy: {Votes_Percentage_Correy:.3f}% ({Votes_for_Correy})")
    print(f"Li: {Votes_Percentage_Li:.3f}% ({Votes_for_Li})")
    print(f"O'Tooley: {Votes_Percentage_O_Tooley:.3f}% ({Votes_for_O_Tooley})")
    print("---------------------")
    print(f"Winner: {Winner}")
    print("---------------------")

    # Set the path for output text file
    output_path = pathlib.Path("Resources/PyPoll_output.txt")

    # Open the file with write mode
    with open(file=output_path, mode='w', newline='') as txtfile:
        txtfile.write("Election Results: \n")
        txtfile.write("------------------- \n")
        txtfile.write(f"Total Votes: {Total_Votes} \n")
        txtfile.write(f"Khan: {Votes_Percentage_Khan:.3f}% ({Votes_for_Khan}) \n")
        txtfile.write(f"Correy: {Votes_Percentage_Correy:.3f}% ({Votes_for_Correy}) \n")
        txtfile.write(f"Li: {Votes_Percentage_Li:.3f}% ({Votes_for_Li}) \n")
        txtfile.write(f"O'Tooley: {Votes_Percentage_O_Tooley:.3f}% ({Votes_for_O_Tooley}) \n")
        txtfile.write(f"Winner: {Winner}")
        txtfile.close()
