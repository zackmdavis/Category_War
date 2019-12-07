from tabulate import tabulate

tenths = [i/10 for i in range(10)]


rows = [["choice", "p", "q", "funk-tunul payoff", "9-bot payoff"]]
for p in tenths:
    for q in tenths:
        if p + q > 1:
            continue
        rows.append(["funk-tunul gives in", p, q, 8*p + 4*q + 1, 9*p + 9*q])
        rows.append(["funk-tunul defies", p, q, 9*p + 5*q, 9*p])

print(tabulate(rows, headers="firstrow"))
