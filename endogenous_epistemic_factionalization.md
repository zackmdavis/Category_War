## Comment on "Endogenous Epistemic Factionalization"

In ["Endogenous Epistemic Factionalization"](https://arxiv.org/abs/1812.08131) (due in a forthcoming issue of the philosophy-of-science journal [_Synthese_](https://www.springer.com/journal/11229/)), James Owen Weatherall and Cailin O'Connor propose a possible answer to the question of why people who disagree on one subject tend to also disagree on others.

The existence of persistent disagreements is [_already_](https://www.lesswrong.com/posts/NKECtGX4RZPd7SqYp/the-modesty-argument) [kind](https://www.lesswrong.com/posts/tKa9Lebyebf6a7P2o/the-rhythm-of-disagreement) [of](https://www.lesswrong.com/posts/gTTWRkSz474o7s4Dg/principles-of-disagreement) [a puzzle](https://ppe.mercatus.org/system/files/Are_Disagreements_Honest_-_WP.pdf) from a Bayesian perspective. [There's only one](https://genius.com/They-might-be-giants-one-everything-lyrics) reality. If everyone is honestly trying to get the right answer and we can all _talk_ to each other, then we should coverge on the right answer (or an answer that is [less wrong](https://tvtropes.org/pmwiki/pmwiki.php/Main/TitleDrop) given the evidence we have). The fact that we _can't do it_ is, or should be, an embarrassment to our species.

And the existence of _correlated_ persistent disagreements—when not only do I say "top" when you say "bottom" even after we've gone over all the arguments for whether it is in fact the case that top or bottom, but _furthermore_, the fact that I said "top" lets you _predict_ that I'll probably say "cold" rather than "hot" even _before_ we go over the arguments for that, is an _atrocity_. (Not hyperbole. Thousands of people are dying horrible suffocation deaths because we can't figure out the optimal response to a new kind of coronavirus.)

Correlations between beliefs are often attributed to ideology or [tribalism](https://slatestarcodex.com/2014/11/04/ethnic-tension-and-meaningless-arguments/): if I believe that Markets Are the Answer, I'm likely to propose Market-based solutions to all sorts of seemingly-unrelated social problems, and if I'm [loyal to my people of the Green tribe](https://www.lesswrong.com/posts/6hfGNLf4Hg5DXqJCF/a-fable-of-science-and-politics), I'm likely to [selectively censor my thoughts in order to fit the Green party line](https://www.lesswrong.com/posts/DoPo4PDjgSySquHX8/heads-i-win-tails-never-heard-of-her-or-selective-reporting). But ideology can't explain correlated disagreements on unrelated topics that the content of the ideology is silent on, and tribalism can't explain correlated disagreements on narrow, technical topics that aren't [tribal shibboleths](https://slatestarcodex.com/2016/04/04/the-ideology-is-not-the-movement/).

In this paper, Weatherall and O'Connor exhibit a toy model that proposes a simple mechanism that can explain correlated disagreement: if agents disbelieve in evidence presented by those with sufficiently dissimilar beliefs, factionalization emerges, even though everyone is honestly reporting their observations and updating on what they are told (to the extent that they believe it). The paper didn't seem to provide source code for the simulations it describes, so I followed along in Python. (Replication!)

In each round of the model, our little Bayesian agents choose between repeatedly performing one of two actions, A or B, that can "succeed" or "fail." A is a fair coin: it succeeds exactly half the time. _As far as our agents know_, B is _either_ slightly better or slightly worse (with equal prior proability): the per-action probability of success is either 0.5 + ɛ or 0.5 − ɛ, for some ɛ (a parameter to the simulation). But secretly, we the simulation authors know that B is better.

```
import random

ε = 0.01

def b():
    return random.random() < 0.5 + ε
```

The agents start out with a uniformly random probability that B is better. The ones who believe that A is better, repeatedly do A (and don't learn anything, because they already know that A is exactly a coinflip). The ones who believe that B is better, repeatedly do B, but keep track of and publish their results in order to help everyone figure out whether B is slightly better or slightly worse than a coinflip.

```
class Agent:
    ...

    def experiment(self):
        results = [b() for _ in range(self.trial_count)]
        return results
```

Except in order to study the emergence of factionalization among multiple beliefs, we should actually have our agents face _multiple_ "A or B" dilemmas, representing beliefs about unrelated questions. (In each case, B will again be better, but the agents don't start out knowing that.) I chose three beliefs, because that's all I can fit in my pretty 3D scatterplots.

If all the agents update on the experimental results published by the agents who do B, they quickly learn that B is better for all three questions. If $H_{+}$ represents the hypothesis that B is better than A, and $H_{-}$ represents the hypothesis that B is worse, then Bayes's theorem says

$$P(H_{+}|E) = \frac{P(E|H_{+})P(H_{+})}{P(E|H_{+})P(H_{+}) + P(E|H_{-})P(H_{-})}$$

where E is the record of how many successes we got in how many times we tried action B. The likelihoods $P(E|H_{+})$ and $P(E|H_{-})$ can be calculated from the probability mass function of the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution), so the agents have all the information they need to update their beliefs based on experiments with B.

```
def binomial(p, n, k):
    return (
        factorial(n) / (factorial(k) * factorial(n - k)) *
        p**k * (1 - p)**(n - k)
    )

class Agent:
    ...

    def pure_update(self, question, hits, trials):
        raw_posterior_good = binomial(0.5 + ε, trials, hits) * self.credences[question]
        raw_posterior_bad = binomial(0.5 - ε, trials, hits) * (1 - self.credences[question])
        normalizing_factor = raw_posterior_good + raw_posterior_bad
        return raw_posterior_good / normalizing_factor

```

If we make a pretty 3D scatterplot where [each dimension represents](https://www.lesswrong.com/posts/WBw8dDkAWohFjWQSk/the-cluster-structure-of-thingspace) the probability that B is better for one of the dilemmas, then the points converge to the corner [1.0, 1.0, 1.0], even though they started out uniformly distributed all over the space.

![](https://i.imgur.com/E61Hp4W.png)

-------



In [a previous paper](https://arxiv.org/abs/1712.04561), 



Why do beliefs cluster? Some say ideology, but the clusters we see don't seem coherent enough for that

Polarization: stable beliefs despite discussion—disagreement isn't polarization because it's not stable

models of cultural influence assume there is no fact of the matter; you can't share evidence for liking Mozart

N agents choose between A and B, which each give the same payoff on success, but have a different probability of success. pA = 0.5, pB = 0.5 +/- ε

B is actually better; agents' credence that B is better are drawn from a uniform distribution

in each round, each agent does what they think is best n times, and does a Bayesian update on the result (A is already well understood)

update on neighbors—complete network

in the model as described, we get consensus

reproducible research: https://www.frontiersin.org/articles/10.3389/fninf.2017.00069/full

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
