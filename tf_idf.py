# coding=utf-8
import math

from library import Document, Library
from vec import Vec


class Doc2Vec(object):
    def __init__(self, library):
        self.lib = library

    def tf(self, term, document):
        return document.vec[term]

    def idf(self, term):
        return math.log(float(self.lib.N) / self.lib.df(term), 2) if self.lib.df(term) != 0 else float('inf')

    def tf_idf(self, term, document):
        return self.tf(term, document) * self.idf(term)

    def doc2vec(self, document):
        return Vec([(term, self.tf_idf(term, document)) for term in document.words])


if __name__ == '__main__':
    print 'Initializing library...'
    lib = Library()
    d2v = Doc2Vec(lib)

    id1 = 1
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

    id2 = 40
    doc2 = u'O 40 procent zostanie podniesiona wkrótce w Rosji minimalna cena ' \
           u'wódki - poinformowało ministerstwo gospodarki.'

    doc1 = Document(id1, doc1)
    vec1 = d2v.doc2vec(doc1)
    vec1.normalize()

    doc2 = Document(id2, doc2)
    vec2 = d2v.doc2vec(doc2)
    vec2.normalize()

    print vec1.cos_dist(vec2)
