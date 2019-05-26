import src.Grabber as Grabber

# The verse class holds the verse's verse and corresponding
# gloss and footnotes for that verse
class Verse():

    verse = ""
    gloss = ""
    footnote = "f"
    bk = -1
    sec = -1
    poem_i = 0
    gloss_i = 0
    foot_i = 0

    def __init__(self, bk, sec):
        g = Grabber.Grabber()
        self.bk = bk
        self.sec = sec
        self.verse = g.get_verse(bk, sec)
        self.gloss = g.get_gloss(self.verse)

    def __str__(self):
        s = 'VERSE\n' + self.verse + 'GLOSS\n'+ self.gloss
        return s

    def gen_verses(self):
        g = Grabber.Grabber()
        while self.verse != '':
            yield self
            self.sec += 1
            self.verse = g.get_verse(self.bk, self.sec)
            if self.verse == '':
                self.sec = 1
                self.bk += 1
                self.verse = g.get_verse(self.bk, self.sec)
            self.gloss = g.get_gloss(self.verse)
