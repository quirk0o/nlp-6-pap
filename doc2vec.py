# coding=utf-8
import math
from collections import defaultdict

from library import Document, Library

print 'Initializing library...'
lib = Library()


def tf(term, document):
    return document.vec[term]


def idf(term):
    return math.log(float(lib.N) / lib.df(term), 2) if lib.df(term) != 0 else float('inf')


def tf_idf(term, document):
    return tf(term, document) * idf(term)


def doc2vec(document):
    return defaultdict(lambda: 0, [(term, tf_idf(term, document)) for term in document.words])


def distance(v1, v2):
    keys = set(v1.keys()).union(v2.keys())
    return math.sqrt(sum([(v1[key] - v2[key]) ** 2 for key in keys]))


if __name__ == '__main__':
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
           u'Ostatnim etapem obchodów 80 rocznicy Zaślubin Polski z Morzem były ' \
           u'uroczystości we Władysławowie. Głównym ich punktem było utworzenie ' \
           u'"Hallerówki" - muzeum poświęconego gen. Józefowi Hallerowi. '

    print 'Preparing documents...'
    doc1 = Document(1, doc1)
    doc2 = Document(2, doc2)
    doc3 = Document(3, doc3)

    print 'Calculating vectors...'
    vec1 = doc2vec(doc1)
    vec2 = doc2vec(doc2)
    vec3 = doc2vec(doc3)

    print 'Calculating distance...'
    print distance(vec1, vec2)
    print distance(vec1, vec3)
    print distance(vec2, vec3)
