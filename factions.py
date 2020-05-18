import random

from math import factorial, floor, sqrt

agent_count = 200  # number of agents
trial_count = 50  # trials per experiment
round_count = 20  # number of rounds
ε = 0.01  # size of edge for B
mistrust = 2  # mistrust factor
question_count = 3


def binomial(p, n, k):
    return (
        factorial(n) / (factorial(k) * factorial(n - k)) *
        p**k * (1 - p)**(n - k)
    )


def euclidean_distance(v, w):
    return sqrt(sum((v[i] - w[i]) ** 2 for i in range(len(v))))


def b():
    return random.random() < 0.5 + ε


def summarize_experiment(results):
    return (len([r for r in results if r]), len(results))


class Agent:
    def __init__(self, initial_credences):
        self.credences = initial_credences

    def experiment(self):
        results = [b() for _ in range(trial_count)]
        return results

    def discount_factor(self, reporter_credences):
        return min(1, mistrust * euclidean_distance(self.credences, reporter_credences))

    def update(self, question, hits, trials, discount):
        # P(H₊|E) = P(E|H₊)P(H₊) / (P(E|H₊)P(H₊) + P(E|H₋)P(H₋))
        raw_posterior_good = binomial(0.5 + ε, trials, hits) * self.credences[question]
        raw_posterior_bad = binomial(0.5 - ε, trials, hits) * (
            1 - self.credences[question]
        )
        normalizing_factor = raw_posterior_good + raw_posterior_bad
        posterior = raw_posterior_good / normalizing_factor
        self.credences[question] = (
            discount * self.credences[question] + (1 - discount) * posterior
        )


def simulation(agents):
    for _ in range(round_count):
        for question in range(question_count):
            experiments = []
            for agent in agents:
                if agent.credences[question] >= 0.5:
                    experiments.append(
                        (summarize_experiment(agent.experiment()), agent.credences)
                    )
            for agent in agents:
                for experiment, reporter_credences in experiments:
                    hits, trials = experiment
                    agent.update(
                        question,
                        hits,
                        trials,
                        agent.discount_factor(reporter_credences),
                    )

    return agents


import matplotlib.pyplot as plot
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans


def plot_beliefs(agents):
    beliefs = [agent.credences for agent in agents]

    cluster_model = KMeans(n_clusters=8)
    cluster_model.fit(beliefs)

    figure = plot.figure()
    axes = Axes3D(figure)
    for scale_setter in [axes.set_xlim, axes.set_ylim, axes.set_zlim]:
        scale_setter(0, 1)

    axes.scatter(
        *[[agent.credences[i] for agent in agents] for i in range(3)],
        c=cluster_model.predict(beliefs),
        cmap=ListedColormap(
            ["red", "orangered", "green", "blue", "purple", "black", "brown", "gray"]
        ),
    )
    plot.show()


if __name__ == "__main__":
    agents = [
        Agent([random.random() for _ in range(question_count)])
        for i in range(agent_count)
    ]
    simulation(agents)
    plot_beliefs(agents)
