# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:13:18 2020

@author: skrlj
"""

import numpy as np

def loadGloveModel(gloveFile):
    print("Loading Glove Model")
    f = open(gloveFile,'r', encoding="utf8")
    gloveModel = {}
    for line in f:
        splitLines = line.split()
        word = splitLines[0]
        wordEmbedding = np.array([float(value) for value in splitLines[1:]])
        gloveModel[word] = wordEmbedding
    print(len(gloveModel)," words loaded!")
    return gloveModel

def embeddingMatrix(lemmas, glovefile):
    i = 0
    gloveModel = loadGloveModel(glovefile)

    for sentence in lemmas:
        for lemma in sentence:
            lemma.split(' ')
            lemma = lemma[0]
            if i == 0:
                try:
                    embedMat = gloveModel[lemma]
                    i = 1
                except:
                    embedMat = np.zeros((50))
                i = 1
            else:
                try:
                    embedMat = np.vstack([embedMat, gloveModel[lemma]])
                except:
                    embedMat = np.vstack([embedMat, np.zeros((50))])
    return embedMat
            

if __name__ == "__main__":
    glovefile = 'glove.6B.50d.txt'
    lemmas = [['yes', 'no'], ['off', 'EU']]
    print (embeddingMatrix(lemmas, glovefile))