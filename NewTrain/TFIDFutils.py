from scipy.sparse import csr_matrix, hstack
from math import log


def Lemmaise(document):
    """
    
    Parameters
    ----------
    document : a list of lists of dictionaries (this
    is how stanza annotated texts are stored)

    Returns
    -------
    newlist : a list of lists (sentences) of lemmas. 

    """

    newlist = []
    for list in document:
        temp = []
        for dictionary in list:
            temp.append(dictionary["lemma"])
        newlist.append(temp)
    return newlist
            

def IDFlemma(lllemmas, lemma): 

    """
    Calculates the IDF of a lemma in a given
    list of lists of lemmas.
    """
    n = len(lllemmas)
    nt = 0 
    for list in lllemmas: 
        if lemma in list:
            nt = nt + 1
    idf = log(n/nt)
    return idf

def IDFlist(lemmas):
    """Given a list of lists of lemmas, this 
    returns the list of all lemmas that appearead
    with their  IDF value in this corpus."""
    appeared = []
    IDFlemmas = []
    for list in lemmas:
        for str in list:
            if str not in appeared:
                IDFlemmas.append([str, IDFlemma(lemmas, str)])
                appeared.append(str)
    return IDFlemmas

def findIDF(IDFs, str):
    """
    
    Parameters
    ----------
    IDFs : a list containing lemmas with their IDF
    values
    str : a lemma

    Returns
    -------
    the IDF corresponding
    to the lemma. 

    """
    for list in IDFs:
        if str in list: 
            return list[1]


def TFIDFword(lllemmas, lemma, lst):
    """
    

    Parameters
    ----------
    lllemmas : list of list of lemmas
    lst : a list of lemmas, contained in the lemma
    lemma : a lemma contained in the list

    Returns
    -------
    TFIDFmatrix : the TFIDF matrix (1 row) where the document
    is a word and thecorupus is all the lemmas in lllemmas
    """

    TFIDFmatrix = csr_matrix([])
    IDFlemmas = IDFlist(lllemmas)
    TF = lst.count(lemma)/len(lst)
    for elem in IDFlemmas:
            if (elem[0]) == lemma: 
                if elem[1] > 0.4: 
                    TFIDFmatrix = hstack([TFIDFmatrix, elem[1]*TF])
                else:
                  TFIDFmatrix = hstack([TFIDFmatrix, [0]])
            else:
                TFIDFlist = hstack([TFIDFmatrix, [0]])
    return TFIDFlist

def createSurroundings(lllemmas):
    """

    Parameters
    ----------
    lllemmas : A list of list of lemmas

    Returns
    -------
    surroundings : a list of each lemmas surrounding words  
    (3 in front and 3 after, not counting those belonging to a 
    different sentence.) 

    """

    surroundings = []
    for list in lllemmas:
        for lemma in list:
            id = list.index(lemma)
            if id > 2:
                lemmalist = list[id-3:id+3]
            else:
                lemmalist = list[0:id+3]
            surroundings.append(lemmalist)
    return surroundings
            
            
def TFIDFsurrounding(lllemmas, lst):
    """
    Parameters
    ----------
    lllemmas : list of list of lemmas
    lst : list that is in lllemmas
    
    Returns
    -------
    TFIDFlist : TFIDF matrix for given list in lllemmas

    """
    
    TFIDFlist = []
    IDFlemmas = IDFlist(lllemmas)
    for elem in IDFlemmas:
        if (elem[0]) in lst: 
            TF = lst.count(elem[0])/len(lst)
            TFIDFlist.append(elem[1]*TF)
        else:
            TFIDFlist.append(0)
    TFIDFlist = csr_matrix(TFIDFlist)
    return TFIDFlist
