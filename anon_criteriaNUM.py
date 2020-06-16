# -*- coding: utf-8 -*-
"""
This file contains similar functions as anonymiser_criteria,
but they all return numbers, instead of boolean values. 

"""
import re

def MatchesRegEx(pattern, string):
    p = re.compile(pattern)
    isMatch = p.fullmatch(string)
    return isMatch

def isAboveNUM(head, lemmas, l): 
    above = 0
    id = head
    while id != 0:
        head = l[id -1]
        if head.get("lemma") in lemmas:
            above = 1
            break
        else:
            id = head.get("head")
    return above

def isBelowNUM(id, lemma, l):
    below = 0
    for dictionary in  l:
        if (dictionary.get("lemma") == lemma and
            dictionary.get("head") == id):
            below = 1
    return below

def SameHeadNUM(head, lemma, l):
    sameHead = 0 
    for dictionary in  l:
        if (dictionary.get("lemma") == lemma):
            if dictionary.get("head") == head:
                sameHead = 1
    return sameHead

def numeriseXPOS(XPOS):
    if XPOS == "Mlc-pn":
        return 1
    else:
        if XPOS == "Mdc":
            return 2
        else:
            return 0
        
def isMonth(lemma):
    month = 'januar|februar|marec|april|maj|junij|julij|avgust|september|november|december'
    if MatchesRegEx(month, lemma):
        return 1
    else: 
        return 0
    
def isForm(lemma):
    if MatchesRegEx('[0-9]{1,2}[./][0,9]{1,2}[./][0-9]{4,4}', lemma):
        return 1
    else:
        return 0

def isNum(UPOS):
    if UPOS == "NUM":
        return 1
    else:
        return 0
    
