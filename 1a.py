# coding=utf-8
import sys

from library import Document, Library
from tf_idf import Doc2Vec

alpha = 0.85

if __name__ == '__main__':
    print 'Initializing library...'
    lib = Library()
    d2v = Doc2Vec(lib)

    try:
        id = int(sys.argv[1])
        input_doc = lib.doc(id)
    except ValueError:
        id = None
        input_doc = Document(id, sys.argv[1])

    input_vec = d2v.doc2vec(input_doc)
    input_vec.normalize()

    print input_doc.text

    for doc in lib.documents():
        if doc.id == input_doc.id: continue

        vec = d2v.doc2vec(doc)
        vec.normalize()
        dist = vec.cos_dist(input_vec)

        if dist < alpha:
            print 'id: {}, distance: {}'.format(doc.id, dist)
            print doc.text
