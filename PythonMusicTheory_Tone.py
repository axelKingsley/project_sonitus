__author__ = 'Axel Kingsley'
import Intervals
import winsound
class Tone(object):
    #The potential relationships a tone can have
    frequency=None
    #The constructor for Tone only sets frequency
    def __init__(self, fq):
        self.frequency=fq
    def applyInterval(self,intervalName): return Tone(self.frequency*Intervals.tonalIntervals[intervalName])
    def playTone(self, duration):
        winsound.Beep(int(self.frequency), duration)

