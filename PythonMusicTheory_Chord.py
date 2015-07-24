__author__ = 'Axel Kingsley'
import Patterns

def chordFromToneAndPattern(tone, pattern):
    appliedTones=map(lambda p: tone.applyInterval(p), Patterns.chordPatterns[pattern])
    return Chord(appliedTones)

class Chord(object):
    tones=[]
    def __init__(self, tones=[]):
        self.tones=tones
    def playChord(self, duration):
        for tone in self.tones:
            tone.playTone(duration)
    def map(self, interval):
        return Chord(tones=map(lambda t: t.applyInterval(interval), self.tones))
    def add(self, tone):
        self.tones.append(tone)
