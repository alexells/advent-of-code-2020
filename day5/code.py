import numpy as np
import pandas as pd

# load data and get it into columns
df = pd.read_csv("day5/input.txt", header=None, names=["raw"])

# split string and decode to binary
df["fb"] = df.apply(lambda x: x.raw[0:7], axis=1)
df["lr"] = df.apply(lambda x: x.raw[7:10], axis=1)

df["fb"] = df["fb"].str.replace("F", "0")
df["fb"] = df["fb"].str.replace("B", "1")

df["lr"] = df["lr"].str.replace("L", "0")
df["lr"] = df["lr"].str.replace("R", "1")

# convert binary to decimal
df["fb_bin"] = df.apply(lambda x: int(x.fb, 2), axis=1)
df["lr_bin"] = df.apply(lambda x: int(x.lr, 2), axis=1)

# apply final equation for part 1
df["sol1"] = (df["fb_bin"] * 8) + df["lr_bin"]
solution1 = df.sol1.max()
print(f"Part 1 solution = {solution1}")

# count allocated seats per row / column
fb_ct = df.groupby("fb_bin").agg(ct=("sol1", "count"))
lr_ct = df.groupby("lr_bin").agg(ct=("sol1", "count"))

# apply final equation to the row / column with the unallocated seat
solution2 = fb_ct[1:-1].idxmin() * 8 + lr_ct[1:-1].idxmin()
print(f"Part 2 solution = {solution2}")
