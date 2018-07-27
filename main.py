#!/usr/bin/python3
import codecs
from src.poemGen.poemGen import parseGloss

def main():
    with codecs.open('raw.txt', 'r', encoding='utf8') as raw:
        text = raw.readlines()
    pf, gloss = parseGloss(text)
    print('File parsed')

    with codecs.open('pf.txt', 'w', encoding='utf8') as pf_file:
        for line in pf:
            pf_file.write(line)

    with codecs.open('gloss.txt', 'w', encoding='utf8') as gloss_file:
        for line in gloss:
            gloss_file.write(line)

    print('Output written to file')


if __name__ == '__main__':
    main()
