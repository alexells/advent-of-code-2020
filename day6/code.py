import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)

# read in data
with open("day6/input.txt", "r") as file:
    # one row per group of passengers
    raw = list(file.read().split("\n\n"))
    raw = [el.rstrip().replace("\n", ",") for el in raw]
    df = pd.DataFrame(raw, columns=["raw"])

# Part 1: For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
# == sum of counts of unique characters for each row

# unique characters excluding commas
df["set"] = df.apply(lambda x: set(x.raw.replace(",", "")), axis=1)

# count of unique characters
df["len"] = df.apply(lambda x: len(x.set), axis=1)

# sum to get the solution
sol1 = df.len.sum()

print(f"Solution 1: {sol1}")


# Part 2: For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
# == count how many of the group's answers apply to all passengers in a group, then sum

# count the number of passengers in each group
df["pax_ct"] = df.apply(lambda x: x.raw.count(",") + 1, axis=1)

# for each of the group's unique answers, how many times do they appear in the group
df["ct"] = df.apply(lambda x: [x.raw.count(l) for l in x.set], axis=1)

# how many answers appear the same number of times as the count of passengers in each group
df["all"] = df.apply(lambda x: len([l for l in x.ct if l == x.pax_ct]), axis=1)

# sum to get the solution
sol2 = df["all"].sum()

print(f"Solution 2: {sol2}")
