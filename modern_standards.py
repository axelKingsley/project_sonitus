__author__ = 'Axel Kingsley'
# This file defines the standard music theory's relationships

octave_multiplier = 2
number_of_notes = 12

""" A function for calculating the tonal ratio of a note given the number of semitones they are apart"""
semitones = lambda x: octave_multiplier**(float(x)/number_of_notes)

""" Describes various names of commonly known tonal relationships """
intervals={
    0                  : semitones(0),
    "perfect_unison"   : semitones(0),
    "root"             : semitones(0),
    1                  : semitones(1),
    "semitone"         : semitones(1),
    "minor_second"     : semitones(1),
    2                  : semitones(2),
    "wholetone"        : semitones(2),
    "major_second"     : semitones(2),
    3                  : semitones(3),
    "minor_third"      : semitones(3),
    4                  : semitones(4),
    "major_third"      : semitones(4),
    5                  : semitones(5),
    "perfect_fourth"   : semitones(5),
    6                  : semitones(6),
    "tritone"          : semitones(6),
    "augmented_fourth" : semitones(6),
    "diminished_fifth" : semitones(6),
    7                  : semitones(7),
    "perfect_fifth"    : semitones(7),
    "diapente"         : semitones(7),
    8                  : semitones(8),
    "augmented_fifth"  : semitones(8),
    "minor_sixth"      : semitones(8),
    9                  : semitones(9),
    "major_sixth"      : semitones(9),
    10                 : semitones(10),
    "minor_seventh"    : semitones(10),
    11                 : semitones(11),
    "major_seventh"    : semitones(11),
    12                 : semitones(12),
    "perfect_octave"   : semitones(12),
    14                 : semitones(12)*semitones(2),
    16                 : semitones(12)*semitones(4),
    17                 : semitones(12)*semitones(5),
    19                 : semitones(12)*semitones(7)
    
}

""" Dictionary containing common sets of three-note chords """
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

""" Dictionary containing common lists of notes which make up scales """
scales={
    "chromatic" : [0,1,2,3,4,5,6,7,8,9,10,11,12],

    "major_pentatonic" : [
        0,
        2,
        4,
        5,
        7,
        9,
        11,
        12,
        14,
        16,
        17,
        19
        ],
    "minor_pentatonic" : [
        "root",
        "wholetone",
        "semitone",
        "wholetone",
        "wholetone",
        "semitone",
        "wholetone",
        "wholetone"
        ]
}


if __name__ == "__main__":
    pass
