from sklearn.cluster import KMeans
import numpy as np
import data_manager as dm

homicides = np.array(dm.select_data('Homicide.csv', [0, 1]))  # X & Y coordinates of reported homicide
num_divisions = 17

k_means = KMeans(n_clusters=num_divisions, init='k-means++')

k_means.fit(homicides)
print(k_means.cluster_centers_)