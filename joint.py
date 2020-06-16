# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:07:29 2020

@author: skrlj
"""

import os
import sys
import stanza 

stanza.download('sl')
nlp = stanza.Pipeline('sl')
filepath = sys.argv[1]


if os.path.exists("time_binary.csv"):
  os.remove("time_binary.csv")
else:
  print("The file does not exist")
if os.path.exists("newdata.csv"):
  os.remove("newdata.csv")
else:
  print("The file does not exist")
if os.path.exists("words.csv"):
  os.remove("words.csv")
else:
  print("The file does not exist")


from CVSframe import CVSframe
from anonymiser import anonymiser
from clf import clf

CVSframe(filepath)
anonymiser(filepath, nlp)
""" between these two steps the time_binary file needs to be
checked using the words.csv file, so as to ensure the SVM
model isnt taught with faulty data. 
"""
clf()
