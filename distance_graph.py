# coding=utf-8
from collections import Counter

from graph import Graph
from library import Document
from vec import Vec


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
    doc1 = u'W nocy ze środy na czwartek zmarł po długiej i ciężkiej chorobie ' \
           u'minister kultury i dziedzictwa narodowego Andrzej Zakrzewski. ' \
           u'Miał 59 lat. Z wykształcenia prawnik, był historykiem, badaczem ' \
           u'historii, m.in. II Rzeczypospolitej. Przez wiele lat pracował w ' \
           u'Instytucie Historii PAN. ' \
           u'W latach 1991-95 był wysokim rangą urzędnikiem w Kancelarii ' \
           u'Prezydenta i jednym z najbliższych współpracowników Lecha ' \
           u'Wałęsy. W 1997 roku kandydował do Sejmu z list AWS. Jako poseł ' \
           u'tego ugrupowania stanął na czele Komisji Łączności z Polakami za ' \
           u'Granicą. Był członkiem Ruchu Stu, a od marca 1998 r. - ' \
           u'Stronnictwa Konserwatywno-Ludowego.'

    graph = DistanceGraph(3, Document(1, doc1))
    print graph.svm()