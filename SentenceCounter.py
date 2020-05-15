from CountUtils import countValue
import sys 

filepath = sys.argv[1]

def countSentences(line):
    seperator = '.\s[A-Z\u017d]'
    valueName = "sentences"
    countValue (line, seperator, valueName)

with open(filepath) as file:
         for line in file:
            countSentences(line)
