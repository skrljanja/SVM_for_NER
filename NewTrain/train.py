# -*- coding: utf-8 -*-
"""
clf for CoNLL 03
"""
from parseCoNLL import getFeatures, getLabel
from scipy.sparse import csr_matrix, vstack, hstack
from sklearn import svm
from sklearn.model_selection import cross_validate
#filepath = sys.argv[1]
#anonType = sys.argv[2]
from isform import isFormDoc
from TFIDF import TFIDFprepare, TFIDFallsurroundings, TFIDFallwords
import stanza
stanza.download('en')
nlp = stanza.Pipeline('en', tokenize_pretokenized=True)


if __name__ == "__main__":
    filepath = "short.txt"
    anonType = "LOC"
    i = 0
    doc = TFIDFprepare(filepath, nlp)
    idfwords = TFIDFallwords(doc)
    idfsurroundings = TFIDFallsurroundings(doc)
    print ("TFIDF matrices made!")
    isForm = isFormDoc(doc)
    labelList = []
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
    

    print ("Feature matrices made!")
    
    X=hstack([featuresList, isForm, idfwords, idfsurroundings])
    X = csr_matrix(X)
    print ("Feature matrices joined and Sparsed!")
   
    y = labelList

    clf = svm.SVC(kernel='linear', C=1)
    clf.fit(X, y)
    print ("fit made!")

    scores = cross_validate(clf, X, y, scoring = ['accuracy','f1', 'recall', 'precision'], cv = 5)
    print (scores)
