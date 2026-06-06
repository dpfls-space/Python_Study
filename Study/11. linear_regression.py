from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

#가상의 데이터 생성
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])

#데이터 분할
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=1130)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

#모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

#예측
y_pred = model.predict(X_test)
print("예측값: ", y_pred)