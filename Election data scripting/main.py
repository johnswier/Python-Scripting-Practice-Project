#PyPoll script
import os
import csv

csvPath = os.path.join("..", "Resources", "election_data.csv")
outputPath = os.path.join("..", "Analysis", "outputPyPoll.txt")

with open(csvPath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    
    totalVotes = 0
    candidateDict = {}
    for row in csvReader:
        totalVotes += 1
        candidate = row['Candidate']
        if candidate not in candidateDict.keys():
            candidateDict[candidate] = 0
        candidateDict[candidate] += 1
    
    print(f"Election results\n"
          f"--------------------------\n") 
    print(f"Total Votes: {totalVotes}\n")
    print(f"--------------------------\n")
    
    for i in candidateDict:
        percentVotes = round(((candidateDict[i]) / totalVotes)*100,3)
        eachCandidate = (i + ":" + " " + str(percentVotes) + "%" + " " + 
            "(" + str((candidateDict[i])) + ")")
        print(eachCandidate)
    mostVotes = max(candidateDict["Khan"], candidateDict["Correy"], 
                candidateDict["Li"], candidateDict["O'Tooley"])

    winner = list(candidateDict.keys())[list(candidateDict.values())
                .index(mostVotes)]
    
    
    electionText1 = (f"--------------------------\n"
                    f"\n\nWinner: {winner}\n"
                    f"--------------------------\n")
    print(electionText1)                
    
    
with open(outputPath, 'w') as writerfile:
    electionText2 = (f"Election results\n"
                    f"--------------------------\n" 
                    f"Total Votes: {totalVotes}\n"
                    f"--------------------------\n")
    writerfile.write(electionText2)

    for i in candidateDict:
        candidateName = i
        candidatePercent = round(((candidateDict[i]) / totalVotes)*100,3)
        candidateVote = candidateDict[i]

        candidateText = (f"{candidateName}: {candidatePercent}% ({candidateVote})\n")
    

        writerfile.write(candidateText)
    
    writerfile.write(electionText1)
        
        


