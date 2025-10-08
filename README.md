# K-Means-IRIS-data

This study focuses on clustering operations performed on the Iris dataset using the K-Means algorithm, aiming to identify optimal cluster separation and evaluate the algorithm’s performance using the Elbow method. The main objective is to determine the ideal number of clusters and achieve accurate clustering results for the dataset.

DATASET AND PREPROCESSING

Iris Dataset:

SepalLengthCm: Sepal length (cm)

SepalWidthCm: Sepal width (cm)

PetalLengthCm: Petal length (cm)

PetalWidthCm: Petal width (cm)

Species: Species name (Setosa, Versicolor, Virginica)

The dataset consists of 150 samples, each containing the above features.

Data Cleaning and Preparation:

Unnecessary columns were removed.

Missing values were checked and cleaned.

K-MEANS ALGORITHM

Theoretical Background:
The K-Means algorithm divides data points into a specified number of clusters by grouping points that are closest to their cluster centroids. In this study, the Elbow method was used to determine the optimal number of clusters.

SILHOUETTE SCORE

The Silhouette score is a widely used metric to evaluate the performance of clustering algorithms. It measures how similar a data point is to its own cluster compared to other clusters. In other words, it assesses how well each point fits within its assigned cluster and how distinct it is from others.

Reasons for using the Silhouette score:

Cluster Separation: Indicates how well-separated and compact the clusters are. A higher score means better-defined clusters.

Interpretability: The score ranges from -1 to 1, where values close to 1 indicate well-clustered data, 0 indicates overlapping clusters, and values near -1 suggest incorrect clustering.

Determining the Optimal Number of Clusters: By comparing Silhouette scores across different cluster counts, the number yielding the highest score can be chosen as optimal.

The Silhouette score for each data point is computed as:

s=(b-a)/(max⁡(a,b))​


where:


a = Mean intra-cluster distance (average distance within the same cluster)

b = Mean nearest-cluster distance (average distance to the nearest neighboring cluster)

The overall Silhouette score is the mean of all individual scores and provides a global measure of clustering quality.

ELBOW METHOD

The Elbow method is a commonly used approach to determine the optimal number of clusters in K-Means. It uses the Within-Cluster Sum of Squares (WCSS) as a measure of compactness.

Steps of the Elbow Method:

Compute WCSS: Apply K-Means for a range of cluster numbers (typically 1 to 10) and compute the WCSS for each.

WCSS=∑_(k=1)^K▒∑_(i=1)^(n_k)▒〖||x_i-c_k ||〗^2 

K: Number of clusters
	​

n_k: Number of data points in cluster 


x_i: Data point


c_k: Cluster centroid

Plot the Elbow Graph:

X-axis: Number of clusters

Y-axis: WCSS value

Identify the Elbow Point:

The point where WCSS starts decreasing more slowly (the “elbow”) indicates the optimal number of clusters.

Advantages:

Simple and intuitive visualization

Fast and effective for initial cluster estimation

Widely applicable to various datasets

Disadvantages:

Subjective interpretation of the elbow point

May not show a clear elbow for all datasets

Can overestimate the optimal cluster count in high-dimensional data

MODEL IMPLEMENTATION

The Iris dataset was clustered using the K-Means algorithm, and the optimal number of clusters was determined via the Elbow method.

The Silhouette score was used as the primary performance metric.

MODEL TRAINING AND EVALUATION

Training Data: The entire dataset was used.

Model Training: The model was trained using the K-Means algorithm.

Prediction and Evaluation: The clustering results were evaluated, and the Silhouette score was calculated to assess performance.

##Elbow 

<img width="940" height="601" alt="image" src="https://github.com/user-attachments/assets/6722c9cf-59f5-4e62-a0a4-e5f727502b9a" />


##cluster



<img width="940" height="705" alt="image" src="https://github.com/user-attachments/assets/449a1596-1340-4674-964f-5201ba438375" />

