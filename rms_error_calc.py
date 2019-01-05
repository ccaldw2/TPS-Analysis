from functools import reduce
import math


# this is such a brute force way to do this calculation but it's fine given our data size
# todo: find algorithms that optimise to reduce the largest distances as much as possible as an alternative evaluation
def min_dist(means, locs):

    smallest = float('inf')
    smallest_pair = [None, None]
    for means_i in means:
        for locs_j in locs:
            if distance(means_i, locs_j) < smallest:
                smallest = distance(means_i, locs_j)
                smallest_pair = [means_i, locs_j]
    return smallest_pair


def min_dists(means, locs):
    pairs = []

    rng = len(means)

    for _ in range(rng):
        pair = min_dist(means, locs)
        pairs.append(pair)
        means.remove(pair[0])
        locs.remove(pair[1])

    distances = [distance(i[0], i[1]) for i in pairs]
    return pairs, distances


def distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


# normally rms e measures how far some dependent variable y is from its prediction,
# but in this case we're measuring the actual police stations against the optimised location
# according to k-means, meaning we have to compute distance from predictions in 2-space using pythagorean theorem
def euclidian_rms_error(a, b):
    _, dists = min_dists(a, b)

    total_squared_dist = sum([item ** 2 for item in dists])
    mean_squared_dist = total_squared_dist / len(dists)
    return math.sqrt(mean_squared_dist) # root mean square


def euclidian_mae_error(a, b):
    _, dists = min_dists(a, b)
    total_abs_dist = sum(dists)
    mean_dist = total_abs_dist / len(dists)
    return mean_dist