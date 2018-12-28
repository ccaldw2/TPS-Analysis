from sklearn.cluster import KMeans


def k_m_clustering(num_clusters, data):
    k_means = KMeans(num_clusters)

    fit_data = k_means.fit_predict(data)
    cluster_means = k_means.cluster_centers_

    return cluster_means, fit_data


