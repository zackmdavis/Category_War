from fractions import Fraction
from math import log2 as lg

def scale_feature(category):
    if category == "blegg":
        return [0, 0, 0, 0, 0, Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)]
    elif category == "rube":
        return [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4), 0, 0, 0, 0, 0]
    else:
        return [Fraction(1, 8)]*8

def boolean_feature(category):
    return int(category == "blegg")

def conditional_joint(category, x1, x2, p):
    return scale_feature(category)[x1]*scale_feature(category)[x2]*int(p == boolean_feature(category))

# def category_from_data(datum):


# def format_fraction(f):
#     if f == 0:
#         return "0"
#     else:
#         return "\\frac{%d}{%d}" % (f.numerator, f.denominator)

# for row, indices in zip(table, [(i, j) for i in range(8) for j in range(2)]):
#         print(
#            "blueness = {}, vanadium = {} & ".format(*indices) +
#             ' & '.join("${}$".format(format_fraction(cell)) for cell in row) + r" \\ \hline"
#         )

        # camera_distribution[(blueness, eggness)] = sum(sum(p*conditional_joint(c, blueness, eggness, vanadium) for c, p in {"blegg": Fraction(12, 25), "rube": Fraction(12, 25), "other": Fraction(1, 25)}.items()) for vanadium in range(2))

        # print(entropy(camera_distribution.values()))

def entropy(p_x):
    return sum(p*lg(1/p) for p in p_x if p)


def conditional_entropy(distribution, condition):
    total = 0
    for key, p in distribution.items():
        p_x = sum(q for l, q in distribution.items() if l[condition] == key[condition])
        if p:
            total -= p * lg(p/p_x) # lg(p(x)/p(x,y))
    return total


base_rates = {"blegg": Fraction(12, 25), "rube": Fraction(12, 25), "other": Fraction(1, 25)}

blegg_star_cells = {(i, j) for i in range(5,8) for j in range(5,8)} | {(6, k) for k in range(1, 5)}  | {(l, 1) for l in range(2, 6)} | {(2,2)}
rube_star_cells = {(i, 0) for i in range(0,3)} | {(1,0), (1,1), (0,2), (1,2)}

distribution = {}
labeled_distribution = {}
badly_labeled_distribution = {}

for blueness in range(8):
    for eggness in range(8):
        for vanadium in range(2):
            if (eggness, blueness) in blegg_star_cells:
                bad_label = 'blegg*'
            elif (eggness, blueness) in rube_star_cells:
                bad_label = 'rube*'
            else:
                bad_label = 'other'
            badly_labeled_distribution[(bad_label, blueness, eggness, vanadium)] = 0
            distribution[(blueness, eggness, vanadium)] = 0
            for c, p in base_rates.items():
                v = p*conditional_joint(c, blueness, eggness, vanadium)
                distribution[(blueness, eggness, vanadium)] += v
                badly_labeled_distribution[(bad_label, blueness, eggness, vanadium)] += v
                labeled_distribution[(c, blueness, eggness, vanadium)] = v


def squared_error(distribution, metric):
    grand_error = 0
    for guess, guess_probability in distribution.items():
        for actual, actual_probability in distribution.items():
            grand_error += guess_probability * actual_probability * metric(actual, guess)
    return grand_error

def bleggspace_metric(u, v):
    return sum((u[i] - v[i])**2 for i in range(3))

def bleggspace_metric_strip_labels(u, v):
    return bleggspace_metric(u[1:], v[1:])


def shaded_error(distribution, metric):
    squerr = squared_error(distribution, metric)
    average_revenue = 0
    for actual, actual_probability in distribution.items():
        if actual[0] in ['blegg', 'blegg*']:
            average_revenue += 2*actual_probability
        elif actual[0] in ['rube', 'rube*']:
            average_revenue += actual_probability
    return squerr - 20*average_revenue

print(labeled_distribution)
print(badly_labeled_distribution)
print("rube/blegg/?? initial mean squared error", float(squared_error(labeled_distribution, bleggspace_metric_strip_labels)))
print("blegg*/not initial mean squared error", float(squared_error(badly_labeled_distribution, bleggspace_metric_strip_labels)))

# TODO: to measure actual goodness of category system, need to sum over after
# learning all categories, not just the blegg case

print("square-err after learning blegg", float(squared_error({k: v for k, v in labeled_distribution.items() if k[0] == 'blegg'}, bleggspace_metric_strip_labels)))
print("square-err after learning blegg*", float(squared_error({k: v for k, v in badly_labeled_distribution.items() if k[0] == 'blegg*'}, bleggspace_metric_strip_labels)))

print("shady-score after learning blegg", float(shaded_error({k: v for k, v in labeled_distribution.items() if k[0] == 'blegg'}, bleggspace_metric_strip_labels)))
print("shady-score after learning blegg*", float(shaded_error({k: v for k, v in badly_labeled_distribution.items() if k[0] == 'blegg*'}, bleggspace_metric_strip_labels)))


total = sum(labeled_distribution.values())
print(labeled_distribution)
print(total)
assert total == 1


H_category_data = entropy(labeled_distribution.values())
H_data = entropy(distribution.values())
H_category = entropy([12/25, 12/25, 1/25])
H_data_given_category = conditional_entropy(labeled_distribution, 0)
H_category_given_data = conditional_entropy(labeled_distribution, slice(1, None))

H_badegory_data = entropy(badly_labeled_distribution.values())
H_badegory = entropy([sum(p for k, p in badly_labeled_distribution.items() if k[0]), sum(p for k, p in badly_labeled_distribution.items() if not k[0])])
H_data_given_badegory = conditional_entropy(badly_labeled_distribution, 0)
H_badegory_given_data = conditional_entropy(badly_labeled_distribution, slice(1, None))

print("H(category,data)", H_category_data)
print("H(data)", H_data)
print("H(data|category)", H_data_given_category)
print("H(category|data)", H_category_given_data)
print("H(category)", H_category)
print("H(data) − H(data|category)", H_data - H_data_given_category)
print("H(category) − H(category|data)", H_category - H_category_given_data)

print("————")

print("H(badegory,data)", H_badegory_data)
print("H(data)", H_data)
print("H(data|badegory)", H_data_given_badegory)
print("H(badegory|data)", H_badegory_given_data)
print("H(badegory)", H_badegory)
print("H(data) − H(data|badegory)", H_data - H_data_given_badegory)
print("H(badegory) − H(badegory|data)", H_badegory - H_badegory_given_data)
