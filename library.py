# coding=utf-8
import codecs
import os
import re
from collections import defaultdict, Counter

from dictionary import basic_form
from vec import Vec
from preprocessor import clean_corpus

LIBRARY_FILENAME = 'data/pap.txt'
LIBRARY_CACHE_FILENAME = 'cache/df.txt'
DOCUMENT_SEP = '#(\d+)'


class Document(object):
    def __init__(self, id, document):
        self.id = id
        self.text = document
        self.words = [basic_form(word) for word in clean_corpus(document)]
        self.vec = Counter(self.words)


class Library(object):
    def __init__(self):
        corpus = codecs.open(LIBRARY_FILENAME, encoding='utf-8').read()
        documents = re.split(DOCUMENT_SEP, corpus)
        ids = [int(id) for id in documents[1::2]]
        documents = documents[0::2]

        self._documents = dict([(id, Document(id, doc)) for id, doc in zip(ids, documents) if doc])
        self.N = len(documents)

        self.load_df()

    def load_df(self):
        if os.path.isfile(LIBRARY_CACHE_FILENAME):
            with codecs.open(LIBRARY_CACHE_FILENAME, encoding='utf-8') as cache_file:
                entries = [line.split(':') for line in cache_file.readlines()]
                self._df = defaultdict(
                    lambda: 0,
                    [(key, int(value)) for key, value in entries]
                )
        else:
            self._df = Counter([word for doc in self._documents.values() for word in set(doc.words)])

    def doc(self, id):
        return self._documents[id]

    def documents(self):
        return self._documents.values()

    def df(self, term):
        return self._df[term]

    def dump_df(self):
        with codecs.open(LIBRARY_CACHE_FILENAME, mode='w', encoding='utf-8') as cache_file:
            for key, df in self._df.items():
                cache_file.write(key)
                cache_file.write(':')
                cache_file.write(str(df))
                cache_file.write('\n')


if __name__ == '__main__':
    print 'Initializing library...'
    lib = Library()

    print lib._documents.items()[:10]
    print lib._df.items()[:10]
    print lib.N
