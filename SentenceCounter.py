from CountUtils import countValue

def countSentences(line):
    seperator = '.\s[A-Z\u017d]'
    valueName = "sentences"
    countValue (line, seperator, valueName)

with open("article_info_sample.jsonl") as file:
         for line in file:
            countSentences(line)
