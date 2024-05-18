import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("new_csv/vector.csv")

# 切割 train data 與 test data
# train_data = data[data['startYear'] < 2020]
# test_data = data[data['startYear'] >= 2020]
feature = data[['region', 'startYear', 'runtimeMinutes', 'genres', 'directors', 'writers', 'numVotes']]
label = data['averageRating']
X_train, X_test, y_train, y_test = train_test_split(feature, label, train_size=0.85)

# train data
# X_train = train_data[['region', 'startYear', 'runtimeMinutes', 'genres', 'directors', 'writers', 'numVotes']]
# y_train = train_data['averageRating']

# test data
# X_test = test_data[['region', 'startYear', 'runtimeMinutes', 'genres', 'directors', 'writers', 'numVotes']]
# y_test = test_data['averageRating']
tconst = data['tconst']
primaryTitle = data['primaryTitle']

""" 訓練模型 """

# 建立隨機森林
model = RandomForestRegressor(n_estimators=500)

# 訓練
model.fit(X_train, y_train)

# 預測
y_pred = model.predict(X_test)

""" 檢查模型是否良好 """

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
print('訓練集:',model.score(X_train,y_train))
print('測試集:',model.score(X_test,y_test))
print('特徵重要程度:',model.feature_importances_)

""" 畫圖 """

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue',s=5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.savefig('new_csv/result.png')
# plt.show()

""" 建立 csv """

# 建立包含 actual、predict、tconst和  primaryTitle 的DataFrame
# results = pd.DataFrame({'tconst': tconst, 'primaryTitle': primaryTitle, 'Actual': y_test, 'Predicted': y_pred})

# 印前十行
# print(results.head(10))

# if os.path.exists('new_csv/result.csv'):
#     os.remove('new_csv/result.csv')

# results.to_csv('new_csv/result.csv', index=False)