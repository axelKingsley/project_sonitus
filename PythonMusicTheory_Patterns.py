__author__ = 'Axel Kingsley'
#This is simply an importable dictionary detailing common chord progressions.
#Values can be found at https://en.wikipedia.org/wiki/List_of_chords

chord_patterns={
    "major" : ["root", "major_third", "perfect_fifth"],
    "minor" : ["root", "minor_third", "perfect_fifth"],

    "diminished" : ["root", "minor_third", "diminished_fifth"],
    "augmented"  : ["root", "major_third", "augmented_fifth"],

    "major_seventh":["root","major_third","major_seventh"],
    "minor_seventh":["root","minor_third","minor_seventh"],

    "dominant_seventh":["root","major_third","minor_seventh"],
    "diminished_seventh":["root","minor_third","major_sixth"]
}