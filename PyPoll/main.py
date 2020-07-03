#PyPoll script

import os
import csv

csvPath = os.path.join("..", "Resources", "election_data.csv")

candidateDict = {}

with open(csvPath) as csvFile:

    csvReader = csv.DictReader(csvFile)
    print("Election results")
    print("------------------------")
    totalVotes = 0
    for row in csvReader:
        totalVotes += 1
        candidate = row['Candidate']
        if candidate not in candidateDict.keys():
            candidateDict[candidate] = 0
        candidateDict[candidate] += 1
    print("Total Votes:" + " " + str(totalVotes))
    print("-------------------------")
    for i in candidateDict:
        percentVotes = round(((candidateDict[i]) / totalVotes)*100,5)
        print(i + ":" + " " + str(percentVotes) + "%" + " " + 
            str((candidateDict[i])))
    print("-------------------------")   

    mostVotes = max(candidateDict["Khan"], candidateDict["Correy"], 
                candidateDict["Li"], candidateDict["O'Tooley"])

    winner = list(candidateDict.keys())[list(candidateDict.values())
                .index(mostVotes)]
    
    print("Winner:" + " " + winner)


electionText = (f"Winner: + " " + winner")

with open(electionText, 'w') as writerfile:
    writerfile.write(electionText)

    
    
    
    
    
    
    
    #other method....
    

    # totalVotes = 0
    # candidateList = []
    # Khan = 0
    # Correy = 0
    # Li = 0
    # Tooley = 0
    # for row in csvReader: 
    #     totalVotes += 1 
    #     if row[2] not in candidateList: 
    #         candidateList.append(row[2])
    
    #     if row[2] == candidateList[0]:
    #         Khan += 1
    #     elif row[2] == candidateList[1]:
    #         Correy += 1
    #     elif row[2] == candidateList[2]:
    #         Li += 1
    #     elif row[2] == candidateList[3]:
    #         Tooley += 1
    
    # percentKhan = round(((Khan / totalVotes) * 100 ), 5)
    # percentCorrey = round(((Correy / totalVotes) * 100), 5) 
    # percentLi = round(((Li / totalVotes)*100),5)
    # percentTooley = round(((Tooley / totalVotes)*100),5)

    # mostVotes = max([Khan, Correy, Li, Tooley])

        
        


