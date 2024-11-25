import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error, explained_variance_score
from sklearn.model_selection import train_test_split

# Получение пути к директории, где находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Чтение данных из файлов
x_path = os.path.join(script_dir, 'x.csv')
y_path = os.path.join(script_dir, 'y.csv')
x = np.loadtxt(x_path, delimiter=',')  # Чтение файла x.csv
y = np.loadtxt(y_path, delimiter=',')  # Чтение файла y.csv

# Разделение данных на тренировочную и тестовую выборки
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Линейная регрессия по каждому признаку
metrics = []  # Для хранения метрик
for i in range(x.shape[1]):
    reg = LinearRegression()
    reg.fit(x_train[:, i].reshape(-1, 1), y_train)
    y_pred = reg.predict(x_test[:, i].reshape(-1, 1))
    
    metrics.append({
        'Model': f'Linear Regression Feature {i+1}',
        'R2_Score': r2_score(y_test, y_pred),
        'MSE': mean_squared_error(y_test, y_pred),
        'EVS': explained_variance_score(y_test, y_pred)
    })

# Множественная линейная регрессия
reg_multi = LinearRegression()
reg_multi.fit(x_train, y_train)
y_pred_multi = reg_multi.predict(x_test)

metrics.append({
    'Model': 'Multiple Linear Regression',
    'R2_Score': r2_score(y_test, y_pred_multi),
    'MSE': mean_squared_error(y_test, y_pred_multi),
    'EVS': explained_variance_score(y_test, y_pred_multi)
})

# Полиномиальная регрессия степени 2 и 3
for degree in [2, 3]:
    for i in range(x.shape[1]):
        poly = PolynomialFeatures(degree=degree)
        x_train_poly = poly.fit_transform(x_train[:, i].reshape(-1, 1))
        x_test_poly = poly.transform(x_test[:, i].reshape(-1, 1))

        reg_poly = LinearRegression()
        reg_poly.fit(x_train_poly, y_train)
        y_pred_poly = reg_poly.predict(x_test_poly)

        metrics.append({
            'Model': f'Polynomial Regression (Degree {degree}) Feature {i+1}',
            'R2_Score': r2_score(y_test, y_pred_poly),
            'MSE': mean_squared_error(y_test, y_pred_poly),
            'EVS': explained_variance_score(y_test, y_pred_poly)
        })

# Сводная таблица
results = pd.DataFrame(metrics)

# Сохранение таблицы в файл
results_path = os.path.join(script_dir, 'regression_metrics_summary.csv')
results.to_csv(results_path, index=False)
print('Анализ завершен, метрики записаны в таблицу, сохраненную в ту же папку, что и скрипт')