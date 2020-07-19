from fractions import Fraction

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

table = []
for blueness in range(8):
    for palladium in range(2):
        row = []
        for eggness in range(8):
            row.append(sum(p*conditional_joint(c, blueness, eggness, palladium) for c, p in {"blegg": Fraction(12, 25), "rube": Fraction(12, 25), "other": Fraction(1, 25)}.items()))
        table.append(row)

print(table)
cells = sum(len(row) for row in table)
print(cells)
assert cells == 128
total_probability = sum(sum(cell for cell in row) for row in table)
print(total_probability)
assert total_probability == 1


def format_fraction(f):
    if f == 0:
        return "0"
    else:
        return "\\frac{%d}{%d}" % (f.numerator, f.denominator)

# for blueness in range(8):
#     for palladium in range(2):
for row, indices in zip(table, [(i, j) for i in range(8) for j in range(2)]):
        print(
           "blueness = {}, palladium = {} & ".format(*indices) +
            ' & '.join("${}$".format(format_fraction(cell)) for cell in row) + r" \\ \hline"
        )
