from os import listdir
import string
import math

def pWin(r1, r2):
  p1 = 1. / (1. + pow(10, float(r2 - r1) / 400))
  return p1, 1 - p1

print(pWin(1000, 1000))
print(pWin(1400, 1000))
print(pWin(1800, 1400))
print(pWin(200, -200))
