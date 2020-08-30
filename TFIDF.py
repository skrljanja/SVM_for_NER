# -*- coding: utf-8 -*-
"""
This file has functions that calculate the
TF, IDF and TF-IDF of words in a corpus. 

"""
import numpy as np
from scipy.sparse import csr_matrix, vstack, hstack
from TFIDFutils import TFIDFword, TFIDFsurrounding, IDFdict, LemmaiseLIB


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
        #doc = Lemmaise(doc)
        (dct, sentences, surlist, dl) = LemmaiseLIB(doc)
    
    #return (doc)
    return (dct, sentences, surlist, dl)   
    
    
def TFIDFmakematrices(lllemmas):
    """
    

    Parameters
    ----------
    lllemmas : list of lists of lemmas

    Returns
    -------
    wordmatrix : csr matrix
        tf-idf matrix for each lemma (each row is a lemma)
    slist : csr matrix
        tf-idf matrix for the surroundings of each lemma
    """
    i = 0
    IDFlemmas = IDFdict(lllemmas)
    for list in lllemmas:
        for lemma in list:
            id = list.index(lemma)
            if id > 3:
                lemmalist = list[id-3:id+3]
            else:
                lemmalist = list[0:id+3]
            if i == 0:
                wordmatrix = TFIDFword(lllemmas, lemma, list, IDFlemmas)
                smatrix = TFIDFsurrounding(lllemmas, lemmalist, IDFlemmas)
                i += 1 
            else:
                wordmatrix = np.vstack([wordmatrix, TFIDFword(lllemmas, lemma, list,IDFlemmas)])
                smatrix = np.vstack([smatrix,TFIDFsurrounding(lllemmas, lemmalist, IDFlemmas)])
    print ("TFIDF matrices made!")
    return (csr_matrix(wordmatrix), csr_matrix(smatrix))


if __name__ == "__main__":
    import stanza
    filepath = "short.txt"
    stanza.download('en')
    nlp = stanza.Pipeline('en')
    doc, lemmas, s, dl = TFIDFprepare(filepath, nlp)
    
    print (doc, lemmas, s, dl)
    print (TFIDFmakematrices(doc)[1])


    

        
        

            
                
            
        