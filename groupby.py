import pandas as pd

file6 = pd.read_csv("new_csv/new.title.principals.csv") # read new.title.principals.csv
file6 = file6.groupby(['tconst','category'])['nconst'].apply(','.join).reset_index()
file6.replace(to_replace={'nconst': ', '}, value=',', regex=True, inplace=True) # if the list start at comma or end with comma, replace the value to ''
file6.to_csv("new_csv/new.title.principals.csv", index=False)