import json
import re


def getBody(line):
    info_dict = json.loads(line)
    article_dict = info_dict.get("info")
    article_body = article_dict.get("body")
    return(article_body)

def getTitle(line):
    info_dict = json.loads(line)
    article_dict = info_dict.get("info")
    article_title = article_dict.get("title")
    return(article_title)

def countRegEx(pattern, thestring):
  return re.subn(pattern, '', thestring)[1]

#This is the skeleton for the word counter and the sentence counter 
def countValue(line, seperator, valueName):
    body = getBody(line)
    title = getTitle(line)
    body.strip()
    count = countRegEx(seperator, body)
    print("Number of {0} in '{1}': {2}".format(valueName, title, count))

