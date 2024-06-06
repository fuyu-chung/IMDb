import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split

data = pd.read_csv("new_csv/vector.csv")
# 切割 train data 與 test data

feature = data[['tconst','primaryTitle','region', 'startYear', 'genres', 'runtimeMinutes', 'directors', 'writers', 'numVotes']]
label = data['averageRating']

# 保留 tconst, primaryTitle
metadata = data[['tconst', 'primaryTitle']]
X_train, X_test, y_train, y_test = train_test_split(feature, label, train_size=0.9)

# 分離 train 和 test 中的 tconst, primaryTitle
X_train_meta = X_train[['tconst', 'primaryTitle']]
X_test_meta = X_test[['tconst', 'primaryTitle']]

# 刪除 train 和 test 中的 tconst, primaryTitle
X_train = X_train.drop(columns=['tconst', 'primaryTitle'])
X_test = X_test.drop(columns=['tconst', 'primaryTitle'])

# """ 訓練模型 """

# 建立隨機森林
model = RandomForestRegressor(n_estimators=500)

# 訓練
model.fit(X_train, y_train)

# 預測
y_pred = model.predict(X_test)

# """ 檢查模型是否良好 """

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
plt.show()

""" 建立 csv """

# 建立包含 actual、predict、tconst和  primaryTitle 的DataFrame
results = pd.DataFrame({
    'tconst': X_test_meta['tconst'],
    'primaryTitle': X_test_meta['primaryTitle'],
    'Actual': y_test,
    'Predicted': y_pred
})

# 印前十行
print(results.head(10))

if os.path.exists('new_csv/result.csv'):
    os.remove('new_csv/result.csv')

results.to_csv('new_csv/result.csv', index=False)