import matplotlib.pyplot as plt
from k_means_cluster_analysis import k_m_clustering
import data_manager as dm

data = dm.select_data('homicide.csv', [0, 1])

tps_divisions = 17

clusters, fit = k_m_clustering(tps_divisions, data)

cluster_xs = [float(n[0]) for n in clusters]  # converted to float because data manager wrapper class returns strings
cluster_ys = [float(n[1]) for n in clusters]

plt.scatter(cluster_xs, cluster_ys, label='s')

plt.show()
