import data_manager as dm
import k_means_cluster_analysis as kmca
import graph as gr
import numpy as np

data = np.array(dm.select_data('homicide.csv', [0, 1]), dtype='float')
data = [[float(n)
        for n in item]
        for item in data]


tps_divisions = 17
clusters, fit = kmca.k_m_clustering(tps_divisions, data)
gr.graph_cluster(data, fit, clusters)
