import math
from collections import defaultdict


class Vec(object):
    def __init__(self, vec):
        self.vec = defaultdict(lambda: 0, vec)

    def len(self):
        return math.sqrt(sum([x ** 2 for x in self.vec.values()]))

    def distance(self, other):
        keys = set(self.vec.keys()).intersection(other.vec.keys())
        if self.len() == 0 or other.len() == 0:
            return float('inf')

        return 1 - sum([self.vec[key] * other.vec[key] for key in keys]) / (self.len() * other.len())

    def __str__(self):
        return super(Vec, self).__str__()

    def __repr__(self):
        return str(self)
