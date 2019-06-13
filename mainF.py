

import os
import csv


trade_csv = os.path.join('budget_data.csv')

with open(trade_csv, "r") as csv_file:
    c1 = []
    #Split the data
    csvreader = csv.reader(csv_file, delimiter=',')
    #Reset
    total = 0
    months = 0
    #File
    header = next(csvreader)
    #Use a For Loop
    for row in csv.reader(csv_file):
       
        c1.append(row[1])
        #Calculate total profit/loss
        total = total + (int(row[1]))
        
        months = months + 1

with open(trade_csv, "r") as csv_file:
   
    csvreader = csv.reader(csv_file, delimiter=',')
    
    header = next(csvreader)
    
    c2 = []
 
    for x, y in zip(c1, c1[1:]):
        
        header = next(csvreader)
        
        c2.append(int(x) - int(y))
        #Calculate the average 
        total_change = sum(c2)
        average = total_change / months

greatest_increase = max(c2)
greatest_decrease = min(c2)


print("Financial Analysis")
print("------------------------")
print("Total months: " + str(months))
print("Total volume: " + str(total))

print("Average monthly change: "+ str(average))

print("Greatest increase: " + str(greatest_increase))

print("Greatest decrease: " + str(greatest_decrease))

##Output to text file
text_file = open("PYBankFinancials.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------\n")
text_file.write("Total months: " + str(months) + "\n")
text_file.write("Total volume: " + str(total) + "\n")
text_file.write("Average monthly change: " + str(average) + "\n")
text_file.write("Greatest increase: " + str(greatest_increase) + "\n")
text_file.write("Greatest decrease: " + str(greatest_decrease) + "\n")
text_file.close()
