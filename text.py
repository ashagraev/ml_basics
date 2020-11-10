from os import listdir
from os.path import isfile, join
from collections import defaultdict
import string
import matplotlib.pyplot as plt

wordsMap = defaultdict(int)

def loadText(path):
  text = open(path).read().lower()
  translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
  text = text.translate(translator)
  words = filter(None, text.split())
  for word in words:
    wordsMap[word] += 1

path = 'C:\\Users\\alex-\\OneDrive\\Desktop\\20newsgroups\\alt.atheism'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
for file in onlyfiles:
  loadText(path + '/' + file)

sortedWords = []
for w, c in wordsMap.items():
  sortedWords.append([c, w])

sortedWords.sort(reverse=True)
for ww in sortedWords[:10]:
  print(ww[0], ww[1])

x = []
y = []

for i in range(len(sortedWords)):
  x.append(i)
  y.append(sortedWords[i][0])

fig = plt.figure()
fig.set_size_inches(10, 5)
plt.plot(x, y)
plt.show()
    
