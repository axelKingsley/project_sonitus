__author__ = 'Axel Kingsley'

chromatic = ["root"]+(["semitone"]*11)
#The pentatonics DON'T SOUND RIGHT AT ALL!
majorPentatonic = [
    "root",
    "wholetone",
    "semitone",
    "semitone",
    "wholetone",
    "semitone",
    "wholetone",
    "semitone"
    ]
minorPentatonic = [
    "root",
    "wholetone",
    "semitone",
    "semitone",
    "wholetone",
    "semitone",
    "wholetone",
    "semitone"
    ]
def makeScale(tone, scale):
    returnScale=[tone]
    for each in range(1,len(scale)):
        returnScale.append(returnScale[-1].applyInterval(scale[each]))
    return returnScale