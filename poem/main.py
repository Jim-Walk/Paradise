#!/usr/bin/python3
import codecs, copy
from src.poemGen.poemGen import parseGloss, parse_footnotes
import faulthandler

def main():
    faulthandler.enable()
    with codecs.open('raw.txt', 'r', encoding='utf8') as raw:
        text = raw.readlines()
    pf, gloss = parseGloss(text)
    print('Parsed gloss')
    poem, feet = parse_footnotes(copy.copy(pf))
    print('File parsed')

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
