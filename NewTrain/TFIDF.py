# -*- coding: utf-8 -*-
"""
This file has functions that calculate the
TF, IDF and TF-IDF of words in a corpus. 

"""

from scipy.sparse import csr_matrix, vstack, hstack
from TFIDFutils import *
import stanza
from math import log
import json
import csv
filepath = "short.txt"

#stanza.download('en')
#nlp = stanza.Pipeline('en')


def TFIDFprepare(filepath, nlp):
    """
    

    Parameters
    ----------
    filepath name of file.
    type is .txt file, where each line contains a token and its features
    nlp : TYPE
        DESCRIPTION.

    Returns
    -------
    doc : a list of list of lemmas.

    """
    text = ""
    with open(filepath) as file :
        for line in file:
            if len(line) > 1:
                line = line.split(" ")
                text += line[0] + " "
            else:
               text += "\n" 
        
        doc = nlp (text)
        doc = doc.to_dict()
        doc = Lemmaise(doc)
    
    return (doc)          
    
    
def TFIDFallwords(lllemmas):
    """
    

    Parameters
    ----------
    lllemmas : list of list of lemmas

    Returns
    -------
    matrixlist : matrix where each row is the TFIDF Matrix for a lemma 
    from the input list.

    """
    i = 0 
    matrixlist = csr_matrix([])
    for list in lllemmas:
        for str in list:
            if i == 0:
                matrixlist = TFIDFword(lllemmas, str, list)
                i = i + 1
            else:
                matrixlist = vstack([matrixlist, TFIDFword(lllemmas, str, list)])
    return matrixlist

def TFIDFallsurroundings(lllemmas):
    """
    

    Parameters
    ----------
    lllemmas : list of list of lemmas

    Returns
    -------
    matrixlist : matrix of the TFIDF row matrices of the surroundings 
    of each lemma

    """
   
    
    surroundings = createSurroundings(lllemmas)
    print (len(surroundings))
    i = 0
    for list in surroundings:
        if i == 0:
            matrixlist = TFIDFsurrounding(lllemmas, list)
            i += 1
        else:
            matrixlist = vstack([matrixlist,TFIDFsurrounding(lllemmas, list)])
    return matrixlist



    

        
        

            
                
            
        