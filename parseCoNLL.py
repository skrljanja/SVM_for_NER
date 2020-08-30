# -*- coding: utf-8 -*-
"""
conLL numeric parse 

"""
from scipy.sparse import csr_matrix, vstack
import sys
#filepath = sys.argv[1]
#anonType = sys.argv[2]
allUPOS = ['-X-', 'NNP', 'VBZ', 'JJ', 'NN', 'TO', 'VB', '.', 'CD', 'DT', 'VBD', 
'IN', 'PRP', 'NNS', 'VBP', 'MD', 'VBN', 'POS', 'JJR', '"', 'RB', ',', 
'FW', 'CC', 'WDT', '(', ')', ':', 'PRP$', 'RBR', 'VBG', 'EX', 'WP', 
'WRB', '$', 'RP', 'NNPS', 'SYM', 'RBS', 'UH', 'PDT', "''", 'LS', 
'JJS', 'WP$', 'NN|SYM']
emptyUPOS = ['-X-', '.', '"',"''",  '(', ')', ':','$' ]
allChunks = ['O', '-X-', 'B-NP', 'B-VP', 'I-NP', 'I-VP', 'B-PP', 'B-SBAR', 
             'B-ADJP', 'I-ADJP', 'B-ADVP', 'B-PRT', 'B-CONJP', 'I-CONJP', 
             'I-PP', 'B-INTJ','I-ADVP', 'B-LST', 'I-SBAR', 'I-LST', 'I-INTJ',
             'I-PRT']
emptyChunks = ['O', '-X-',]


def getDict(document):
    dictionaries = []
    temp = []
    for line in document:
        line = line.split(" ")
        if len(line) == 4:
            temp.append({ 'word': line[0], 'pos': line[1], 'chunk': line[2], 'ner': line[3]})
            if line[0] == ".":
                dictionaries.append(temp)
                temp = []
        else:
            if len(temp) > 0:
                dictionaries.append(temp)
    return dictionaries


     
        
def getFeatures(line):   
    """

    Parameters
    ----------
    line : a line of tect  containing a word, its UPOS, chunk and named 
    entity tag(in that order)
    .

    Returns
    a csr matrix containing the UPOS and chunk tag of the word (numerised)

    """
    line = line.split(" ")
    UPOS = line [1]
    chunk = line [2]
    if UPOS in emptyUPOS:
        UPOS = 0
    else:
        UPOS = allUPOS.index(UPOS)
    if chunk in emptyChunks:
        chunk = 0
    else:
        chunk = allChunks.index(chunk)
    return csr_matrix([UPOS, chunk])  
    
def getLabel(line, anonType):
    """

    Parameters
    ----------
    line : string
         a line of tect  containing a word, its UPOS, chunk and named 
    entity tag(in that order)
    .
    anonType : string
       a possible named entity tag (LOC, MISC, PER, ORG)

    Returns
    -------
    int
        1 if the line is about a word matching the NE tag, 0 if not

    """
    line = line.split(" ")
    anon = line [3]
    if anonType in anon:
        return 1
    else:
        return 0


    
if __name__ == "__main__":
    filepath = "short.txt"
    anonType = "LOC"
    labelList = []
    i = 0
    with open (filepath) as file: 
        for line in file:
            if i==0:
                featuresList = getFeatures(line)
                labelList.append(getLabel(line, anonType))
                i = i + 1
            else:
                if len(line) > 1:
                    featuresList = vstack([featuresList, getFeatures(line)])
                    labelList.append(getLabel(line, anonType))
            dictionaries = getDict(file)
            print (len(file))
    
    print (dictionaries)
    print (len(dictionaries))
          
    print (featuresList.shape)
    
        