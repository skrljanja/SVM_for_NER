# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:25:03 2020

@author: skrlj
"""

import json

def nameFile(sourceFilepath, string):
    fileName = string + sourceFilepath
    return fileName

def parseLine(line):
    info_dict = json.loads(line)
    article_dict = info_dict.get("info")
    return article_dict 
            
    
def AddLineToFile(file, dictionary):
    line = (json.dumps(dictionary))
    file.write (line + "\n")
            