import src.Grabber as Grabber

# The verse class holds the verse's verse and corresponding
# gloss and footnotes for that verse
class Verse():

    verse = ""
    gloss = ""
    footnote = ""
    bk = -1
    sec = -1
    lineN = 0 # The line number of the verse in its own book
    gloss_i = 0
    foot_i = 0

    def __init__(self, verse_text):
        g = Grabber.Grabber()
        self.bk, self.sec = g.get_bk_sec(verse_text)
        self.verse, self.lineN = g.get_verse(self.bk, self.sec)
        self.footnote = g.get_footnote(self.bk, self.sec)
        self.gloss = g.get_gloss(self.verse)

    def __str__(self):
        s = ('VERSE\n'+self.verse+'GLOSS\n'+self.gloss+'FOOTNOTES '+
             str(self.lineN) + '\n' +self.footnote)
        return s

    def gen_verses(self):
        g = Grabber.Grabber()
        while self.verse != '':
            yield self
            self.sec += 1
            self.verse, self.lineN = g.get_verse(self.bk, self.sec)
            if self.verse == '':
                self.sec = 1
                self.bk += 1
                if self.bk > 12:
                    self.bk = 1
                    print('Completed reading')
                self.verse, self.lineN = g.get_verse(self.bk, self.sec)
            self.gloss = g.get_gloss(self.verse)
            self.footnote = g.get_footnote(self.bk, self.lineN)
