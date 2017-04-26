# coding=utf-8
from collections import Counter

from graph import Graph
from library import Document, Library
from vec import Vec

print 'Initializing library...'
lib = Library()


class DistanceGraph(Graph):
    def __init__(self, order, document):
        super(DistanceGraph, self).__init__(directed=True)
        self.k = order
        self.document = document

        self.init_graph()

    def init_graph(self):
        for i in xrange(len(self.document.words)):
            window = self.document.words[i:i + self.k + 1]
            for word in window:
                self.add(window[0], word)

    def svm(self):
        counts = {word: Counter(self._graph[word]) for word in self._graph.keys()}
        return Vec([((a, b), counts[a][b]) for a in counts.keys() for b in counts[a].keys()])


if __name__ == '__main__':
    doc1 = u'O 40 procent zostanie podniesiona wkrótce w Rosji minimalna cena ' \
           u'wódki - poinformowało ministerstwo gospodarki.'

    doc1 = Document(40, doc1)
    graph1 = DistanceGraph(10, doc1)
    vec1 = graph1.svm()

    print 'Calculating similarity...'
    for doc in lib.documents():
        if doc.id == doc1.id: continue

        graph = DistanceGraph(10, doc)
        vec = graph.svm()
        dist = vec.cos_dist(vec1)

        if dist < 0.95:
            print dist
            print doc.text
