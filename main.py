# -*- coding: utf-8 -*-

import sys
import csv
import sendEmail
import random
  
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
    random.shuffle(randomKeyOrder)
    
    with open('santa_solution','w') as solutionFile:
        last = len(randomKeyOrder) -1
        for i, key in enumerate(randomKeyOrder):
            solutionFile.write(key + '\n') #keep record of santa list, to reveal at end
            santa = santaDictionary[randomKeyOrder[i]]
            if i == last:
                santee = santaDictionary[randomKeyOrder[0]]
            else:
                santee = santaDictionary[randomKeyOrder[i+1]]
            
            message = sendEmail.constructMessage(santa,santee)
            toEmailAddress = key
            sendEmail.send(toEmailAddress,message)