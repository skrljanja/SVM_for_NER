# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:19:03 2020

@author: skrlj
"""


import stanza 
from stanza_CounterUtils import PrettyPrint, parseLine 
import sys

stanza.download('sl')
nlp = stanza.Pipeline('sl')
filepath = sys.argv[1]
value = sys.argv[2]


if __name__ == "__main__":
    with open(filepath) as file:
        if (value == "words"):
            for line in file:
                article_dict = parseLine(line)
                doc = nlp (article_dict.get("body"))
                count = doc.num_words
                PrettyPrint(article_dict.get("title") , value, count) 
        else: 
            if (value == 'sentences'):
                for line in file:
                    article_dict = parseLine(line)
                    doc = nlp (article_dict.get("body"))
                    count = len(doc.sentences)
                    PrettyPrint(article_dict.get("title") , value, count) 
            else: 
                print("invalid value argument.")
                print (value)