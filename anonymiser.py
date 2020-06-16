# -*- coding: utf-8 -*-

"""This file constructs the files that the SVM classifier
will be modelled on."""

import csv
import stanza
import sys
from anonymiser_utils import parseLine, AddLineToFile
from anonymiser_criteria import Anonymiser



"""
stanza.download('sl')
nlp = stanza.Pipeline('sl')
sourceFilepath = sys.argv[1]
"""

            
def anonymiser(filepath, nlp):
    f = open("anonymiser.csv", "w", newline = '')
    writer = csv.writer(f)
    t = "time_binary.csv"
    with open(filepath) as file:
        for line in file:
            article_dict = parseLine(line)
            annotatedText = nlp (article_dict.get("body"))
            textDict = annotatedText.to_dict()
            anonymisedDicts = Anonymiser(textDict, t, "words.csv")
            article_dict["body"] = anonymisedDicts
            AddLineToFile(f, article_dict)
            


