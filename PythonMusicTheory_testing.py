__author__ = 'Axel Kingsley'
import Tone
import Chord
import Patterns
import Intervals
import Scales
t = Tone.Tone(400)
"""
for each in Patterns.chordPatterns:
    Chord.chordFromToneAndPattern(t, each).playChord(40)
    print each
   # _=raw_input("PRESS ENTER")

for each in Chord.chordFromToneAndPattern(t, "minorSeventh").tones:
    print each.frequency

for each in Chord.chordFromToneAndPattern(t, "dominantSeventh").tones:
    print each.frequency

for each in Intervals.tonalIntervals:
    print each, ":", Intervals.tonalIntervals[each]

scale = Chord.Chord(tones=[t])
for each in range(12):
    scale.add(scale.tones[-1].applyInterval("wholetone"))
scale.playChord(10)
"""
#Chord.Chord(Scales.makeScale(t,Scales.chromatic)).playChord(300)
Chord.Chord(Scales.makeScale(t,Scales.majorPentatonic)).playChord(300)