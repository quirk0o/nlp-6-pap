# coding=utf-8
import codecs
import re

STOPWORDS_FILENAME = 'data/stopwords.txt'

stopwords = set([line.strip() for line in codecs.open(STOPWORDS_FILENAME, encoding='utf-8').readlines()])


def remove_special_chars(text):
    return re.compile(r'[\W\d]+', re.UNICODE).sub(' ', text)


def deduplicate_whitespace(text):
    return re.compile(r'[\s\n]+', re.UNICODE).sub(' ', text)


def remove_stopwords(words):
    return [word for word in words if word not in stopwords]


def clean_corpus(corpus):
    corpus = corpus.strip().lower()
    corpus = remove_special_chars(corpus)
    corpus = deduplicate_whitespace(corpus)
    words = corpus.split()
    return remove_stopwords(words)

if __name__ == '__main__':
    text = u'To ja, czekoladowy niedźwiedź. Ala ma kota.'
    for word in clean_corpus(text):
        print word
