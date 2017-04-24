import codecs
from preprocessor import *

INPUT_FILENAME = 'data/pap.txt'


if __name__ == '__main__':
    with codecs.open(INPUT_FILENAME, encoding='utf-8') as input_file:
        input = input_file.read()
        notes = re.split('#\d+', input)
        notes = [clean_corpus(note) for note in notes if note]
