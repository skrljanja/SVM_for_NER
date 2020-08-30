# -*- coding: utf-8 -*-
"""

"""


from TFIDF import * 
import sys 
filepath = "short.txt"
#filepath = sys.argv[1]


def isFormName(lemma):
    """
    Parameters
    ----------
    lemma : 

    Returns
    -------
    list
    containing 1 if word is in form [Aaaa..]
    containing 0 if not.

    """
    lemma.split(' ')
    lemma = lemma[0]
    form = lemma[0].isupper()
    i = 1
    while i < len(lemma):
        form = form and lemma[i].islower()
        i = i + 1
    if form == True:
        return [1]
    else:
        return [0]

    
def isFormDoc(doc):
    """
    Parameters
    ----------
    doc : list of list of lemmas

    Returns
    -------
    formList : list of lists that denote whether each of
   the lemmas is in form "Aaaa..."

    """
    #formList = []
    #for lst in doc:
    #    formList = formList + list(map(isFormName, lst))
    #return formList
    i = 0
    isform = list(map(isFormName,doc))
    return isform 

if __name__ == "__main__":
    import stanza
    stanza.download('en')
    nlp = stanza.Pipeline('en', tokenize_pretokenized=True)
    (doc, lemmas, surs) = (TFIDFprepare(filepath, nlp))
    print (lemmas)
    print (isFormDoc(lemmas))
