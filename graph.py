import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        self.plot = plt

    def graph_cluster(self, data, labels, means):
        xs = [n[0] for n in data]
        ys = [n[1] for n in data]

        self.plot.scatter(xs, ys, c=labels, s=25, cmap='tab20')
        plt.scatter(means[:, 0], means[:, 1], c='black', alpha=0.5, s=200)

    def graph_ps(self, data):
        xs = [n[0] for n in data]
        ys = [n[1] for n in data]
        self.plot.scatter(xs, ys, c='grey', alpha=0.5, s=200)

    def display(self):
        self.plot.show()
