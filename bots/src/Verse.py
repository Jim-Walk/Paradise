import src.Grabber as Grabber

# The verse class holds the verse's verse and corresponding
# gloss and footnotes for that verse
class Verse():

    verse = ""
    gloss = ""
    footnote = ""

    def __init__(self, bk, sec):
        g = Grabber.Grabber()
        self.verse = g.get_verse(bk, sec)
        self.gloss = g.get_gloss(self.verse)

    def __str__(self):
        print('VERSE')
        print(self.verse)
        print('GLOSS')
        print(self.gloss)
        print('FOOTNOTE')
        print(self.footnote)
