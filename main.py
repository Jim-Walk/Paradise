#!/usr/bin/python3
import codecs, copy
from src.poemGen.poemGen import parseGloss, parse_footnotes

def main():
    with codecs.open('raw.txt', 'r', encoding='utf8') as raw:
        text = raw.readlines()
    pf, gloss = parseGloss(text)
    poem, feet = parse_footnotes(copy.copy(pf))
    print('File parsed')

    with codecs.open('pf.txt', 'w', encoding='utf8') as pf_file:
        for line in pf:
            pf_file.write(line)

    with codecs.open('poem.txt', 'w', encoding='utf8') as poem_file:
        for line in poem:
            poem_file.write(line)

    with codecs.open('footnotes.txt', 'w', encoding='utf8') as footnotes_file:
        for line in feet:
            footnotes_file.write(line)

    with codecs.open('gloss.txt', 'w', encoding='utf8') as gloss_file:
        for line in gloss:
            gloss_file.write(line)

    print('Output written to file')


if __name__ == '__main__':
    main()
