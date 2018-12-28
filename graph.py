import matplotlib.pyplot as plt


def graph_cluster(data, labels, means):
    xs = [n[0] for n in data]
    ys = [n[1] for n in data]

    plt.scatter(xs, ys, c=labels, s=25, cmap='tab20')
    plt.scatter(means[:, 0], means[:, 1], c='black', alpha=0.5, s=200)
    plt.show()
