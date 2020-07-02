#PyBank script

import os
import csv 

csvpath = os.path.join('..' , 'Resources' , 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',' )
    header = next(csvreader)
    firstRow = next(csvreader)
    print(header)
    print(firstRow)

    totalMonths = 0
    totalProfitLoss = 0
    netChangeList = []
    previousRow = firstRow
    for row in csvreader:
        totalMonths += 1
        totalProfitLoss += int(row[1])
        
        eachChange = int(row[1]) - int(previousRow[1])
        netChangeList.append(eachChange)

    print(netChangeList)
    print(totalMonths)
    print(totalProfitLoss)
    
    
    

    
    
        
    





