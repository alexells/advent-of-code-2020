import numpy as np
import pandas as pd

# load data and get it into columns
df = pd.read_csv("day3/input.txt", header=None)
df = df[0].apply(lambda x: pd.Series(list(x))).replace({".": "0", "#": "1"})


def ski(right, down):
    # starting point
    x, y, i = 0, 0, 0

    while y <= df.shape[0] - 1:
        i += int(df[x].values[y])
        x = (x + right) % 31
        y += down

    return i


solution1 = ski(3, 1)
print(f"Part 1 solution = {solution1}")

solution2 = ski(1, 1) * ski(3, 1) * ski(5, 1) * ski(7, 1) * ski(1, 2)
print(f"Part 2 solution = {solution2}")
