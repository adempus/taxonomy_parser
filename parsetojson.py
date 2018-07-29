'''input data copied locally from: https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt '''

import regex
import json

categoryDict = {}

def inFromFile(inPath):
    ''':param inPath: path to the file being read from.
       :returns a list containing lists of sequentially parsed categories.
    '''
    with open(inPath) as file:
        return file.readlines()


def parseData(contents):
    ''':param contents: a list of lists containing sequentially parsed categories from file. '''
    for cont in contents:
        parsedStr = regex.sub('[0-9].* - ', repl="", string=cont)
        if not '>' in parsedStr:
            parsedStr = parsedStr.strip()
            categoryDict[parsedStr] = {}
        elif '>' in parsedStr:
            splitCats = parsedStr.split('>')
            categorize(categoryDict, splitCats)


def categorize(dic, sequence=list()):
    ''' :param dic: a nested dictionary of categories in categoryDict.
        :param sequence: a list of strings ordered by category from input data.
    '''
    if len(sequence) > 0:
        cat = sequence[0].strip()
        if cat in dic:
            categorize(dic[cat], sequence[1:])
        else:
            dic[cat] = {}


def outToFile(outPath):
    ''':param outPath: path to the file being written to. '''
    with open(outPath, 'w') as file:
        file.write(
            json.dumps(categoryDict, indent=10))


def main():
    contents = inFromFile('./res/taxonomies.txt')
    # print(contents)
    parseData(contents)
    outToFile('./res/jsonOutput.json')


if '__main__'==__name__:
    main()
