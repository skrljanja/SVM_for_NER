from CountUtils import countValue, getTitle, PrettyPrint
import sys 

filepath = sys.argv[1]

def countWords(line):
    seperator = '\s+'
    valueName = "words"
    return (countValue (line, seperator, valueName))


with open(filepath) as file:
         for line in file:
            count = countWords(line)
            PrettyPrint(getTitle, "words", count)
