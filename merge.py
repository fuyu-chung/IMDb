import pandas as pd

# file1 = pd.read_csv("new_csv/new.name.basics.csv") # read new title.akas.csv
# file2 = pd.read_csv("new_csv/new.title.akas.csv") # read new title.akas.csv
# file3 = pd.read_csv("new_csv/new.title.basics.csv") # read new title.basics.csv
# file4 = pd.read_csv("new_csv/new.title.crew.csv") # read new title.crew.csv
# file5 = pd.read_csv("new_csv/new.title.episode.csv") # read new title.episode.csv
# file6 = pd.read_csv("new_csv/new.title.principals.csv") # read new title.principals.csv
# file7 = pd.read_csv("new_csv/new.title.ratings.csv") # read new title.ratings.csv

# akas_basics_crew_ratings = file2.merge(file3, on = 'tconst', how = 'inner').merge(file4, on = 'tconst', how = 'inner').merge(file7, on = 'tconst', how = 'inner')
# akas_basics_crew_ratings.to_csv("csv/akas_basics_crew_ratings.csv", index = False)

file8 = pd.read_csv("new_csv/new.akas_basics_crew_ratings.csv")
file9 = pd.read_csv("new_csv/actor.csv")
file10 = pd.read_csv("new_csv/actress.csv")
file11 = pd.read_csv("new_csv/producer.csv")

akas_basics_crew_ratings = file8.merge(file9, on = 'tconst', how = 'inner').merge(file10, on = 'tconst', how = 'inner').merge(file11, on = 'tconst', how = 'inner')
akas_basics_crew_ratings.to_csv("new_csv/new.akas_basics_crew_ratings.csv", index = False)


