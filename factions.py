import random

from math import factorial, floor

N = 100  # number of agents
n = 50  # experiments per round
ε = .005  # size of edge for B
m = 1  # mistrust factor

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
        results = [b() for _ in range(n)]
        return results

    def discount_factor(self, reporter_credence):
        # let me try a simpler function than the paper
        return min(1, 2*abs(reporter_credence - self.credence))

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
        posterior = raw_posterior_good / normalizing_factor
        self.credence = discount * self.credence + (1-discount)*posterior


def histogram(credences):
    buckets = [0 for _ in range(10)]
    for credence in credences:
        buckets[min(9, floor(credence*10))] += 1
    return(buckets)


def simulation():
    agents = [Agent(random.random()) for i in range(N)]
    print([round(agent.credence, 3) for agent in agents])
    print()
    print(histogram([agent.credence for agent in agents]))

    for round_ in range(50):
        experiments = []
        for agent in agents:
            if agent.credence >= 0.5:
                experiments.append(
                    (summarize_experiment(agent.experiment()), agent.credence)
                )
        for agent in agents:
            for experiment, reporter_credence in experiments:
                hits, trials = experiment
                agent.update(hits, trials, agent.discount_factor(reporter_credence))

        print(histogram([agent.credence for agent in agents]))
        # print([round(agent.credence, 3) for agent in agents])

simulation()
