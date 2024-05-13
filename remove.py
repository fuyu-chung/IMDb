import pandas as pd
import numpy as np

# name.basics.csv
# file1 = pd.read_csv("csv/name.basics.csv") # read name.basics.csv
# file1.drop(['birthYear', 'deathYear'], axis=1, inplace=True) #remove birthYear, deathYear column
# file6 = pd.read_csv("new_csv/new.title.principals.csv")
# nconst = file6['nconst'].unique().tolist() # save all unique nconst value in new.title.principals.csv
# file1.drop(file1.loc[~file1['nconst'].isin(nconst) | file1['primaryProfession'].isin([r'\N']) | file1['knownForTitles'].isin([r'\N'])].index, inplace=True) # remove nconst not include in new.title.principals['nconst'] row or # remove primaryProfession == r'\N' row

# profession = ['actor', 'actress', 'director', 'editor', 'producer', 'writer']
# file1[['primaryProfession1', 'primaryProfession2','primaryProfession3']] =(file1['primaryProfession'].str.split(',',expand=True)) # split primaryProfession to three column
# file1['primaryProfession1'].loc[~file1['primaryProfession1'].isin(profession)] = '' # if primaryProfession1 is not in profession, set its value to ''
# file1['primaryProfession2'].loc[~file1['primaryProfession2'].isin(profession)] = '' 
# file1['primaryProfession3'].loc[~file1['primaryProfession3'].isin(profession)] = ''
# file1["primaryProfession"] = file1["primaryProfession1"] + ',' + file1["primaryProfession2"] + ',' + file1["primaryProfession3"] # combine three column of primaryProfession
# file1.replace(to_replace={'primaryProfession': [r',{2,}']}, value=',', regex=True, inplace=True) # if the list include two or more comma, replace the value to one comma
# file1.replace(to_replace={'primaryProfession': [r'^,', r',$']}, value='', regex=True, inplace=True) # if the list start at comma or end with comma, replace the value to ''
# file1.drop(file1.loc[file1['primaryProfession'].isin([''])].index, inplace=True)
# file1.drop(['primaryProfession1', 'primaryProfession2', 'primaryProfession3'], axis=1, inplace=True)

# file1[['knownForTitles1', 'knownForTitles2','knownForTitles3', 'knownForTitles4']] =(file1['knownForTitles'] + (3 - file1['knownForTitles'].str.count(',')).map(lambda x : x * ',')).str.split(',',expand=True) # 
# file8 = pd.read_csv("csv/akas_basics_crew_ratings.csv")
# tconst = file8['tconst'].tolist()
# file1['knownForTitles1'].loc[~file1['knownForTitles1'].isin(tconst)] = ''
# file1['knownForTitles2'].loc[~file1['knownForTitles2'].isin(tconst)] = ''
# file1['knownForTitles3'].loc[~file1['knownForTitles3'].isin(tconst)] = ''
# file1['knownForTitles4'].loc[~file1['knownForTitles4'].isin(tconst)] = ''
# file1["knownForTitles"] = file1["knownForTitles1"] + ',' + file1["knownForTitles2"] + ',' + file1["knownForTitles3"] + ','+ file1["knownForTitles4"]
# file1.replace(to_replace={'knownForTitles': [r',{2,}']}, value=',', regex=True, inplace=True)
# file1.replace(to_replace={'knownForTitles': [r'^,', r',$']}, value='', regex=True, inplace=True)
# file1.drop(file1.loc[file1['knownForTitles'].isin([''])].index, inplace=True)
# file1.drop(['knownForTitles1', 'knownForTitles2', 'knownForTitles3', 'knownForTitles4'], axis=1, inplace=True)
# file1.to_csv("new.name.basics.csv", index=False) # output

# title.akas.csv
# file2 = pd.read_csv("csv/title.akas.csv")
# file2.rename(columns={"titleId": "tconst"}, inplace=True) # rename titleId to tconst
# file3 = pd.read_csv("new_csv/new.title.basics.csv")
# tconst = file3['tconst'].tolist()
# file2.drop(['title', 'language', 'types', 'attributes', 'isOriginalTitle'], axis=1, inplace=True)
# file2.drop(file2.loc[file2['ordering'] != 2].index, inplace=True) # remove ordering != 2 row
# file2.drop(file2.loc[file2['region'].isin([r'\N']) | ~file2['tconst'].isin(tconst)].index, inplace=True) # remove ordering != 2 row
# file2.drop(['ordering'], axis=1, inplace=True)
# file2.to_csv("new.title.akas.csv", index=False)

# # title.basic.csv
# file3 = pd.read_csv("csv/title.basics.csv")
# file3.drop(['originalTitle', 'isAdult', 'endYear'], axis=1, inplace=True)
# file3.drop(file3.loc[file3['startYear'] < '2000'].index, inplace=True) # remove startYear < 2000 row
# file3.drop(file3.loc[file3['startYear'].isin([r'\N']) | file3['runtimeMinutes'].isin([r'\N']) | file3['genres'].isin([r'\N']) | ~file3['titleType'].isin(['movie'])].index, inplace=True)
# file3.drop(['titleType'], axis=1, inplace=True)
# file3.to_csv("new.title.basics.csv", index=False)

# title.crew.csv
# file4 = pd.read_csv("csv/title.crew.csv")
# file3 = pd.read_csv("new_csv/new.title.basics.csv")
# tconst = file3['tconst'].tolist()
# file4.drop(file4.loc[file4['directors'].isin([r'\N']) | file4['writers'].isin([r'\N']) | ~file4['tconst'].isin(tconst)].index, inplace=True)
# file4.to_csv("new.title.crew.csv", index=False)

# title.episode.csv
# file5 = pd.read_csv("csv/title.episode.csv") # read title.episode.csv
# file3 = pd.read_csv("new_csv/new.title.basics.csv")
# tconst = file3['tconst'].tolist()
# file5.drop(file5.loc[file5['seasonNumber'].isin([r'\N']) | file5['episodeNumber'].isin([r'\N']) | ~file5['tconst'].isin(tconst)].index, inplace=True)
# file5.to_csv("new.title.episode.csv", index=False)

# title.principals.csv
# file6 = pd.read_csv("csv/title.principals.csv") # read title.principals.csv
# file8 = pd.read_csv("csv/akas_basics_crew_ratings.csv")
# tconst = file8['tconst'].tolist()
# file6.drop(['job', 'characters'], axis=1, inplace=True)
# profession = ['actor', 'actress', 'director', 'editor', 'producer', 'writer']
# file6.drop(file6.loc[~file6['category'].isin(profession) | ~file6['tconst'].isin(tconst)].index, inplace=True)
# file6.to_csv("new.title.principals.csv", index=False)

# title.ratings.csv
# file7 = pd.read_csv("csv/title.ratings.csv")
# file3 = pd.read_csv("new_csv/new.title.basics.csv")
# tconst = file3['tconst'].tolist()
# print(file7.loc[:, 'numVotes'].mean()) # print numVote average
# file7.drop(file7.loc[file7['numVotes'] < 1000].index, inplace=True)
# file7.drop(file7.loc[~file7['tconst'].isin(tconst)].index, inplace=True)
# file7.to_csv("new.title.ratings.csv", index=False)

# akas_basics_crew_ratings.csv
# file8 = pd.read_csv("csv/akas_basics_crew_ratings.csv")
# file8_director_dic = dict()
# file8_writer_dic = dict()

# for i, row in file8.iterrows():
#     file8_i_director_set = set()
#     file8_i_writer_set = set()
#     for director in row['directors'].split(','):
#         file8_i_director_set.add(director)
#     file8_director_dic[row['tconst']] = file8_i_director_set
    
#     for writer in row['writers'].split(','):
#         file8_i_writer_set.add(writer)
#     file8_writer_dic[row['tconst']] = file8_i_writer_set

# new_directors_list = []
# new_writers_list = []

# file9 = pd.read_csv("new_csv/new.name.basics.csv")
# file9_set = set(file9['nconst'])

# for file8_i_dic_key, file8_i_director_set in file8_director_dic.items():
#     file8_i_director_set_copy = set(file8_i_director_set)
#     for file8_i_director in file8_i_director_set_copy:
#         if file8_i_director not in file9_set:
#             file8_director_dic[file8_i_dic_key].remove(file8_i_director)
#     new_directors_list.append(','.join(file8_i_director_set))
            
# for file8_i_dic_key, file8_i_writer_set in file8_writer_dic.items():
#     file8_i_writer_set_copy = set(file8_i_writer_set)
#     for file8_i_writer in file8_i_writer_set_copy:
#         if file8_i_writer not in file9_set:
#             file8_writer_dic[file8_i_dic_key].remove(file8_i_writer)
#     new_writers_list.append(','.join(file8_i_writer_set))

# file8.drop(['directors', 'writers'], axis=1, inplace=True)
# file8.insert(6, "directors", new_directors_list, False)
# file8.insert(7, "writers", new_writers_list, False)
# file8.drop(file8.loc[file8['directors'].isin(['']) | file8['writers'].isin([''])].index, inplace=True)
# file8.to_csv("new.akas_basics_crew_ratings.csv", index=False)
