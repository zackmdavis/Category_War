from fractions import Fraction
from math import log2

p_a = [1/4, 7/16, 1/4, 1/16]
p_b = [1/16, 1/4, 7/16, 1/4]

total_prob = 0
bits = 0
symbols = []
for i in range(4):
    p = (p_a[i] + p_b[i]) / 2
    lr = p_a[i]/p_b[i]
    llr = log2(lr)
    print(p, lr, llr)
    total_prob += p
    bits += p * abs(log2(lr))
    symbols.append("({} + {})/2 * abs(log2({}))".format(Fraction(p_a[i]), Fraction(p_b[i]), Fraction(p_a[i]/p_b[i])))
print("total probability", total_prob)
print("bits", bits)
print(" + ".join(symbols))
print(eval(" + ".join(symbols)))
