import pandas as pd
from glob import glob

file1 = pd.read_csv("title.basics.csv")
file2 = pd.read_csv("title.ratings.csv")

result = pd.merge(left = file1, right = file2, how = "inner", on = "tconst")
result.to_csv("result.csv")
# print(result)