# coding=utf-8
import codecs
import math
import re
from collections import defaultdict

from plp import basic_form
from preprocessor import clean_corpus


class LanguageModel(object):
    def __init__(self, documents):
        self.__df__ = defaultdict(lambda: 0)
        self.terms = set()
        self.N = len(documents)

        for doc in documents:
            words = doc.split()
            basic_forms = set([basic_form(word) for word in words])

            for word in basic_forms:
                self.__df__[word] += 1
                self.terms.add(word)

    def df(self, term):
        return self.__df__[term]


def tf(term, document):
    words = [basic_form(word) for word in document.split()]
    return len(filter(lambda x: x == term, words))


def tf_idf(term, document):
    return tf(term, document) * math.log(float(lm.N) / lm.df(term), 2)


def doc2vec(document):
    return [tf_idf(term, document) for term in lm.terms]


def distance(v1, v2):
    return math.sqrt(sum([(i - j) ** 2 for i, j in zip(v1, v2)]))


if __name__ == '__main__':
    with codecs.open('data/pap.txt', encoding='utf-8') as docs_file:
        input = docs_file.read()
        documents = re.split('#\d+', input)
        documents = [clean_corpus(doc) for doc in documents if doc]

    print 'Initializing language model...'
    lm = LanguageModel(documents)

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

    doc2 = u'10 czerwca br. zostanie otwarty cmentarz polskich żołnierzy w ' \
           u'Miednoje, 17 czerwca - w Charkowie, a 1 lipca w Katyniu - wynika ' \
           u'z wstępnego harmonogramu obchodów 60-tej rocznicy zbrodni ' \
           u'katyńskiej, który przedstawił sekretarz generalny Rady Ochrony ' \
           u'Pamięci Walk i Męczeństwa Andrzej Przewoźnik.' \
           u'Centralne obchody rocznicy w kraju planowane są na 13 kwietnia. ' \
           u'Tego dnia odbędzie się uroczyste posiedzenie Sejmu, który ma ' \
           u'przyjąć uchwałę z okazji 60-tej rocznicy zbrodni katyńskiej. ' \
           u'Obchody zaczynają się 3 marca od konferencji naukowej ' \
           u'"Dokumentowanie zbrodni NKWD na obywatelach II RP w czasie ' \
           u'drugiej wojny światowej". Zostaną zamknięte 17 września 2000 r. ' \
           u'uroczystościami pod pomnikiem "Poległym i Pomordowanym na ' \
           u'Wschodzie".'

    doc3 = u'Wrzuceniem przez premiera Jerzego Buzka srebrnego pierścienia do ' \
           u'Bałtyku zakończyły się w Pucku obchody 80 rocznicy Zaślubin ' \
           u'Polski z Morzem.' \
           u'Szef rządu wrzucił pierścień do wody, podobnie jak zrobił to w ' \
           u'1920 r. gen. Józef Haller, dokonując symbolicznego aktu ' \
           u'przywrócenia Polsce dostępu do Bałtyku. ' \
           u'Ostatnim etapem obchodów 80 rocznicy Zaślubin Polski z Morzem były' \
           u'uroczystości we Władysławowie. Głównym ich punktem było utworzenie' \
           u'"Hallerówki" - muzeum poświęconego gen. Józefowi Hallerowi. '

    print 'Preparing documents...'
    doc1 = clean_corpus(doc1)
    doc2 = clean_corpus(doc2)
    doc3 = clean_corpus(doc3)

    print 'Calculating vectors...'
    vec1 = doc2vec(doc1)
    vec2 = doc2vec(doc2)
    vec3 = doc2vec(doc3)

    print 'Calculating distance...'
    print distance(vec1, vec2)
    print distance(vec1, vec3)
    print distance(vec2, vec3)
