# -*- coding: utf-8 -*-
"""
creates CVS file where every row gives numerical
data representing data about a token. 
"""
from anonymiser_utils import *
from anon_criteriaNUM import *
from TFIDF import *
import csv
#import sys

#filepath = sys.argv[1]



# csv framework

def makeList(dictionaries):
    """
    This function takes a list of stanza dictionaries and 
    returns a list of numbers which represent information
    about said dictionaries.
    """
    newLemmas = []
    for list in dictionaries:
        for dictionary in list: 
            head = dictionary.get("head")
            lemma = dictionary.get("lemma")
            id = dictionary.get("id")
            upos = dictionary.get("upos")
            xpos = dictionary.get("xpos")
            
            Newlist = [isAboveNUM(head,["ura", "leto"], list),
                       isBelowNUM(id, ["ob"], list),
                       SameHeadNUM(head, ["ob"], list),
                       isMonth(lemma),
                       numeriseXPOS(xpos),
                       isNum(upos),
                       isForm(lemma)
                       ]
            newLemmas.append(Newlist) 
    return newLemmas
    
def makeDictionaries(jsonlfile):
    """
    Takes a jsonl file and returns only the content
    under the body tag of each line. 
    """
    document = []
    with open(jsonlfile) as file:
        for line in file:
            article_dict = parseLine(line)
            text = article_dict.get("body")
            document = document + nlp(text).to_dict()
    return document
            
def CVSframe(filepath):    
    dicts = makeDictionaries(filepath)
    listic = makeList(dicts)

    header =["isAbove", 
             "isBelow", 
             "SameHead", 
             "isMonth", 
             "numeriseXPOS", 
             "isNum", 
             "isForm"]
    with open("newdata.csv", "w", newline='') as csvfile:
        write = csv.writer(csvfile)
        write.writerow(header)
        for value in listic:
            write.writerow(value)
    


