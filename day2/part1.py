import numpy as np
import pandas as pd

# load data
df = pd.read_csv("day2/input.txt", delimiter="\s+|;|:|-", header=None)
df.columns = ["min_ct", "max_ct", "letter", "whitespace", "pw"]
df = df.drop(columns="whitespace")

# count occurances of required letter
df["ct"] = df.apply(lambda x: x.pw.count(x.letter), axis=1)

# print a count of valid passwords
print(df[(df.ct >= df.min_ct) & (df.ct <= df.max_ct)].shape[0])