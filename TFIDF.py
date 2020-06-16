# -*- coding: utf-8 -*-
"""
This file has functions that calculate the
TF, IDF and TF-IDF of words in a corpus. 

"""

from anonymiser_utils import parseLine, nameFile
import stanza
from math import log
import json
import csv
filepath = "info.jsonl"

stanza.download('sl')
nlp = stanza.Pipeline('sl')


def Lemmaise(document):
    """
    Converts a list of lists of dictionaries into
    a list of lists of lemmas. 
    """
    newlist = []
    for list in document:
        temp = []
        for dictionary in list:
            temp.append(dictionary["lemma"])
        newlist.append(temp)
    return newlist
            

def IDFlemma(lllemmas, lemma): 
    """Calculates the IDF of a lemma in a given
    list of lists of lemmas."""
    n = len(lllemmas)
    nt = 0 
    for list in lllemmas: 
        if lemma in list:
            nt = nt + 1
    idf = log(n/nt)
    return idf

def IDFlist(lemmas):
    """Given a list of lists of lemmas, this 
    returns the list of all lemmas that appearead
    with their  IDF value in this corpus."""
    appeared = []
    IDFlemmas = []
    for list in lemmas:
        for str in list:
            if str not in appeared:
                IDFlemmas.append([str, IDFlemma(lemmas, str)])
                appeared.append(str)
    return IDFlemmas

def findIDF(IDFs, str):
    """ Given a list containing lemmas with their IDF
    values and a lemma, this returns the IDF corresponding
    to the lemma. 
    """
    for list in IDFs:
        if str in list: 
            return list[1]
    

def TFIDF1(lllemmas):
    """Given a list of lists of lemmas, this function
    returns a list of TF-IDF values in the same order."""
    newLemmas = []
    IDFlemmas = IDFlist(lllemmas)
    for list in lllemmas:
        newList = []
        for str in list:
            TF = list.count(str)/len(list)
            IDF = findIDF(IDFlemmas, str)
            newLemmas.append(TF*IDF)
            value = TF * IDF
    return newLemmas

def TFIDF():
    """This function opens a jsonl file, 
    and transforms it into a list of lists of
    lemmas. It returns a list of TFIDF values
    in the same order. """
    doc = []
    with open(filepath) as file:
        for line in file:
            article_dict = parseLine(line)
            annotatedText = nlp (article_dict.get("body"))
            doc = doc + Lemmaise(annotatedText.to_dict())
    return (TFIDF1(doc))
    


            
        
        

    

        
        

            
                
            
        