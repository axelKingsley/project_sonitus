__author__ = 'Axel Kingsley'
# This file defines the standard music theory's relationships


""" A function for calculating the tonal ratio of a note given the number of semitones they are apart"""
semitones = lambda x: 2**(float(x)/12.0)

""" Describes various names of commonly known tonal relationships """
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
    "chromatic" : ["root"]+["semitone"]*11,

    "major_pentatonic" : [
        "root",
        "wholetone",
        "wholetone",
        "semitone",
        "wholetone",
        "wholetone",
        "wholetone",
        "semitone"
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
    from tone import Tone
    import threading
    base_frequency = 440
    for each in scales["major_pentatonic"]:
        print(base_frequency)
        tone = Tone(base_frequency * intervals[each])
        base_frequency *= intervals[each]
        tone.playTone(500)

    base_frequency = 440
    for each in scales["minor_pentatonic"]:
        print(base_frequency)
        tone = Tone(base_frequency * intervals[each])
        base_frequency *= intervals[each]
        tone.playTone(500)

    chord = []
    base_frequency = 440
    for each in chords["major_seventh"]:
        noteThread = threading.Thread(target=Tone(base_frequency * intervals[each]).playTone(500))
        chord.append(noteThread)
    for each in chord: each.start()
