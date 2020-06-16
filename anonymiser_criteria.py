# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:25:24 2020

@author: skrlj
"""
import re
import csv

def MatchesRegEx(pattern, string):
    """Returns true if a regular expression pattern matches a string"""
    p = re.compile(pattern)
    isMatch = p.fullmatch(string)
    return isMatch

def listContainsLemma(lemma, l):
    """"Returns true if a list (sentence) contains a lemma"""
    contains = False
    for dictionary in  l:
        if dictionary.get("lemma") == lemma:
            contains = True
    return contains

def isAbove (dictionary, lemmas, l):
    """Return true if one of the input lemmas is
    above the observed word in the dependancy tree
    of the sentence. Otherwise return false."""
    above = False
    id = dictionary.get("head")
    while id != 0:
        head = l[id -1]
        if head.get("lemma") in lemmas:
            above = True
            break
        else:
            id = head.get("head")
    return above
            
def isBelow(dictionary1, lemma, l):
    """Return true if one of the input lemmas is
    below the observed word in the dependancy tree
    of the sentence. Otherwise return false."""
    below = False
    for dictionary in  l:
        if (dictionary.get("lemma") == lemma and
            dictionary.get("head") == dictionary1.get("id")):
            below = True
    return below

def SameHead(dictionary1, lemma, l):
    """Return true if the observed word and a word
    with the input lemma have the same head in the
    dependancy tree."""
    sameHead = False 
    for dictionary in  l:
        if (dictionary.get("lemma") == lemma):
            if dictionary.get("head") == dictionary1.get("head"):
                sameHead = True
    return sameHead



def isForm(lemma):
    """Return true if a lemma is of the form corresponding to
    a date (00.00.0000 or 00/00/0000)"""
    return MatchesRegEx('[0-9]{1,2}[./][0,9]{1,2}[./][0-9]{2,4}', lemma)

def isNum(dictionary):
    """Return true if the "upos" value is "NUM"""
    return dictionary.get("upos") == "NUM"

        
def isMonth(lemma):
    """Return true if the input lemma corresponds to a month"""
    month = 'januar|februar|marec|april|maj|junij|julij|avgust|september|november|december'
    return MatchesRegEx(month, lemma)

    

## time crit 
def isTime(dictionary, l):
    """Combines the criteria for Time, to determine whether 
    the word is expected to denote time or not."""
    month = 'januar|februar|marec|april|maj|junij|julij|avgust|september|november|december'
    months = ["januar", "februar", "marec", "april","maj", "junij", "julij", "avgust", "september", "november", "december"]
    isMonth = MatchesRegEx(month, dictionary.get("lemma"))
    isHour1 = (dictionary.get("upos") == "NUM" and
              dictionary.get("deprel") == "nummond" and
              dictionary.get("xpos") == "Mlc-pn" and
              "NumType=Card" in dictionary.get("feats"))
    isHour2 = (dictionary.get("xpos") == "Mdc" and
               dictionary.get("upos") == "NUM" and
               "NumType=Card" in dictionary.get("feats"))
    if isHour1 or isHour2:
        if not (isBelow(dictionary, "ob", l) or SameHead(dictionary, "ob", l) or
        isAbove(dictionary, ["ura", "leto"], l) or isAbove(dictionary, months, l)):
            isHour1 = False
            isHour2 = False
    form = isForm(dictionary.get("lemma"))
    return (isHour1 or isHour2 or isMonth or form)
    

def PROPN(dictionary):
    propn = dictionary.get("upos") == "PROPN"
    return propn



def Anonymiser(AnnotatedText, labelsFile, wordsFile):
    """Creates two files. One is a csv file containing the values of
    isTime for each token (time_binary.csv). The other is a csv
    file (words.csv) containing all the tokens in the document, 
    those denoting time marked with "__". This makes it easier 
    to spot and fix mistakes the program has made, so that 
    when we use this data to teach a classifier, it is not 
    taught from faulty data"""
    newText = ""
    YesNo = []
    f = open(wordsFile, "a", newline = '')
    wordwrite = csv.writer(f)
    csvfile = open(labelsFile, "a", newline = '')   
    labelwrite = csv.writer(csvfile)
    for list in AnnotatedText:
        for dict in list:
            if isTime(dict, list):
                dict["text"] = dict["text"] + "__"
                labelwrite.writerow("1")
                wordwrite.writerow([dict["text"] ])
            else:
                labelwrite.writerow("0")
                wordwrite.writerow([dict["text"]])
          #  if PROPN(dictionary):
            #    dictionary["text"] = dictionary["text"] + "_"
            newText = newText + dict["text"] + " "
    return newText

                
    
