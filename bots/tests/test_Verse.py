#!/usr/bin/python3

import pytest
import src.Verse as Verse

def test_verse_1_12():
    verse_ans = ('Dove-like satst brooding on the vast Abyss\nAnd mad’st it '
                'pregnant: What in me is dark\nIllumin, what is low raise and '
                'support;\nThat to the highth of this great Argument°\nI may'
                 ' assert Eternal Providence,\n')
    gloss_ans = 'subject\n'
    
    v = Verse.Verse(1,12)
    assert v.verse == verse_ans
    assert v.gloss == gloss_ans

def test_verse_2_33():
    verse_ans = ('Incapable of stain would soon expel\n'
            'Her mischief, and purge off the baser fire\n'
            'Victorious. Thus repuls’d, our final hope\n'
            'Is flat° despair: we must exasperate\n'
            'Th’ Almighty Victor to spend all his rage,\n')
    gloss_ans = 'absolute\n'
    
    v = Verse.Verse(2,33)
    assert v.verse == verse_ans
    assert v.gloss == gloss_ans
