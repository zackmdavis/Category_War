import logging
import random
from math import log2 as lg

def h(distribution):
    return sum(p * lg(1/p) for p in distribution)

p_a = [1/4, 7/16, 1/4, 1/16]
p_b = [1/16, 1/4, 7/16, 1/4]

h_a = h(p_a)
h_b = h(p_b)

def a():
    return random.sample([1]*4 + [2]*7 + [3]*4 + [4], 1)[0]

def b():
    return random.sample([1] + [2]*4 + [3]*7 + [1]*4, 1)[0]

def odds_to_probability(o):
    return o/(1+o)

def probability_to_odds(p):
    return p/(1-p)

def tally_likelihood(xs, a_dist, b_dist):
    r = 1
    for x in xs:
        n = a_dist[x-1]/b_dist[x-1]
        logging.info("x = %s, likelihood ratio is %s", x, n)
        r *= n
    return r
