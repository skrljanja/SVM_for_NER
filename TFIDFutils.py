from scipy.sparse import csr_matrix, hstack
from math import log
import numpy as np


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

def LemmaiseLIB(document):
    doc = []
    surlist = []
    sentences = []
    dlemmas = []
    lemmas = []
    for lst in document:
        tempdct = []
        templ = [] 
        sentence = ""
        for dictionary in lst:
            tempdct.append(dictionary['lemma'])
            #tempdct = tempdct + " " + dictionary['text']
            temps = ""
            templ = dictionary["lemma"]
            lemmas.append(dictionary["lemma"])
            sentence = sentence + " " + dictionary["lemma"]
            for subdict in lst:
                if (0 < abs(int(dictionary['id']) - int(subdict['id'])) 
                and abs(int(dictionary['id']) - int(subdict['id'])) <= 3):
                    #temps.append(subdict['lemma'])   
                    temps = temps + " " + subdict['lemma']
                if (not dictionary["id"] == subdict['id']
                and dictionary["lemma"] == subdict['lemma']):
                    templ = templ + " " + subdict['lemma']
                else:
                    if not dictionary["id"] == subdict['id']:
                        templ = templ + " " + "."
            surlist.append(temps)
            dlemmas.append(templ)
        doc.append(tempdct)
        sentences.append(sentence)
    return (doc, lemmas, surlist, dlemmas)
            
            
"""def CountVectorizerWord(doc):
    for sentence in doc:
        for word in  """

def IDFdict(lemmas):
    """

    Parameters
    ----------
    lemmas : list of all lemmas (with repetition.)

    Returns
    -------
    IDFlemmas : list of all lemmas that appear in lemmas
    and their respective IDF values in lemmas as the corpus.

    """

    appeared = {}
    IDFlemmas = {}
    i = 0
    sentence_N = len(lemmas)
    for sentence in lemmas:
        sentence = list(dict.fromkeys(sentence))
        for lemma in sentence:
            if lemma not in appeared:
                IDFlemmas[lemma] = {'idf': 0.0, 'index' : i, 'frequency': 1}
                i += 1
                appeared[lemma] = 1
            else:
                IDFlemmas[lemma]['frequency'] += 1 
            
    for lemma in appeared:
        info = IDFlemmas[lemma]
        info['idf'] = log(sentence_N/info['frequency'])
            
    return IDFlemmas


def TFIDFword(lllemmas, lemma, lst, IDFlemmas):
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
    i = 0
    TFIDFmatrix = np.zeros((1, len(IDFlemmas)))
    #TFIDFmatrix = csr_matrix([])
    TF = lst.count(lemma)/len(lst)
    
    IDFdict = IDFlemmas [lemma] 
    TFIDFmatrix [0, IDFdict ['index']] = TF * IDFdict ['idf']
    
    return TFIDFmatrix
            
            
def TFIDFsurrounding(lllemmas, lst, IDFlemmas):
    """
    Parameters
    ----------
    lllemmas : list of list of lemmas
    lst : list that is in lllemmas
    
    Returns
    -------
    TFIDFlist : TFIDF matrix for given list in lllemmas

    """
    TFIDFmatrix = np.zeros((1, len(IDFlemmas)))
    
    for lemma in lst:
        IDFdict = IDFlemmas [lemma] 
        TF = lst.count(lemma)/len(lst)
        TFIDFmatrix [0, IDFdict ['index']] = TF * IDFdict ['idf']
        
    
    #TFIDFmatrix = csr_matrix(TFIDFmatrix)
    return TFIDFmatrix

if __name__ == "__main__":
    import stanza
    stanza.download('en')
    nlp = stanza.Pipeline('en')
    
    text = "You are my fire. The one desire. Belive, when I say. I want it that way want. Hello, Phil."
    
    doc = nlp(text)
    doc = doc.to_dict()
    
    (doc, sentences, surlist, dl) = (LemmaiseLIB(doc))
    
    print (doc)
    print (sentences)
    print (surlist)
    print (dl)