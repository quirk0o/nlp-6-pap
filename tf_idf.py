# coding=utf-8
import math

from library import Document, Library
from vec import Vec

print 'Initializing library...'
lib = Library()


def tf(term, document):
    return document.vec[term]


def idf(term):
    return math.log(float(lib.N) / lib.df(term), 2) if lib.df(term) != 0 else float('inf')


def tf_idf(term, document):
    return tf(term, document) * idf(term)


def doc2vec(document):
    return Vec([(term, tf_idf(term, document)) for term in document.words])


if __name__ == '__main__':
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

    doc2 = Document(id2, doc2)
    vec2 = doc2vec(doc2)

    print 'Calculating similarity...'
    for doc in lib.documents():
        if doc.id == doc2.id: continue
        
        vec = doc2vec(doc)
        dist = vec.distance(vec2)
        if dist < 0.82:
            print dist
            print doc.text
