tenths = [i/10 for i in range(10)]

def submit(p, q):
    return 8*p + 4*q + 1

def defy(p, q):
    return 9*p + 5*q

for p in tenths[1:5]:
    for q in tenths[1:5]:
        if p + q > 1:
            continue
        print(
            "p={}, q={}, submit={}, defy={}".format(
                p, q, submit(p, q), defy(p, q)
            )
        )


# rows = [["choice", "p", "q", "funk-tunul payoff", "9-bot payoff"]]
# for p in tenths:
#     for q in tenths:
#         if p + q > 1:
#             continue
#         rows.append(["funk-tunul gives in", p, q, 8*p + 4*q + 1, 9*p + 9*q])
#         rows.append(["funk-tunul defies", p, q, 9*p + 5*q, 9*p])

# print(tabulate(rows, headers="firstrow"))
