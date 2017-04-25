# coding=utf-8
import codecs
import re
from collections import defaultdict, Counter

from dictionary import basic_form
from lvec import LVec
from preprocessor import clean_corpus

LIBRARY_FILENAME = 'data/pap.txt'
LIBRARY_CACHE_FILENAME = 'cache/pap.txt'
DOCUMENT_SEP = '#(\d+)'


class Document(object):
    def __init__(self, id, document):
        self.id = id
        self.words = [basic_form(word) for word in clean_corpus(document)]
        self.vec = Counter(self.words)


class Library(object):
    def __init__(self):
        corpus = codecs.open(LIBRARY_FILENAME, encoding='utf-8').read()
        documents = re.split(DOCUMENT_SEP, corpus)
        ids = [int(id) for id in documents[1::2]]

        self.__documents__ = dict([(id, Document(id, doc)) for id, doc in zip(ids, documents[0::2]) if doc])
        self.__df__ = Counter([word for doc in self.__documents__.values() for word in set(doc.words)])
        self.N = len(documents)

    def doc(self, id):
        return self.__documents__[id]

    def df(self, term):
        return self.__df__[term]

if __name__ == '__main__':
    print 'Initializing library...'
    lib = Library()

    print lib.__documents__[:10]
    print lib.__df__.items()[:10]
    print lib.N
