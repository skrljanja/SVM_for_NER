# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:25:24 2020

@author: skrlj
"""
import re

def containsRegEx(pattern, string) :
    p = re.compile(pattern)
    isContained = re.subn(p, '', string)[1] == 1
    return isContained

def listContainsLemma(lemma, l):
    contains = False
    for dictionary in  l:
        if dictionary.get("lemma") == lemma:
            contains = True
    return contains

def isAbove (dictionary, lemmas, l):
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
    below = False
    for dictionary in  l:
        if (dictionary.get("lemma") == lemma and
            dictionary.get("head") == dictionary1.get("id")):
            below = True
    return below

def SameHead(dictionary1, lemma, l):
    sameHead = False 
    for dictionary in  l:
        if (dictionary.get("lemma") == lemma):
            if dictionary.get("head") == dictionary1.get("head"):
                sameHead = True
    return sameHead
    
        
## time crit 
def isTime(dictionary, l):
    month = 'januar|februar|marec|april|maj|junij|julij|avgust|september|november|december'
    months = ["januar", "februar", "marec", "april","maj", "junij", "julij", "avgust", "september", "november", "december"]
    isMonth = containsRegEx(month, dictionary.get("lemma"))
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

    return (isHour1 or isHour2 or isMonth)
    


def PROPN(dictionary):
    propn = dictionary.get("upos") == "PROPN"
    return propn


def Anonymiser(AnnotatedText, file):
    newText = ""
    YesNo = []
    for list in AnnotatedText:
        for dict in list:
            if isTime(dict, list):
                dict["text"] = dict["text"] + "*"
                YesNo.append("1")
            else:
                YesNo.append("0")
          #  if PROPN(dictionary):
            #    dictionary["text"] = dictionary["text"] + "_"
            newText = newText + dict["text"] + " "
    file.write(" ".join(YesNo) + "\n")
    return newText

                
    
