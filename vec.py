import math
from collections import defaultdict


class Vec(object):
    def __init__(self, vec):
        self.vec = defaultdict(lambda: 0, vec)

    def normalize(self):
        length = self.len()
        for key, value in self.vec.items():
            self.vec[key] = value / length

        return self

    def len(self):
        return math.sqrt(sum([x ** 2 for x in self.vec.values()]))

    def euc_dist(self, other):
        keys = set(self.vec.keys()).union(other.vec.keys())
        return math.sqrt(sum([(self.vec[key] - other.vec[key]) ** 2 for key in keys]))

    def cos_dist(self, other):
        if self.len() == 0 or other.len() == 0:
            return float('inf')

        keys = set(self.vec.keys()).intersection(other.vec.keys())
        return 1 - sum([self.vec[key] * other.vec[key] for key in keys]) / (self.len() * other.len())

    def __str__(self):
        return '\n'.join(['{}: {}'.format(str(key), str(value)) for key, value in self.vec.items()])