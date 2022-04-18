# Graphing requirements: scipy and matplotlib

import random
import enum

from math import factorial, sqrt

ε = 0.01  # size of edge for B
δ = 0.015  # size of partisan bias


def binomial(p, n, k):
    return (
        factorial(n) / (factorial(k) * factorial(n - k)) *
        p**k * (1 - p)**(n - k)
    )


def euclidean_distance(v, w):
    return sqrt(sum((v[i] - w[i]) ** 2 for i in range(len(v))))


def experiment(edge):
    return random.random() < 0.5 + edge


def summarize_experiment(results):
    return (len([r for r in results if r]), len(results))


class Alignment(enum.Enum):
    Honest = 1
    PartisanA = 2
    PartisanB = 3


class Agent:
    def __init__(self, initial_credences, initial_mistrusts, trial_count, alignment):
        self.questions = []
        assert len(initial_credences) == len(initial_mistrusts)
        for i in range(len(initial_credences)):
            question = {}
            for belief in [True, False]:
                for j, mistrust in enumerate(['honest', 'A', 'B']):
                    question[(belief, mistrust)] = (
                        (initial_credences[i] if belief else 1 - initial_credences[i]) *
                        initial_mistrusts[i][j]
                    )
            assert sum(question.values()) - 1 < 0.0001, sum(question.values())
            self.questions.append(question)

        self.trial_count = trial_count
        self.alignment = alignment

    def belief(self, question):
        total_belief = 0
        for bucket, probability in self.questions[question].items():
            belief, _mistrust = bucket
            if belief:
                total_belief += probability
        return total_belief

    def experiment(self):
        if self.alignment == Alignment.Honest:
            return [experiment(ε) for _ in range(self.trial_count)]
        elif self.alignment == Alignment.PartisanA:
            return [experiment(ε - δ) for _ in range(self.trial_count)]
        elif self.alignment == Alignment.PartisanB:
            return [experiment(ε + δ) for _ in range(self.trial_count)]
        else:
            raise ValueError("bogus alignment")

    def update(self, question, hits, trials):
        raw_posteriors = {}
        for (belief, edge) in [(True, ε), (False, -ε)]:
            for j, (mistrust, bias) in enumerate([('honest', 0), ('A', - δ), ('B', δ)]):
                likelihood = binomial(0.5 + edge + bias, trials, hits)
                raw_posteriors[(belief, mistrust)] = likelihood * self.questions[question][(belief, mistrust)]

        normalizing_factor = sum(raw_posteriors.values())
        for belief in [True, False]:
            for j, mistrust in enumerate(['honest', 'A', 'B']):
                self.questions[question][(belief, mistrust)] = raw_posteriors[(belief, mistrust)] / normalizing_factor


def random_mistrust_partition():
    a, b = sorted([random.random(), random.random()])
    partition = [a, b-a, 1-b]
    random.shuffle(partition)
    return partition


def simulation(
    honest_agent_count,  # number of honest agents
    partisan_a_agent_count,
    partisan_b_agent_count,
    question_count,  # numer of questions
    round_count,  # number of rounds
    trial_count,  # number of trials per round
):

    agents = []
    for _ in range(honest_agent_count):
        agents.append(
            Agent(
                [random.random() for _ in range(question_count)],
                [random_mistrust_partition() for _ in range(question_count)],
                trial_count=trial_count,
                alignment=Alignment.Honest
            )
        )
    for _ in range(partisan_a_agent_count):
        agents.append(
            Agent(
                [random.random() for _ in range(question_count)],
                [random_mistrust_partition() for _ in range(question_count)],
                trial_count=trial_count,
                alignment=Alignment.PartisanA
            )
        )
    for _ in range(partisan_b_agent_count):
        agents.append(
            Agent(
                [random.random() for _ in range(question_count)],
                [random_mistrust_partition() for _ in range(question_count)],
                trial_count=trial_count,
                alignment=Alignment.PartisanB
            )
        )

    for _ in range(round_count):
        for question in range(question_count):
            experiments = []
            for agent in agents:
                if agent.belief(question) >= 0.5:
                    experiments.append(
                        summarize_experiment(agent.experiment())
                    )

            for agent in agents:
                for experiment in experiments:
                    hits, trials = experiment
                    agent.update(question, hits, trials)

    return agents


# graph it!

import matplotlib.pyplot as plot
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans


def plot_beliefs(agents):
    beliefs = [[agent.belief(i) for i in range(len(agents[0].questions))]
               for agent in agents]

    graph_kwargs = {
        'c': [agent.alignment.value - 1 for agent in agents],
        'cmap': ListedColormap(
            ["black", "red", "blue"]
        )
    }

    figure = plot.figure()
    axes = Axes3D(figure)
    for scale_setter in [axes.set_xlim, axes.set_ylim, axes.set_zlim]:
        scale_setter(0, 1)

    axes.scatter(
        *[[agent.belief(i) for agent in agents] for i in range(3)],
        **graph_kwargs
    )
    plot.show()


if __name__ == "__main__":
    agents = simulation(
        honest_agent_count=20,
        partisan_a_agent_count=60,
        partisan_b_agent_count=60,
        round_count=20, question_count=3, trial_count=50
    )
    plot_beliefs(agents)
