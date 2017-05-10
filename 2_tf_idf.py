# coding=utf-8
import sys

from library import Document, Library
from statistics import StatisticsService
from tf_idf import Doc2Vec

alpha = 0.83

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

    sample_filename = 'samples/{}'.format(id)
    classification = [int(id) for id in open(sample_filename).readlines()]

    input_vec = d2v.doc2vec(input_doc)
    input_vec.normalize()

    print input_doc.text

    results = []
    for doc in lib.documents():
        if doc.id == input_doc.id: continue

        vec = d2v.doc2vec(doc)
        vec.normalize()
        dist = vec.cos_dist(input_vec)

        if dist < alpha:
            results.append(doc.id)

    stats = StatisticsService(all_samples=lib.ids, classification=classification, guesses=results)
    print 'Precision: {}'.format(stats.precision())
    print 'Recall: {}'.format(stats.recall())
    print 'F1: {}'.format(stats.f1())
    print 'Accuracy: {}'.format(stats.accuracy())
