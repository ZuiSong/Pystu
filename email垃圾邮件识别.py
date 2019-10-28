import numpy


def createVocabList(dataSet):
    # 输入单词集合，返回单词表
    vocabSet = set([])  # create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # union of the two sets
    return list(vocabSet)


def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak',
                       'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec


def textParse(bigString):  # input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def wordlist2nummat(docList, vocabList):
    wordnummat = []
    for doc in docList:
        docnummat = [0] * len(vocabList)
        for word in doc:
            if word in vocabList:
                docnummat[vocabList.index(word)] += 1
            else:
                print("the word: '%s' is not in my Vocabulary!" % word)
        wordnummat.append(docnummat)
    return wordnummat


def caluwordpv(wordmat, classList):
    wordnummat = numpy.array(wordmat)
    docnum = len(classList)
    word0count = numpy.array([0] * len(wordmat[0]))
    word1count = numpy.array([0] * len(wordmat[0]))
    word0sum = 0.0
    word1sum = 0.0
    for i in range(docnum):
        if classList[i] == 1:
            word1count += wordnummat[i]
            word1sum += sum(wordnummat[i])
        else:
            word0count += wordnummat[i]
            word0sum += sum(wordnummat[i])
    wordP0 = word0count / word0sum
    wordP1 = word1count / word1sum

    return wordP0, wordP1


def main():
    docList = []
    classList = []
    # fullText = []
    # for i in range(1, 26):
    #     wordList = textParse(open('email/spam/%d.txt' %
    #                               i, encoding='utf-8').read())
    #     docList.append(wordList)
    #     fullText.extend(wordList)
    #     classList.append(1)
    #     wordList = textParse(open('email/ham/%d.txt' %
    #                               i, encoding='utf-8').read())
    #     docList.append(wordList)
    #     fullText.extend(wordList)
    #     classList.append(0)
    docList, classList = loadDataSet()
    vocabList = createVocabList(docList)
    print(vocabList)
    wordmat = wordlist2nummat(docList, vocabList)
    # print(numpy.mat(wordmat))
    wordListP0, wordlistP1 = caluwordpv(wordmat, classList)
    print(wordListP0, '\n', wordlistP1)

    testcontent = ['So stupid']
    splitedcontent = []
    for doc in testcontent:
        spliteddoc = textParse(doc)
        splitedcontent.append(spliteddoc)

    print(splitedcontent)
    contnntnum = wordlist2nummat(splitedcontent, vocabList)
    print(contnntnum)


if __name__ == '__main__':
    main()
