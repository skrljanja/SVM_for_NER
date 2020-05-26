# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:10:25 2020

@author: skrlj
"""
 
import json

def parseLine(line):
    info_dict = json.loads(line)
    article_dict = info_dict.get("info")
    return article_dict 

def PrettyPrint(title, valueName, count):
    print("Number of {0} in '{1}': {2}".format(valueName, title, count))
    
    
    



