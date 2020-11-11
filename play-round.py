import string
import math
import random

def pWin(r1, r2):
  p1 = 1. / (1. + pow(10, float(r2 - r1) / 400))
  return p1

ratings = [2500, 2200, 1900, 1600, 1300]
wins = [0, 0, 0, 0, 0]

def runRound():
  for i in range(len(ratings)):
    for j in range(i + 1, len(ratings)):
      if random.random() < pWin(ratings[i], ratings[j]):
        wins[i] += 1
      else:
        wins[j] += 1

for i in range(1000):
  runRound()

print('\n'.join(map(str, wins)))
