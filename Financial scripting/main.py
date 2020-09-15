#PyBank script

import os
import csv 

csvpath = os.path.join('..' , 'Resources' , 'budget_data.csv')
outputPath = os.path.join("..", "Analysis", "outputPyBank.txt")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',' )
    header = next(csvreader)
    
    totalMonths = 0
    totalProfitLoss = 0
    netChangeList = []
    firstRow = next(csvreader)
    previousRow = firstRow[1]
    for row in csvreader:
        totalMonths += 1
        totalProfitLoss += int(row[1])
        #previousValue += int(row[1])
        change = int(row[1]) - int(previousRow)
        previousRow = row[1]
        netChangeList.append(change)

    avgChange = sum(netChangeList) / len(netChangeList)   
    totalMonths += 1 
    totalProfitLoss += int(firstRow[1])
    greatestInc = max(netChangeList)
    greatestDec = min(netChangeList)
    
    
    
    outputText = (f"Financial Analysis\n"
                 f"------------------------\n"
                 f"Total Months: {totalMonths}\n"
                 f"Total: ${totalProfitLoss}\n"
                 f"Average Change: ${avgChange}\n"
                 f"Greatest Increase in Profits: (${greatestInc})\n"
                 f"Greatest Decrease in Profits: (${greatestDec})\n"
                 f"--------------------------")
    print(outputText)

with open(outputPath, 'w') as writerfile: 
    
    textWriter = writerfile.write(outputText)
    
    
    
        
    





