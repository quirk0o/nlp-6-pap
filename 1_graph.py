# coding=utf-8
import sys

from library import Document, Library
from distance_graph import DistanceGraph

alpha = 0.95

if __name__ == '__main__':
    print 'Initializing library...'
    lib = Library()

    try:
        id = int(sys.argv[3])
        input_doc = lib.doc(id)
    except ValueError:
        id = None
        input_doc = Document(id, sys.argv[3])

    k = int(sys.argv[1])
    alpha = float(sys.argv[2])

    input_graph = DistanceGraph(k, input_doc)
    input_vec = input_graph.svm()
    input_vec.normalize()

    print input_doc.text

    for doc in lib.documents():
        if doc.id == input_doc.id: continue

        graph = DistanceGraph(k, doc)
        vec = graph.svm()
        dist = vec.cos_dist(input_vec)

        if dist < alpha:
            print 'id: {}, distance: {}'.format(doc.id, dist)
            print doc.text
