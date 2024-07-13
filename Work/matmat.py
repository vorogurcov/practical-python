#math.py

from collections import Counter

def mam(n):
  symbols_info = Counter()
  for symb in n:
    symbols_info[symb] +=1
  return symbols_info