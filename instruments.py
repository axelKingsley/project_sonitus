import math

def sign_wave(bitrate, frame, frequency):
    return math.sin(frame/((bitrate/frequency)/math.pi))
