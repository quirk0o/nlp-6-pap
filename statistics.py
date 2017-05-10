
class StatisticsService(object):
    def __init__(self, all_samples=None, classification=None, guesses=None):
        self.all_samples = all_samples
        self.classification = classification
        self.guesses = guesses

    def true_positives(self):
        return [x for x in self.guesses if x in self.classification]

    def true_negatives(self):
        return [x for x in self.all_samples if x not in self.guesses and x not in self.classification]

    def precision(self):
        all_positives = len(self.guesses)
        if all_positives == 0:
            return 0
        return float(len(self.true_positives())) / float(all_positives)

    def recall(self):
        return float(len(self.true_positives())) / len(self.classification)

    def f1(self):
        p = self.precision()
        r = self.recall()
        return 2 * p * r / (p + r)

    def accuracy(self):
        return float(len(self.true_positives() + self.true_negatives())) / len(self.all_samples)


if __name__ == '__main__':
    statistics = StatisticsService(all_samples=[1, 2, 3, 4, 5, 6, 7], classification=[1, 2, 3, 4, 5], guesses=[1, 2, 3, 6])
    print statistics.precision()
    print statistics.recall()
    print statistics.f1()
    print statistics.accuracy()

    statistics = StatisticsService(all_samples=[1, 2, 3, 4, 5, 6, 7], classification=[1, 2, 3, 4, 5], guesses=[1, 2, 3, 4, 5])
    print statistics.precision()
    print statistics.recall()
    print statistics.f1()
    print statistics.accuracy()