# PyBank.py

# import the module to allow creating file paths across operating systems
import pathlib

# import module for reading CSV files
import csv

# Set path for CSV file
csvpath = pathlib.Path("Resources", "budget_data.csv")

# Open and read the CSV
with open(csvpath) as csvfile:
    #print(csvreader)
    
    # Read header row
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")
 
    # Define variables as empty lists
    Months = []
    Total_Profit_Loss = []
    Change = []
    Greatest_Increase_Date = ""
    Greatest_Decrease_Date = ""
    
    # Find the total number of months in the dataset
    for row in csvreader:
        Months.append(row[0])   
        Total_Profit_Loss.append(int(row[1]))
    
    # Find average change between months
    
    for i in range(1, len(Total_Profit_Loss)):
        Difference = (Total_Profit_Loss[i] - Total_Profit_Loss[i-1])
        Change.append(Difference)
        
        # Find average of values
        Average_Change = sum(Change) / len(Change)
        
        # Find the greatest increase with corresponding date
        Greatest_Increase = max(Change)
        Greatest_Increase_Date_index = Change.index(Greatest_Increase) + 1
        Greatest_Increase_Date = Months[Greatest_Increase_Date_index] 
        
        
        # Find the greatest decrease with corresponding date
        Greatest_Decrease = min(Change)
        Greatest_Decrease_Date_index = Change.index(Greatest_Decrease) + 1
        Greatest_Decrease_Date = Months[Greatest_Decrease_Date_index]
    

    # Print Statements
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", len(Months))
    print("Net Total: $", sum(Total_Profit_Loss))
    print("Average Change: $", round(Average_Change, 2))
    print("Greatest Increase in Profits: ", Greatest_Increase_Date, "($", Greatest_Increase,")")
    print("Greatest Decrease in Profits: ", Greatest_Decrease_Date, "($", Greatest_Decrease,")")
        
    # Set the path for output text file
    output_path = pathlib.Path("Resources/PyBank_output.txt")

    # Open the file with write mode
    with open(file=output_path, mode='w', newline='') as txtfile:
        txtfile.write("Financial Analysis: \n")
        txtfile.write("------------------- \n")        
        txtfile.write(f"Total Months: {len(Months)} \n")
        txtfile.write(f"Net Total: $ {sum(Total_Profit_Loss)} \n")
        txtfile.write(f"Average Change: $ {round(Average_Change, 2)} \n")
        txtfile.write(f"Greatest Increase in Profits: {Greatest_Increase_Date}, $ {Greatest_Increase} \n")
        txtfile.write(f"Greatest Decrease in Profits: {Greatest_Increase_Date}, $ {Greatest_Increase}")
        txtfile.close()     
