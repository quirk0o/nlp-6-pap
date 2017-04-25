# coding=utf-8
import codecs
from collections import defaultdict

FORMS_FILENAME = 'data/forms.txt'
FORMS_CACHE_FILENAME = 'cache/forms.txt'


class Dictionary(object):
    def __init__(self):
        self.basic_forms = []
        self.forms = defaultdict(lambda: [])

        with codecs.open(FORMS_FILENAME, encoding='utf-8') as forms_file:
            lines = forms_file.readlines()
            for line in lines:
                forms = line.split(', ')
                id = len(self.basic_forms)
                basic_form = forms[0]
                self.basic_forms.append(basic_form)

                for form in forms:
                    self.forms[form].append(id)

    def rec(self, word):
        return self.forms[word]

    def bform(self, id):
        return self.basic_forms[id]


print 'Initializing dictionary...'
dict = Dictionary()


def basic_form(word):
    ids = dict.rec(word)
    return dict.bform(ids[0]) if len(ids) > 0 else word


if __name__ == '__main__':
    print basic_form(u'żółwiem')
    print basic_form(u'bóle')
    print basic_form('abc')
