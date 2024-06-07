import pandas as pd
pd.options.mode.chained_assignment = None

file6 = pd.read_csv("new_csv/new.title.principals.csv")

actor = file6.loc[file6['category'] == 'actor']
actor.to_csv("new_csv/actor.csv", index=False)
actor.drop(['category'], axis=1, inplace=True)
actor.rename(columns={"nconst": "actor"}, inplace=True)
actor.to_csv("new_csv/actor.csv", index=False)

actress = file6.loc[file6['category'] == 'actress']
actress.to_csv("new_csv/actress.csv", index=False)
actress.drop(['category'], axis=1, inplace=True)
actress.rename(columns={"nconst": "actress"}, inplace=True)
actress.to_csv("new_csv/actress.csv", index=False)

producer = file6.loc[file6['category'] == 'producer']
producer.to_csv("new_csv/producer.csv", index=False)
producer.drop(['category'], axis=1, inplace=True)
producer.rename(columns={"nconst": "producer"}, inplace=True)
producer.to_csv("new_csv/producer.csv", index=False)