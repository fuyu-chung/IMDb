import pandas as pd

# name.basics.csv
# file1 = pd.read_csv("name.basics.csv") # read title.akas.csv
# file1.drop(['birthYear', 'deathYear'], axis = 1, inplace = True) #remove birthYear, deathYear column
# file1.to_csv("new.name.basics.csv", index = False) # row output

# title.akas.csv
# file2 = pd.read_csv("title.akas.csv") # read title.akas.csv
# file2.drop(['title', 'types', 'attributes', 'isOriginalTitle', 'language'], axis = 1, inplace = True) #remove title, types, attributes, isOriginalTitle, language column
# file2.drop(file2.loc[file2['ordering'] != 2].index, inplace = True) # remove ordering != 2 row
# file2.drop(['ordering'], axis = 1, inplace = True) # remove ordering column
# file2.drop(file2.loc[file2['region'].isin(['\\N'])].index, inplace = True) # remove region == '\\N' row
# file2.rename(columns={"titleId": "tconst"}, inplace = True) # rename titleId to tconst
# file2.to_csv("new.title.akas.csv", index = False) # row output

# title.basic.csv
# file3 = pd.read_csv("title.basics.csv") # read title.basics.csv
# file3.drop(['originalTitle', 'isAdult', 'endYear'], axis = 1, inplace = True) # remove originalTitle, isAdult, endYear column
# file3.drop(file3.loc[file3['startYear'] < '2000'].index, inplace = True) # remove startYear < 2000 row
# file3.drop(file3.loc[file3['startYear'].isin(['\\N'])].index, inplace = True) # remove startYear == '\\N' row
# file3.drop(file3.loc[file3['runtimeMinutes'].isin(['\\N'])].index, inplace = True) # remove runtimeMinutes == '\\N' row
# file3.drop(file3.loc[file3['genres'].isin(['\\N'])].index, inplace = True) # remove genres == '\\N' row
# file3.drop(~file3.loc[file3['titleType'].isin(['movie'])].index, inplace = True) # remove titleType != 'movie' row
# file3.drop(['titleType'], axis = 1, inplace = True) # remove titleType column
# file3.to_csv("new.title.basics.csv", index = False) # output

# title.crew.csv
# file4 = pd.read_csv("title.crew.csv") # read title.crew.csv
# file4.drop(file4.loc[file4['writers'].isin(['\\N'])].index, inplace = True) # remove writers == '\\N' row
# file4.to_csv("new.title.crew.csv", index = False) # output

# title.episode.csv
# file5 = pd.read_csv("title.episode.csv") # read title.episode.csv
# file5.drop(file5.loc[file5['seasonNumber'].isin(['\\N'])].index, inplace = True) # remove seasonNumber == '\\N' row
# file5.drop(file5.loc[file5['episodeNumber'].isin(['\\N'])].index, inplace = True) # remove episodeNumber == '\\N' row
# file5.to_csv("new.title.episode.csv", index = False) # output

# title.principals.csv
# file6 = pd.read_csv("title.principals.csv") # read title.principals.csv
# file6.drop(['job', 'characters'], axis = 1, inplace = True) # remove 'originalTitle', 'isAdult', 'endYear' column
# file6.drop(file6.loc[file6['category'].isin(['cinematographer', 'composer', 'self'])].index, inplace = True) #remove row
# file6.to_csv("new.title.principals.csv", index = False) # output

# title.ratings.csv
# file7 = pd.read_csv("title.ratings.csv") # read title.ratings.csv
# print(file7.loc[:, 'numVotes'].mean()) # print numVote average
# file7.drop(file7.loc[file7['numVotes'] < 1000].index, inplace = True) #remove numVotes < 1000 row
# file7.to_csv("new.title.ratings.csv", index = False) # output

