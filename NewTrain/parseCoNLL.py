# -*- coding: utf-8 -*-
"""
conLL num parse

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


        
        
def getFeatures(line):     
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
          
    print (featuresList.shape)
        