import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# İris veri setini CSV dosyasından yükle
iris_df = pd.read_csv('iris.csv')
X = iris_df.iloc[:, :-1].values  # Son sütunun hedef değişken olduğunu varsayıyoruz

# Elbow yöntemi ile optimal öbek sayısını belirle
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Elbow grafiğini çiz
plt.plot(range(1, 11), wcss)
plt.title('Elbow Yöntemi')
plt.xlabel('Öbek Sayısı')
plt.ylabel('WCSS')
plt.show()

# Elbow grafiğinden optimal öbek sayısının 3 olduğunu varsayalım
optimal_clusters = 3

# K-means algoritmasını İris veri setine uygula
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# Silhouette skorunu hesapla
silhouette_avg = silhouette_score(X, y_kmeans)
print(f'Silhouette Skoru: {silhouette_avg}')

# Öbekleri görselleştir
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Öbek 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Öbek 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Öbek 3')

# Öbek merkezlerini çiz
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Merkezler')
plt.title('İris Verisi Öbekleri')
plt.xlabel('Sepal Uzunluğu')
plt.ylabel('Sepal Genişliği')
plt.legend()
plt.show()
