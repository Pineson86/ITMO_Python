from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, adjusted_rand_score, homogeneity_score, v_measure_score
from sklearn.cluster import KMeans, AgglomerativeClustering, SpectralClustering, Birch, DBSCAN, MeanShift
import numpy as np

# Загружаем датасет
data = load_wine()
X = data.data
y_true = data.target  # Таргет для сравнения кластеров с реальными классами

# Стандартизация данных
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Определяем модели кластеризации
models = {
    "KMeans": KMeans(n_clusters=3, random_state=42),
    "Agglomerative": AgglomerativeClustering(n_clusters=3),
    "Spectral": SpectralClustering(n_clusters=3, random_state=42),
    "Birch": Birch(n_clusters=3),
    "MeanShift": MeanShift(),
    "DBSCAN": DBSCAN(eps=1.5, min_samples=5)
}

# Функция для расчета метрик
def calculate_metrics(model, X, y_true, name):
    labels_pred = model.fit_predict(X)
    n_clusters = len(np.unique(labels_pred))
    
    # Проверяем, есть ли хотя бы два кластера
    if n_clusters < 2:
        print(f"Модель {name} выделила только {n_clusters} кластер(ов). Метрики не вычисляются.")
        return {
            "Silhouette Score": None,
            "Adjusted Rand Index": None,
            "Homogeneity Score": None,
            "V-measure Score": None
        }
    
    return {
        "Silhouette Score": silhouette_score(X, labels_pred),
        "Adjusted Rand Index": adjusted_rand_score(y_true, labels_pred),
        "Homogeneity Score": homogeneity_score(y_true, labels_pred),
        "V-measure Score": v_measure_score(y_true, labels_pred)
    }

# Обучение и расчет метрик
results = {}
for name, model in models.items():
    results[name] = calculate_metrics(model, X, y_true, name)

# Вывод результатов
print("Результаты кластеризации:")
for model_name, metrics in results.items():
    print(f"\nМетрики для {model_name}:")
    for metric_name, value in metrics.items():
        if value is not None:
            print(f"  {metric_name}: {value:.4f}")
        else:
            print(f"  {metric_name}: Невозможно вычислить")
