from os import listdir
from os.path import isfile, join
from collections import defaultdict
import string
import matplotlib.pyplot as plt
import math

fullWordsMap = defaultdict(int)

def loadText(path, wordsMap):
  text = open(path).read().lower()
  translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
  text = text.translate(translator)
  words = text.split()
  for word in set(words):
    wordsMap[word] += 1
  return words

def loadTexts(path):
  onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
  texts = []
  wordsMap = defaultdict(int)
  for file in onlyfiles:
    texts.append(loadText(path + '/' + file, wordsMap))
  for k, v in wordsMap.items():
    fullWordsMap[k] += v
  return texts, wordsMap

atheismTexts, atheismWordsMap = loadTexts('C:\\Users\\alex-\\OneDrive\\Desktop\\20newsgroups\\alt.atheism')
baseballTexts, baseballWordsMap = loadTexts('C:\\Users\\alex-\\OneDrive\\Desktop\\20newsgroups\\rec.sport.baseball')
autosTexts, autosWordsMap = loadTexts('C:\\Users\\alex-\\OneDrive\\Desktop\\20newsgroups\\rec.autos')
spaceTexts, spaceWordsMap = loadTexts('C:\\Users\\alex-\\OneDrive\\Desktop\\20newsgroups\\sci.space')
politicsTexts, politicsWordsMap = loadTexts('C:\\Users\\alex-\\OneDrive\\Desktop\\20newsgroups\\talk.politics.guns')
windowsTexts, windowsWordsMap = loadTexts('C:\\Users\\alex-\\OneDrive\\Desktop\\20newsgroups\\comp.windows.x')
medTexts, medWordsMap = loadTexts('C:\\Users\\alex-\\OneDrive\\Desktop\\20newsgroups\\sci.med')

totalDocuments = 0
for k, v in fullWordsMap.items():
  totalDocuments += v

idfMap = defaultdict(float)
for w, v in fullWordsMap.items():
  idf = math.log(float(totalDocuments) / v)
  idfMap[w] = idf

def printWordsTop(wordsMap):
  sortedWords = []
  for w, tf in wordsMap.items():
    tdidf = tf * idfMap[w]
    sortedWords.append([tdidf, w])

  sortedWords.sort(reverse=True)
  for ww in sortedWords[:50]:
    print(ww[0], ww[1])

print('top for atheism:')
printWordsTop(atheismWordsMap)
print('')
print('top for autos:')
printWordsTop(autosWordsMap)
