from collections import namedtuple
from fractions import Fraction
from math import sqrt

def expected_squared_error_reimpl(distribution, metric):
    from collections import namedtuple
    wrap = namedtuple('wrap', ['value'])

    guess = 0
    for outcome, probability in distribution.items():
        print(outcome, probability)
        guess += outcome.value * probability
    print("guess is", guess)
    grand_error = 0
    for actual, actual_probability in distribution.items():
        grand_error += (
            actual_probability * (metric(actual, wrap(value=guess)) ** 2)
        )
    return grand_error


# TODO: what is the "guess" under a non-Euclidean metric?!

def expected_squared_error(distribution, metric):
    """
    If we know the distribution, and we "guess" the value of a sample from that
    distribution (guesses proportional to actual probability-mass), how much
    will we be wrong on average (with respect to a given metric on the space,
    squared)?
    """
    guess = 0
    for outcome, probability in distribution.items():
        print(outcome, probability)
        guess += outcome.value * probability
    print("guess is", guess)
    grand_error = 0
    for actual, actual_probability in distribution.items():
        grand_error += (
            actual_probability * (metric(actual, wrap(value=guess)) ** 2)
        )
    return grand_error
    # grand_error = 0
    # for guess, guess_probability in distribution.items():
    #     for actual, actual_probability in distribution.items():
    #         grand_error += (
    #             guess_probability * actual_probability * metric(actual, guess) ** 2
    #         )
    # return grand_error


def expected_squared_error_given_categorization(
    distribution, metric, category_label_property
):
    category_labels = set(getattr(ω, category_label_property) for ω in distribution)
    grand_error = 0
    for label in category_labels:
        # Get probability of category-membership and the distribution updated
        # on category-membership.

        # First, eliminate the probability-mass of all the other categories
        # that we're not examining right now.
        truncated_distribution = {
            ω: p
            for ω, p in distribution.items()
            if getattr(ω, category_label_property) == label
        }
        category_probability = sum(truncated_distribution.values())
        # Then, renormalize.
        updated_distribution = {
            ω: p / category_probability for ω, p in truncated_distribution.items()
        }
        category_squerr = expected_squared_error(updated_distribution, metric)
        grand_error += category_probability * category_squerr
    return grand_error



FactoryOutcome = namedtuple(
    "FactoryOutcome",
    ["true_category", "unnatural_category", "eggness", "blueness", "vanadium"],
)

base_rates = {
    "blegg": Fraction(12, 25),
    "rube": Fraction(12, 25),
    "other": Fraction(1, 25),
}


def scale_feature(category):
    """
    Given (true) `category` ∈ {"blegg", "rube", "other"}, return a length-8 list
    of probabilities representing the marginal blueness or eggness distributon.
    """
    if category == "blegg":
        return [0, 0, 0, 0, 0, Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]
    elif category == "rube":
        return [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4), 0, 0, 0, 0, 0]
    else:
        return [Fraction(1, 8)] * 8


def boolean_feature(category):
    """
    Given (true) `category` ∈ {"blegg", "rube", "??"}, return 1 if the category
    is "blegg".
    """
    return int(category == "blegg")


def conditional_joint(category, eggness, blueness, vanadium):
    """
    Given true-category-membership, eggness score, blueness score, and
    vanadium-presence, compute the probability density.
    """
    return (
        scale_feature(category)[eggness]
        * scale_feature(category)[blueness]
        * int(vanadium == boolean_feature(category))
    )


def infer_unnatural_category(eggness, blueness):
    # specify which "cells" in (eggness, blueness) space are inside the
    # unnatural blegg*/rube* category boundaries
    blegg_star_cells = (
        {(i, j) for i in range(5, 8) for j in range(5, 8)}
        | {(6, k) for k in range(1, 5)}
        | {(l, 1) for l in range(2, 6)}
        | {(2, 2)}
    )
    rube_star_cells = {(i, 0) for i in range(0, 3)} | {(0, 1), (1, 1), (0, 2), (1, 2)}
    if (eggness, blueness) in blegg_star_cells:
        return "blegg*"
    elif (eggness, blueness) in rube_star_cells:
        return "rube*"
    else:
        return "other*"


def factory_distribution():
    distribution = {}
    for blueness in range(8):
        for eggness in range(8):
            for vanadium in range(2):
                unnatural_category = infer_unnatural_category(eggness, blueness)
                for true_category, true_category_prior in base_rates.items():
                    p = true_category_prior * conditional_joint(
                        true_category, blueness, eggness, vanadium
                    )
                    if p:
                        distribution[
                            FactoryOutcome(
                                true_category=true_category,
                                unnatural_category=unnatural_category,
                                eggness=eggness,
                                blueness=blueness,
                                vanadium=vanadium,
                            )
                        ] = p
    return distribution


def eightfold_example():
    print("{1..8} example")
    EightfoldOutcome = namedtuple("EightfoldOutcome", ["parity", "half", "value"])
    distribution = {
        EightfoldOutcome(parity=value % 2, half=value < 4.5, value=value): 1 / 8
        for value in range(1, 9)
    }
    assert sum(distribution.values()) == 1
    metric = lambda u, v: u.value - v.value
    initial_squerr = expected_squared_error(distribution, metric)

    print("initial expected squared error: ", initial_squerr)
    print("double check", expected_squared_error_reimpl(distribution, metric))
    print(
        "expected squared error given knowledge of parity: ",
        expected_squared_error_given_categorization(distribution, metric, "parity"),
    )
    print(
        "expected squared error given knowledge of 1–4/5–8: ",
        expected_squared_error_given_categorization(distribution, metric, "half"),
    )
    print("------")


def factory_example():
    print("blegg/rube factory example")
    distribution = factory_distribution()
    assert sum(distribution.values()) == 1
    metrics = {
        "basic": lambda u, v: sqrt(
            sum(
                (getattr(u, prop) - getattr(v, prop)) ** 2
                for prop in ["eggness", "blueness", "vanadium"]
            )
        ),
        # ... feel free to try out other metrics here!
    }
    #     "eggness–vanadium-only": lambda u, v: sqrt(
    #         sum(
    #             (getattr(u, prop) - getattr(v, prop)) ** 2
    #             for prop in ["eggness", "vanadium"]
    #         )
    #     ),
    #     "vanadium-weighted": lambda u, v: sqrt(
    #         sum(
    #             (
    #                 (0.2 * (getattr(u, prop) - getattr(v, prop))) ** 2
    #                 if prop in ["eggness", "blueness"]
    #                 else (getattr(u, prop) - getattr(v, prop)) ** 2
    #             )
    #             for prop in ["eggness", "blueness", "vanadium"]
    #         )
    #     ),
    #     "vanadium-only": lambda u, v: u.vanadium - v.vanadium,
    # }
    # show off different metrics
    for metric_name, metric in metrics.items():
        initial_squerr = expected_squared_error(distribution, metric)
        print(
            "initial expected squared error ({} metric): ".format(metric_name),
            initial_squerr,
        )
        for category_system in ["true_category", "unnatural_category"]:
            later_squerr = expected_squared_error_given_categorization(
                distribution, metric, category_system
            )
            print(
                "expected squared error given knowledge of {} ({} metric)".format(
                    category_system.replace("_", " "), metric_name
                ),
                later_squerr,
            )

    # now exhibit the scoring criterion that rewards deception
    for category_system in ["true_category", "unnatural_category"]:
        squerr = expected_squared_error_given_categorization(
            distribution, metrics["basic"], category_system
        )
        revenue = sum(
            price
            * sum(
                p
                for ω, p in distribution.items()
                if getattr(ω, category_system).startswith(object_name)
            )
            for (price, object_name) in [(200, "blegg"), (100, "rube")]
        )
        print(
            "squared error minus revenue given knowledge of {} (basic metric)".format(
                category_system.replace("_", " ")
            ),
            squerr - revenue,
        )


if __name__ == "__main__":
    eightfold_example()
    factory_example()
