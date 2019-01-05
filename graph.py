import matplotlib.pyplot as plt

class Plot:
    def __init__(self):
        self.plot = plt

    def graph_cluster(self, data, labels, means):
        xs = [n[0] for n in data]
        ys = [n[1] for n in data]

        self.plot.scatter(xs, ys, c=labels, s=100, alpha=0.5, cmap='tab20')
        plt.scatter(means[:, 0], means[:, 1], c='black', alpha=1, s=50)

    def graph_ps(self, data):
        xs = [n[0] for n in data]
        ys = [n[1] for n in data]
        self.plot.scatter(xs, ys, c='black', marker='^', alpha=1, s=50)

    def display(self):
        self.plot.show()

    def add_arrows(self, pairs):
        for pair in pairs:
            self.add_arrow(pair)

    def add_arrow(self, pair):
        x_base = pair[0][0]
        y_base = pair[0][1]
        dx = pair[1][0] - pair[0][0]
        dy = pair[1][1] - pair[0][1]
        self.plot.arrow(x_base, y_base, dx, dy, length_includes_head=True, color='grey')

    def add_txt(self, item):
        self.plot.text(-79.4, 43.6, s=item, color='black')
