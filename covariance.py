import logging
import random
from math import log2 as lg

logging.basicConfig(level=logging.INFO)

def h(distribution):
    return sum(p * lg(1/p) for p in distribution)

p_a = [1/4, 7/16, 1/4, 1/16]
p_b = [1/16, 1/4, 7/16, 1/4]

h_a = h(p_a)
h_b = h(p_b)

def a():
    return random.sample(
        [1]*4 +  # 1/4
        [2]*7 +  # 7/16
        [3]*4 +  # 1/4
        [4],     # 1/16
        1
    )[0]

def b():
    return random.sample([1] + [2]*4 + [3]*7 + [1]*4, 1)[0]

def odds_to_probability(o):
    return o/(1+o)

def probability_to_odds(p):
    return p/(1-p)

def tally_likelihoods(x, p_a, p_b):
    total_odds = 1
    for i, x_i in enumerate(x, start=1):
        lr = p_a[x_i-1]/p_b[x_i-1]  # (-1s because of zero-based array indexing)
        logging.info("x_%s = %s, likelihood ratio is %s", i, x_i, lr)
        total_odds *= lr
    return total_odds

x = [a() for _ in range(40)]
print(x)
print(
    odds_to_probability(
        tally_likelihoods(
            x,
            [1/4, 7/16, 1/4, 1/16],
            [1/16, 1/4, 7/16, 1/4]
        )
    )
)
