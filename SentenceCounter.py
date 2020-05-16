from CountUtils import countValue, getTitle, PrettyPrint
import sys 

filepath = sys.argv[1]

""" This function deals with exceptions. (so when an instance of the general 
definition of a separator appears, but isnt used as a separator in that context)"""
def countExceptions(line):
    exceptions = '(npr | prof | Dr | d.d | d.o.o | oz | gdč | g | ga )'
    separator = exceptions + '.\s[A-Z\u017d]'
    valueName = "sentence exceptions"
    return (countValue(line, separator,valueName))

def countSentences(line):
    seperator = '.\s[A-Z\u017d]'
    valueName = "sentences"
    return (countValue (line, seperator, valueName))



with open(filepath) as file:
         for line in file:
            count = countSentences(line) - countExceptions(line)
            PrettyPrint(getTitle(line), "sentences", count)
