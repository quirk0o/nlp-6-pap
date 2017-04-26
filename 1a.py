# coding=utf-8
import sys

from library import Document
from tf_idf import doc2vec, lib

alpha = 0.85

if __name__ == '__main__':
    try:
        id = int(sys.argv[1])
        input_doc = lib.doc(id)
    except ValueError:
        id = None
        input_doc = Document(id, sys.argv[1])

    input_vec = doc2vec(input_doc)
    input_vec.normalize()

    print input_doc.text

    for doc in lib.documents():
        if doc.id == input_doc.id: continue

        vec = doc2vec(doc)
        vec.normalize()
        dist = vec.cos_dist(input_vec)

        if dist < alpha:
            print 'id: {}, distance: {}'.format(doc.id, dist)
            print doc.text
