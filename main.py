# -*- coding: utf-8 -*-

import sys
import csv

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
        for key in randomKeyOrder:
            solutionFile.write(key + '\n') #keep record of santa list, to reveal at end
    
    print(randomKeyOrder)
    print(list(santaDictionary.values()))