import numpy as np
import pandas as pd

values = np.loadtxt("day1/input.txt", delimiter=" ", unpack=False)

# # Solution to Part 1

# # if a+b=2020, then 0 < a <= 1010 <= b < 2020
# a_vals = values[values <= 1010]
# b_vals = values[values >= 1010]

# # b = 2020 - a
# f = lambda v: 2020 - v
# vf = np.vectorize(f)
# acceptable_b_vals = vf(a_vals)

# # find any b_vals that are acceptable and use the first solution
# mask = np.isin(b_vals, acceptable_b_vals)
# b = b_vals[mask][0]
# a = 2020 - b

# # the output required is a * b
# print(f"Solution: {a*b:.0f}")


# Slow but flexible function to solve both parts
# Note: this function allows duplicate use of a value


def solve(values, n, sum):
    # leverage pd.MultiIndex to get the cartesian product
    index = pd.MultiIndex.from_product(
        [values for x in range(0, n)], names=[f"n{x}" for x in range(0, n)]
    )
    df = pd.DataFrame(index=index).reset_index()

    # calculate sum of each combination
    df["sum"] = df.sum(axis=1)

    # return the product of the first combination where the sum == 2020
    return np.prod(df[(df["sum"] == sum)].iloc[:1, :n].values)


answer1 = solve(values, 2, 2020)
print(f"Solution to Part 1: {answer1:.0f}")

answer2 = solve(values, 3, 2020)
print(f"Solution to Part 2: {answer2:.0f}")
