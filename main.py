# -*- coding: utf-8 -*-

import sys
import csv

if __name__ == '__main__':
    csvfile = sys.argv[1]
    print(csvfile)
    readCSV = csv.reader(open(csvfile))
    santaDictionary = {}
    for row in readCSV:
        name = row[0]
        email = row[1]
        santaDictionary[email] = name
    
    print(list(santaDictionary.keys()))
    print(list(santaDictionary.values()))