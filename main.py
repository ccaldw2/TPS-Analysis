import data_manager as dm
import k_means_cluster_analysis as kmca
import graph as gr
import numpy as np

data = np.array(dm.select_data('homicide.csv', [0, 1]), dtype='float')
data = [[float(n)
        for n in item]
        for item in data]


tps_locations = [[-79.460830, 43.671080], [-79.486880, 43.694580], [-79.436680, 43.698330],
                 [-79.425980, 43.651300], [-79.362140, 43.651950], [-79.389720, 43.654210],
                 [-79.400660, 43.706060], [-79.309480, 43.714610], [-79.317300, 43.669180]]


tps_divisions = 17
clusters, fit = kmca.k_m_clustering(tps_divisions, data)

graph = gr.Plot()

graph.graph_cluster(data, fit, clusters)
graph.graph_ps(tps_locations)
graph.display()