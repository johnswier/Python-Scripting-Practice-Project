#PyBank script

import os
import csv 

csvpath = os.path.join('..' , 'Resources' , 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',' )
    header = next(csvreader)
    
    
    

    totalMonths = 0
    totalProfitLoss = 0
    netChangeList = []
    previousValue = 0
    for row in csvreader:
        totalMonths += 1
        totalProfitLoss += int(row[1])
        #previousValue = 
        #eachChange = 
        #netChangeList.append(eachChange)


    print(netChangeList)
    print(totalMonths)
    print(totalProfitLoss)
    
    
    

    
    
        
    





