import pandas as pd
import os

file1 = pd.read_csv("new_csv/new.akas_basics_crew_ratings.csv") # read akas_basics_crew_ratings.csv
file2 = pd.read_csv("new_csv/new.name.basics.csv") # read new.name.basics.csv
file3 = pd.read_csv("new_csv/new.title.principals.csv") # read new.title.principals.csv
count = 0

########################################################################################
""" Region"""

# 統計地區及次數，放入 region_rate
region_rate = {}

for i in range(len(file1)):
    region = file1.iloc[i]['region']
    rating = file1.iloc[i]['averageRating']
    if region in region_rate:
        region_rate[region]['total'] += rating
        region_rate[region]['count'] += 1
    else:
        region_rate[region] = {'total': rating, 'count': 1}


# 計算各地區的平均評分
avg_ratings = {}
for region, values in region_rate.items():
    average_rating = values['total'] / values['count']
    avg_ratings[region] = average_rating

# 更換 region 為數值
file1['region'] = file1['region'].map(avg_ratings)

########################################################################################
""" Genres """

# 統計 gemres 次數，放入 genres_rate
genres_rate = {}
for i in range(len(file1)):
    genres = file1.iloc[i]['genres'].split(',')
    rating = file1.iloc[i]['averageRating']
    for genre in genres:
        genre = genre.strip()
        if genre in genres_rate:
            genres_rate[genre]['total'] += rating
            genres_rate[genre]['count'] += 1
        else:
            genres_rate[genre] = {'total': rating, 'count': 1}

# 計算每個 genre 的平均評分
avg_ratings = {}
for genre, values in genres_rate.items():
    avg_rating = values['total'] / values['count']
    avg_ratings[genre] = avg_rating

# 每部電影平均評分
avg_movie = []
for i in range(len(file1)):
    genres = file1.iloc[i]['genres'].split(',')
    avg_rating_sum = 0
    for genre in genres:
        avg_rating_sum += avg_ratings[genre.strip()] # 平均和
    avg_rating = avg_rating_sum / len(genres)
    avg_movie.append(avg_rating)

# 更換 genres 為數值
file1['genres'] = avg_movie

########################################################################################
""" Directors and Actor """

# 電影對應的評分存在 tconst_rate (字典)

tconst_rate = {}
for i in range(len(file1)):
    tconst_rate[file1.iloc[i]['tconst']] = file1.iloc[i]['averageRating']

#讀取 file2 每一列，並新增工作人員的 rate 存在新的 csv

for i in range(len(file2)):
    sum = 0
    kftitles = file2.iloc[i]['knownForTitles'].split(',')
    for movie in kftitles:
        if movie in tconst_rate:
            sum += tconst_rate[movie]
        # else:
        #     print(file2.iloc[i]['nconst'],movie)

    avg_rating = sum / len(kftitles)
    file2.at[i, 'rate'] = avg_rating


# 如果 Directors_Actor_Writer.csv 存在，則刪掉
if os.path.exists('new_csv/Directors_Actor_Writer.csv'):
    os.remove('new_csv/Directors_Actor_Writer.csv')

# 保存新的 CSV
file2.to_csv('new_csv/Directors_Actor_Writer.csv', index=False)

""" 工作人員對應的評分存在 nconst_rate (字典) """

nconst_rate = {}
for i in range(len(file2)):
    nconst_rate[file2.iloc[i]['nconst']] = file2.iloc[i]['rate']

for i in range(len(file1)):
    directors = file1.iloc[i]['directors'].split(',')
    sum = 0
    for director in directors:
        if director in nconst_rate:
            sum += nconst_rate[director]
    avg_rating = sum / len(directors)
    file1.at[i, 'directors'] = avg_rating

########################################################################################
""" Writer """

for i in range(len(file1)):
    writers = file1.iloc[i]['writers'].split(',')
    sum = 0
    for writer in writers:
        if writer in nconst_rate:
            sum += nconst_rate[writer]
    avg_rating = sum / len(writers)
    file1.at[i, 'writers'] = avg_rating
########################################################################################
""" actor """

for i in range(len(file1)):
    actors = file1.iloc[i]['actor'].split(',')
    sum = 0
    for actor in actors:
        if actor in nconst_rate:
            sum += nconst_rate[actor]
    avg_rating = sum / len(actors)
    file1.at[i, 'actor'] = avg_rating
    
########################################################################################
""" actress """

for i in range(len(file1)):
    actresses = file1.iloc[i]['actress'].split(',')
    sum = 0
    for actress in actresses:
        if actress in nconst_rate:
            sum += nconst_rate[writer]
    avg_rating = sum / len(actresses)
    file1.at[i, 'actress'] = avg_rating
########################################################################################
""" producer """

for i in range(len(file1)):
    producers = file1.iloc[i]['producer'].split(',')
    sum = 0
    for producer in producers:
        if producer in nconst_rate:
            sum += nconst_rate[producer]
    avg_rating = sum / len(producers)
    file1.at[i, 'producer'] = avg_rating

########################################################################################
""" 存檔 """

# 如果 vector.csv 存在，則刪掉
if os.path.exists('new_csv/vector.csv'):
    os.remove('new_csv/vector.csv')

# file1.drop(file1.loc[file1['actor'].isin([0.0]) | file1['actress'].isin([0.0])].index, inplace=True) # remove nconst not include in new.title.principals['nconst'] row or # remove primaryProfession == r'\N' row

# 保存新的 CSV
file1.to_csv('new_csv/vector.csv', index=False)

