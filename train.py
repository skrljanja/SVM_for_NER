# -*- coding: utf-8 -*-
"""
clf for CoNLL 03

"""
from sklearn import svm
from scipy.sparse import csr_matrix, vstack, hstack
from parseCoNLL import getFeatures, getLabel
from sklearn.model_selection import cross_validate
from isform import isFormDoc
from TFIDF import TFIDFprepare
from sklearn.feature_extraction.text import TfidfVectorizer
from glover import embeddingMatrix
from RobertaEmbedding import makeEmbedMatrix
import stanza
stanza.download('en')
nlp = stanza.Pipeline('en', tokenize_pretokenized=True)


if __name__ == "__main__":
    filepath = "train.txt"
    anonType = "MISC"
    i = 0
    (doc, sentences, surlist, dl) = TFIDFprepare(filepath, nlp)
    print(doc)
    EmbeddingMat = embeddingMatrix(doc, 'glove.6B.50d.txt')
    #EmbeddingMat = makeEmbedMatrix(doc)
    transformer = TfidfVectorizer()
    (idfwords, idfsurroundings) = (transformer.fit_transform(dl), transformer.fit_transform(surlist))
    isForm = isFormDoc(sentences)
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
    
    X=hstack([featuresList, isForm, idfwords, idfsurroundings, EmbeddingMat])
    X = csr_matrix(X)
    print ("Feature matrices joined and Sparsed!")
   
    y = labelList

    clf = svm.SVC(kernel='linear', C=1)

    scores = cross_validate(clf, X, y, scoring = ['accuracy','f1', 'recall', 'precision'], cv = 5)
    print (scores)
