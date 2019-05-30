import random
from math import log2 as lg

def h(distribution):
    return sum(p * lg(1/p) for p in distribution)

def d():
