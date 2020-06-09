# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:44:20 2020

@author: skrlj
"""

import stanza
import sys
from anonymiser_utils import nameFile, parseLine, AddLineToFile
from anonymiser_criteria import Anonymiser


stanza.download('sl')
nlp = stanza.Pipeline('sl')
sourceFilepath = sys.argv[1]


            
if __name__ == "__main__":
    f = open(nameFile(sourceFilepath), "w+")
    t = open("time_binary.txt", "w+")
    with open(sourceFilepath) as file:
        for line in file:
            article_dict = parseLine(line)
            annotatedText = nlp (article_dict.get("body"))
            textDict = annotatedText.to_dict()
            anonymisedDicts = Anonymiser(textDict, t)
            article_dict["body"] = anonymisedDicts
            AddLineToFile(f, article_dict)
            
            


