import random

def x():
    r = random.random()
    if 0 <= r < 1/2:
        return 1
    elif 1/2 <= r < 3/4:
        return 2
    elif 3/4 <= r < 15/16:
        return 3
    else:
        return 4


actual = {1: 1/2, 2: 1/4, 3: 3/16, 4: 1/16}

from collections import Counter


def audience(report):
    a = Counter()
    for sight in report:
        for possibility in sight:
            a[possibility] += 1/len(sight)
    d = sum(a_j - len(a) for a_j in a.values())
    return {x: (a_i - 1)/d for x, a_i in a.items()}


# truth
def reporter_0(xs):
    output = []
    for x in xs:
        output.append({x})
    return output

# lies
def reporter_1(xs):
    output = []
    for _ in range(len(xs)):
        output.append({4})
    return output

# selective reporting
def reporter_2(xs):
    output = []
    for x in xs:
        if x == 4 or random.random() < 0.2:
            output.append({x})
        else:
            continue
    return output

# category-gerrymandering
def reporter_3(xs):
    output = []
    for x in xs:
        if x == 1 or x == 4:
            output.append({1, 4})
        else:
            output.append({x})
    return output
