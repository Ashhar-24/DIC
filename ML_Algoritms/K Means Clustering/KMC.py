import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits        # dataset from sklearn
from sklearn.cluster import KMeans
from sklearn import metrics

digits = load_digits()
data = scale(digits.data)                # scale the data to make it easier to work with (0-1) range to simplify calculations and make training easier and more accurate.
y = digits.target

k= 10                                           # number of clusters
samples, features = data.shape                  # 1797 samples, 64 features (8x8 pixels)

def bench_k_means(estimator, name, data):       # function to print out the results of the KMC algorithm 
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))
    
clf = KMeans(n_clusters=k, init="random", n_init=10)     # KMC algorithm with 10 clusters, random initialization, and 10 iterations for each run of the algorithm 
bench_k_means(clf, "1", data)                            # print out the results of the KMC algorithm 
