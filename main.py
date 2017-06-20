import pyaudio
import modern_standards
import instruments

PyAudio = pyaudio.PyAudio
bitrate = 16000
length = .4
number_of_frames = int(bitrate * length)
rest_frames = number_of_frames % bitrate
output = ''    

base_freq = 440
frequency_keys = ["e", "f", "f#", "g", "g#", "a", "a#", "b", "c", "c#", "d", "d#"]
frequency_values = [base_freq * modern_standards.intervals[x] for x in modern_standards.scales['major_pentatonic']]
frequency_dict = dict(zip(frequency_keys, frequency_values))
print frequency_dict

song = "bagabbbaaabddbagabbbbaabag"


for slice in song:
    for x in xrange(number_of_frames):
        new_char = 0
        for note in slice:
            frequency = frequency_dict[note]
            new_char += instruments.sign_wave(bitrate, x, frequency)
        output += chr(int(new_char / len(slice) * 127 +128))

for x in xrange(rest_frames): 
 output = output+chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = bitrate, 
                output = True)

stream.write(output)
stream.stop_stream()
stream.close()
p.terminate()
