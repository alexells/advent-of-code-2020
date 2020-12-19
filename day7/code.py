import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)

# read in the input
df = pd.read_csv("day7/input.txt", header=None, delimiter="\n", names=["raw"])

# parse input and melt from wide to long
df[["parent", "children"]] = df["raw"].str.split(" bags contain ", expand=True)
df = df.join(df["children"].str.split(", ", expand=True))
newcols = df.drop(columns=["raw", "parent", "children"]).columns
df = pd.melt(df, id_vars=["parent"], value_vars=newcols).drop(columns=["variable"])

# drop Nones, clean up data, split quantity and child type
df = df[~pd.isnull(df["value"])]
df["value"] = df["value"].str.replace(".", "")
df["value"] = df["value"].str.replace(" bags", "")
df["value"] = df["value"].str.replace(" bag", "")
df[["quantity", "child"]] = df["value"].str.split(" ", 1, expand=True)
df = df.drop(columns=["value"])
df = df[(df["quantity"] != "no")]


# Part 1: How many bag colors can eventually contain at least one shiny gold bag?

parents = []


def find_parents(child):
    new_parents = set(df[(df.child == child)]["parent"])

    for p in new_parents:
        if p not in parents:
            parents.append(p)
            find_parents(p)

    return len(parents)


sol1 = find_parents("shiny gold")

print(f"Part 1 solution: {sol1}")


# Part 2: How many individual bags are required inside your single shiny gold bag?

children = []


def find_children(parent):
    new_children = list(
        df[(df.parent == parent)][["quantity", "child"]].to_records(index=False)
    )

    for q, c in new_children:
        for i in range(0, int(q)):
            children.append(c)
            find_children(c)

    return len(children)


sol2 = find_children("shiny gold")
print(f"Part 2 solution: {sol2}")
