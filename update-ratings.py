import string
import math
import random

def pWin(r1, r2):
  p1 = 1. / (1. + pow(10, float(r2 - r1) / 400))
  return p1

ratings = [2500, 2200, 1900, 1600, 1300]

def updateRatings(i, j, result, k):
  p = pWin(ratings[i], ratings[j])
  ratings[i] += k * (result - p)
  ratings[j] -= k * (result - p)

print('\n'.join(map(str, ratings)))
print('')

updateRatings(0, 1, 1, 10)
print('\n'.join(map(str, ratings)))
print('')

updateRatings(0, 1, 1, 10)
print('\n'.join(map(str, ratings)))
print('')

updateRatings(0, 1, 1, 10)
print('\n'.join(map(str, ratings)))
print('')

updateRatings(0, 4, 0, 10)
print('\n'.join(map(str, ratings)))
print('')

updateRatings(0, 4, 0, 10)
print('\n'.join(map(str, ratings)))
print('')
