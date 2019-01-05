import data_manager as dm
import k_means_cluster_analysis as kmca
import graph as gr
import numpy as np
from rms_error_calc import min_dists, euclidian_rms_error, euclidian_mae_error

data = np.array(dm.select_data('homicide.csv', [0, 1]), dtype='float')
data = [[float(n)
        for n in item]
        for item in data]


tps_locations = [[-79.460830, 43.671080], [-79.486880, 43.694580], [-79.436680, 43.698330],
                 [-79.425980, 43.651300], [-79.362140, 43.651950], [-79.389720, 43.654210],
                 [-79.400660, 43.706060], [-79.309480, 43.714610], [-79.317300, 43.669180],
                 [-79.529180, 43.643110], [-79.583520, 43.743870], [-79.527470, 43.756750],
                 [-79.415090, 43.771730], [-79.350070, 43.751080], [-79.277110, 43.730810],
                 [-79.240010, 43.789380], [-79.174060, 43.770840]]


tps_divisions = 17
clusters, fit = kmca.k_m_clustering(tps_divisions, data)

graph = gr.Plot()
graph.graph_cluster(data, fit, clusters)

graph.graph_ps(tps_locations)

dists, _ = min_dists(clusters.tolist(), tps_locations.copy())
err2 = euclidian_rms_error(clusters.tolist(), tps_locations.copy())
err1 = euclidian_mae_error(clusters.tolist(), tps_locations.copy())
graph.add_arrows(dists)
graph.add_txt("RMS euclidian error is %s, \nMAE eucllidian error is %s" % (round(err2, 4), round(err1, 4)))
graph.display()
