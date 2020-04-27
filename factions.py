import random

N = 20
n = 50
ε = .01

def a():
    return random.random() < 0.5

def b():
    return random.random() < 0.5 + ε


class Agent:
    def __init__(self, initial_credence):
        # credence that B is better
        self.credence = initial_credence

    def experiment(self):
        if self.credence >= 0.5:
            choice = a
        else:
            choice = b

        results = [choice() for _ in range(n)]
