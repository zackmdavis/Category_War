def squared_error(distribution):
    grand_error = 0
    for guess, guess_probability in distribution.items():
        for actual, actual_probability in distribution.items():
            grand_error += guess_probability * actual_probability * (actual - guess)**2
    return grand_error

print("initial", squared_error({i: 1/8 for i in range(1,9)}))
print("square-err after learning 1–4", squared_error({i: 1/4 for i in range(1,5)}))

print("odds distribution", {i: 1/4 for i in range(1,9,2)})
print("square-err for oddds", squared_error({i: 1/4 for i in range(1,9,2)}))

print("evens distribution", {i: 1/4 for i in range(2,9,2)})
print("square-err for evens", squared_error({i: 1/4 for i in range(2,9,2)}))
