with open('../poem/poem.txt') as poem_f:
    poem = poem_f.readlines()

    i = 0
    book = 1
    book_idxs = [0]

    # Create a list of indexes where each book starts
    while book < 13:
        if poem[i].strip() == 'BOOK ' + str(book):
            book += 1
            book_idxs += [i]
        i += 1

    # Set char limit so we have some room to play
    # with.
    char_limit = 210
    char_count = 0

    verse = ''
    verse_idx = 0

    i = 0
    line = poem[i]
    while char_count < char_limit:
        char_i = 0
        while char_i < len(poem[i]):
            verse += poem[i][char_i]
            char_count += 1
            char_i += 1
        i += 1
        line = poem[i]

    print(verse)
    print(i, char_i)

