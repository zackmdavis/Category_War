def squared_error(distribution):
    grand_error = 0
    for guess, guess_probability in distribution.items():
        for actual, actual_probability in distribution.items():
            grand_error += guess_probability * actual_probability * (actual - guess)**2
    return grand_error

print(squared_error({i: 1/8 for i in range(1,9)}))
print(squared_error({i: 1/4 for i in range(1,5)}))

print({i: 1/4 for i in range(1,9,2)})
print(squared_error({i: 1/4 for i in range(1,9,2)}))

print({i: 1/4 for i in range(2,9,2)})
print(squared_error({i: 1/4 for i in range(2,9,2)}))
