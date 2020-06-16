# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:35:19 2020

@author: skrlj
"""

from TFIDF import TFIDF
import csv

def featuresCSV():
    """reads the file with numerised data and the list containing
    the tfidf and joins them into one matrix, which it then returns."""
    featsList = []
    i = 0
    with open('newdata.csv', newline='') as csvfile:
        readerdata = csv.reader(csvfile, delimiter=' ', quotechar='|')
        tfidf = TFIDF()
        next(csvfile)
        for row in readerdata:
            if len(row) == 1:
                iris = row[0].split(",")
                iris = list(map(float, iris))
               # iris.append(tfidf[i])
                featsList.append(iris)
                i = i + 1
            else:
                break
    return featsList

def labelsCSV():
    """reads the file containing the isTime label for each token 
    and returns it as a list."""
    labelList=[]
    with open('time_binary.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            if len(row) == 1:
                labelList.append(row[0])
            else:
                break
    return labelList


    

                
    
            
            
    