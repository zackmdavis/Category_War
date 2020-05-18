# Comment on "Endogenous Epistemic Factionalization"

In ["Endogenous Epistemic Factionalization"](https://arxiv.org/abs/1812.08131) (due in a forthcoming issue of [_Synthese_](https://www.springer.com/journal/11229/), a philosophy-of-science journal), James Owen Weatherall and Cailin O'Connor propose a possible answer to the question of why people who disagree on one subject tend to also disagree on others.

The existence of persistent disagreements is [_already_ kind of a puzzle](https://ppe.mercatus.org/system/files/Are_Disagreements_Honest_-_WP.pdf) from a Bayesian perspective. There's only one reality.











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
