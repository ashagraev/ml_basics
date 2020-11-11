import string
import math
import random

def pWin(r1, r2):
  p1 = 1. / (1. + pow(10, float(r2 - r1) / 400))
  return p1

trueRatings = [2500, 2200, 1900, 1600, 1300]
events = []

def runRound():
  for i in range(len(trueRatings)):
    for j in range(i + 1, len(trueRatings)):
      result = random.random() < pWin(trueRatings[i], trueRatings[j])
      events.append([i, j, result])

for i in range(1000):
  runRound()

ratings = [1600, 1600, 1600, 1600, 1600]

def updateRatings(i, j, result, k):
  p = pWin(ratings[i], ratings[j])
  ratings[i] += k * (result - p)
  ratings[j] -= k * (result - p)

for e in events:
  updateRatings(e[0], e[1], e[2], 100)

print('\n'.join(map(str, ratings)))
