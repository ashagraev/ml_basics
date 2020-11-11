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

def themeTFIDF(wordsMap):
  themeTFIDF = defaultdict(float)
  for w, tf in wordsMap.items():
    tdidf = tf * idfMap[w]
    themeTFIDF[w] = tdidf
  return themeTFIDF

def score(doc, tfidf):
  return sum([tfidf[w] for w in doc]) / len(doc)

atheismTFIDF = themeTFIDF(atheismWordsMap)
autosTFIDF = themeTFIDF(autosWordsMap)

scores = []
for d in atheismTexts:
  scores.append([score(d, atheismTFIDF), 1])
for d in autosTexts:
  scores.append([score(d, atheismTFIDF), 0])

scores.sort(reverse=True)

def qualityMetrics(count):
  tp = 0
  t = 0
  for i in range(count):
    tp += scores[i][1]
    t += 1

  precision = float(tp) / t
  recall = float(tp) / len(atheismTexts)

  return precision, recall

print("Precision & recall @ 10%:")
print(qualityMetrics(int(len(scores) / 10)))

x = []
y = []

for i in range(10):
  p, r = qualityMetrics(int(len(scores) * (i + 1) / 11))
  x.append(p)
  y.append(r)

fig = plt.figure()
fig.set_size_inches(10, 5)
plt.plot(x, y)
plt.show()
