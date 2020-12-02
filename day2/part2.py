import numpy as np
import pandas as pd

# load data
df = pd.read_csv("day2/input.txt", delimiter="\s+|;|:|-", header=None)
df.columns = ["pos1", "pos2", "letter", "whitespace", "pw"]
df = df.drop(columns="whitespace")

# check occurances of required letters
df["check_p1"] = df.apply(lambda x: x.pw[x.pos1 - 1] == x.letter, axis=1)
df["check_p2"] = df.apply(lambda x: x.pw[x.pos2 - 1] == x.letter, axis=1)
df["exactly_one_match"] = np.logical_xor(df["check_p1"], df["check_p2"])

# print a count of valid passwords
print(df[(df["exactly_one_match"])].shape[0])
