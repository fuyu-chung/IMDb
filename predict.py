import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import os
import joblib

# 載入模型
model = joblib.load('random_forest_model.pkl')

# 讀取 predict data
data = pd.read_csv("new_csv/vector.csv")
data = data[data['startYear'] == 2024]
X_test = data[['tconst','primaryTitle', 'genres', 'runtimeMinutes', 'directors', 'writers', 'numVotes', 'actor', 'producer']]
y_test = data['averageRating']

# 保留 tconst, primaryTitle
metadata = data[['tconst', 'primaryTitle']]

# 分離 train 和 test 中的 tconst, primaryTitle
X_test_meta = X_test[['tconst', 'primaryTitle']]

# 刪除 train 和 test 中的 tconst, primaryTitle
X_test = X_test.drop(columns=['tconst', 'primaryTitle'])

# 預測 
y_pred = model.predict(X_test)

# """ 檢查模型是否良好 """

mse = mean_squared_error(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print('測試集:',model.score(X_test,y_test))
# print('特徵重要程度:',model.feature_importances_)

""" 畫圖 """

# plt.figure(figsize=(8, 6))
# plt.scatter(y_test, y_pred, color='blue',s=5)
# plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
# plt.xlabel('Actual')
# plt.ylabel('Predicted')
# plt.savefig('new_csv/pred.png')
# plt.show()

""" 建立 predict.csv """

# 建立包含 actual、predict、tconst 和  primaryTitle 的DataFrame
val = pd.DataFrame({
    'tconst': X_test_meta['tconst'],
    'primaryTitle': X_test_meta['primaryTitle'],
    # 'Actual': y_test,
    'Predicted': y_pred
})

# 印前十行
# print(results.head(10))

# if os.path.exists('new_csv/result.csv'):
#     os.remove('new_csv/result.csv')

val.to_csv('new_csv/pred.csv', index=False)
print('finish')