# -*- coding: utf-8 -*-

import sys
import csv
import sendEmail


                
    
if __name__ == '__main__':
    santas = sys.argv[1]

    santaDictionary = {}
    with (open(santas)) as santaFile:
        readSantas = csv.reader(santaFile)
        for row in readSantas:
            name = row[0]
            email = row[1]
            santaDictionary[email] = name
    
    randomKeyOrder = list(santaDictionary.keys())
    with open('santa_solution','w') as solutionFile:
        solutionFile = open('santa_solution','w')
        last = len(randomKeyOrder) -1
        for i, key in enumerate(randomKeyOrder):
            solutionFile.write(key + '\n') #keep record of santa list, to reveal at end
            if i == last:
                santa = santaDictionary[randomKeyOrder[i]]
                santee = santaDictionary[randomKeyOrder[0]]
            else:
                santa = santaDictionary[randomKeyOrder[i]]
                santee = santaDictionary[randomKeyOrder[i+1]]
            
            emailMessage = sendEmail.constructMessage(santa,santee)
                        
            print("santa: " + santa + ", santee: " + santee)
            print(emailMessage)
    print(randomKeyOrder)
    print(list(santaDictionary.values()))