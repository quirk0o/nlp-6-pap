# coding=utf-8
import sys
from collections import Counter

from library import Document, Library
from tf_idf import Doc2Vec
from distance_graph import DistanceGraph

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

    print 'Preparing vectors...'
    input_tf_idf = d2v.doc2vec(input_doc).normalize()

    input_graphs = [DistanceGraph(k, input_doc) for k in xrange(2, 5)]
    input_svms = [graph.svm().normalize() for graph in input_graphs]

    print input_doc.text

    for doc in lib.documents():
        vec = d2v.doc2vec(doc)
        vec.normalize()
        doc.tf_idf = vec

        graphs = [(k, DistanceGraph(k, doc)) for k in xrange(2, 5)]
        doc.svm = {k: graph.svm() for k, graph in graphs}

    print 'Calculating similarity...'
    results = Counter()

    current_results = {}
    for doc in lib.documents():
        if doc.id == id: continue

        dist = input_tf_idf.cos_dist(doc.tf_idf)
        current_results[doc.id] = dist

    results.update(sorted(current_results, key=current_results.get)[:50])

    for input_svm in input_svms:
        current_results = {}
        for doc in lib.documents():
            if doc.id == id: continue

            dist = input_tf_idf.cos_dist(doc.tf_idf)
            current_results[doc.id] = dist

        results.update(sorted(current_results, key=current_results.get)[:50])

    for id, freq in results.items():
        print 'id: {}, in: {}'.format(id, freq)
        print lib.doc(id).text
