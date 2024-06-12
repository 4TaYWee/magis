import time
import numpy as np

def k_means(data, k, max_iter=100):
  """
  Performs k-means clustering on the given data.

  Args:
    data: A numpy array of shape (n_samples, n_features) representing the data to be clustered.
    k: The number of clusters to create.
    max_iter: The maximum number of iterations to perform.

  Returns:
    A tuple containing:
      centroids: A numpy array of shape (k, n_features) representing the centroids of the clusters.
      labels: A numpy array of shape (n_samples,) representing the cluster label for each data point.
  """
  start_time = time.time()
  n_samples, n_features = data.shape

  # Initialize centroids randomly
  centroids = data[np.random.choice(n_samples, k, replace=False)]

  # Iterate until convergence or max_iter is reached
  for _ in range(max_iter):
    # Assign data points to the closest centroid
    labels = np.argmin(np.linalg.norm(data[:, np.newaxis] - centroids, axis=2), axis=1)

    # Update centroids as the mean of their assigned data points
    centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])

  execution_time = time.time() - start_time
  return centroids, labels, execution_time

# Sample data
data = np.array([[1, 1], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Perform k-means clustering with k=2 clusters
centroids, labels, execution_time = k_means(data, k=2)

print("Centroids:")
print(centroids)

print("Labels:")
print(labels)

print("Execution time:", execution_time, "seconds")
