import numpy as np
import pandas as pd

# read in data
with open("day4/input.txt", "r") as file:
    # one element per record
    raw = list(file.read().split("\n\n"))

    # convert record to string representation of a dict
    raw = [
        '{"'
        + el.replace("\n", " ").rstrip().replace(" ", '", "').replace(":", '":"')
        + '"}'
        for el in raw
    ]

    # create dataframe from list of evaluated dicts
    df = pd.DataFrame([dict(eval(x)) for x in raw])

print(df.sample(3))

# Part 1
solution1 = df.dropna(subset=["iyr", "ecl", "hgt", "pid", "byr", "hcl", "eyr"]).shape[0]
print(f"Part 1 solution = {solution1}")

## Part 2

# add some helper columns
df["is_cm"] = df["hgt"].str[-2:] == "cm"
df["is_in"] = df["hgt"].str[-2:] == "in"
df["height"] = df["hgt"].str[:-2]
df[["hash", "hexcode"]] = df["hcl"].str.split("#", expand=True)
print(df.sample(3))

# filter as required and get the number of records remaining
solution2 = df[
    (df.byr >= "1920")
    & (df.byr <= "2002")
    & (df.iyr >= "2010")
    & (df.iyr <= "2020")
    & (df.eyr >= "2020")
    & (df.eyr <= "2030")
    & (df.ecl.isin(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]))
    & (df.pid.str.len() == 9)
    & (df.hexcode.str.len() == 6)
    & (
        ((df.is_cm) & (df.height >= "150") & (df.height <= "193"))
        | ((df.is_in) & (df.height >= "59") & (df.height <= "76"))
    )
].shape[0]

print(f"Part 2 solution = {solution2}")
