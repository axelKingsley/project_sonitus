__author__ = 'Axel Kingsley'
# This file defines the standard music theory's relationships


# semitones is an 'anonymous' which calculates the tonal ratio
# given some number of steps.
semitones = lambda x: 2**(float(x)/12.0)

# intervals describes various names of commonly known tonal relationships
# they are described in terms of semitones, the base relationship of notes.
intervals={
    "perfect_unison"   : semitones(0),
    "root"             : semitones(0),
    "semitone"         : semitones(1),
    "minor_second"     : semitones(1),
    "wholetone"        : semitones(2),
    "major_second"     : semitones(2),
    "minor_third"      : semitones(3),
    "major_third"      : semitones(4),
    "perfect_fourth"   : semitones(5),
    "tritone"          : semitones(6),
    "augmented_fourth" : semitones(6),
    "diminished_fifth" : semitones(6),
    "perfect_fifth"    : semitones(7),
    "diapente"         : semitones(7),
    "augmented_fifth"  : semitones(8),
    "minor_sixth"      : semitones(8),
    "major_sixth"      : semitones(9),
    "minor_seventh"    : semitones(10),
    "major_seventh"    : semitones(11),
    "perfect_octave"   : semitones(12)
}

# chord_patterns is a dictionary containing common sets of three-note chords
chords={
    "major"              : ["root", "major_third", "perfect_fifth"],
    "minor"              : ["root", "minor_third", "perfect_fifth"],

    "diminished"         : ["root", "minor_third", "diminished_fifth"],
    "augmented"          : ["root", "major_third", "augmented_fifth"],

    "major_seventh"      : ["root","major_third","major_seventh"],
    "minor_seventh"      : ["root","minor_third","minor_seventh"],

    "dominant_seventh"   : ["root","major_third","minor_seventh"],
    "diminished_seventh" : ["root","minor_third","major_sixth"]
}

scales={
    "chromatic" : ["root"]*["semitone"]*11,

    "major_pentatonic" : [
        "root",
        "wholetone",
        "semitone",
        "semitone",
        "wholetone",
        "semitone",
        "wholetone",
        "semitone"
        ],
    "minor_pentatonic" : [
        "root",
        "wholetone",
        "semitone",
        "semitone",
        "wholetone",
        "semitone",
        "wholetone",
        "semitone"
        ]
}

def makeScale(tone, scale):
    returnScale=[tone]
    for each in range(1,len(scale)):
        returnScale.append(returnScale[-1].applyInterval(scale[each]))
    return returnScale