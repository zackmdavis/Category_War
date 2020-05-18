import random

from math import factorial, sqrt

ε = 0.01  # size of edge for B


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
    def __init__(self, initial_credences, trial_count, mistrust):
        self.credences = initial_credences
        self.trial_count = trial_count
        self.mistrust = mistrust

    def experiment(self):
        results = [b() for _ in range(self.trial_count)]
        return results

    def pure_update(self, question, hits, trials):
        raw_posterior_good = binomial(0.5 + ε, trials, hits) * self.credences[question]
        raw_posterior_bad = binomial(0.5 - ε, trials, hits) * (1 - self.credences[question])
        normalizing_factor = raw_posterior_good + raw_posterior_bad
        return raw_posterior_good / normalizing_factor

    def discount_factor(self, reporter_credences):
        return min(
            1, self.mistrust * euclidean_distance(self.credences, reporter_credences)
        )

    def update(self, question, hits, trials, discount):
        posterior = self.pure_update(question, hits, trials)
        self.credences[question] = (
            discount * self.credences[question] + (1 - discount) * posterior
        )


def simulation(
    agent_count,  # number of agents
    question_count,  # numer of questions
    round_count,  # number of rounds
    trial_count,  # number of trials per round
    mistrust,  # mistrust factor
):
    agents = [
        Agent(
            [random.random() for _ in range(question_count)],
            trial_count=trial_count,
            mistrust=mistrust,
        )
        for i in range(agent_count)
    ]

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


def plot_beliefs(agents, cluster=True):
    beliefs = [agent.credences for agent in agents]

    if cluster:
        cluster_model = KMeans(n_clusters=8)
        cluster_model.fit(beliefs)
        graph_kwargs = {
            'c': cluster_model.predict(beliefs),
            'cmap': ListedColormap(
                ["red", "orangered", "green", "blue", "purple", "black", "brown", "deepskyblue"]
            )
        }
    else:
        graph_kwargs = {}

    figure = plot.figure()
    axes = Axes3D(figure)
    for scale_setter in [axes.set_xlim, axes.set_ylim, axes.set_zlim]:
        scale_setter(0, 1)

    axes.scatter(
        *[[agent.credences[i] for agent in agents] for i in range(3)],
        **graph_kwargs
    )
    plot.show()


if __name__ == "__main__":
    agents = simulation(
        agent_count=200, round_count=20, question_count=3, trial_count=50, mistrust=2
    )
    plot_beliefs(agents)
