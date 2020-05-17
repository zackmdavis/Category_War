import random
from math import factorial

N = 20  # number of agents
n = 50  # experiments per round
ε = .01  # size of edge for B


def binomial(p, n, k):
    return factorial(n)/(factorial(k)*factorial(n-k)) * p**k * (1-p)**(n-k)

def a():
    return random.random() < 0.5

def b():
    return random.random() < 0.5 + ε


def summarize_experiment(results):
    return (len([r for r in results if r]), len(results))


class Agent:
    def __init__(self, initial_credence):
        # credence that B is better
        self.credence = initial_credence

    def __repr__(self):
        return "<Agent credence={}>".format(self.credence)

    def experiment(self):
        if self.credence <= 0.5:
            choice = a
        else:
            choice = b

        results = [choice() for _ in range(n)]
        return results

    def update(self, hits, trials, discount):
        # our beliefs are over two mutually-exclusive and exhaustive
        # hypotheses: "actors are unsure whether the success rate of B is
        # better, p_B = .5 + ε, or worse, p_B = .5 − ε"
        #
        # I'll call the hypotheses H₊ and H₋.
        #
        # Bayes's theorem says
        # P(H₊|E) = P(E|H₊)P(H₊) / P(E|H₊)P(H₊) + P(E|H₋)P(H₋)
        #
        # But P(E|H₊) is a binomial probability
        raw_posterior_good = binomial(0.5 + ε, trials, hits) * self.credence
        raw_posterior_bad = binomial(0.5 - ε, trials, hits) * (1 - self.credence)
        normalizing_factor = raw_posterior_good + raw_posterior_bad
        self.credence = raw_posterior_good / normalizing_factor
        # TODO: discount


def simulation():
    agents = [Agent((1/(N+1))*(i+1)) for i in range(N)]
    print([round(agent.credence, 3) for agent in agents])

    for round_ in range(10):
        experiments = [a.experiment() for a in agents]
        summaries = [summarize_experiment(e) for e in experiments]
        for agent in agents:
            for summary in summaries:
                hits, trials = summary
                agent.update(hits, trials, None)

        print([round(agent.credence, 3) for agent in agents])

simulation()
