from objects.Pitch import *

#file_loader.write(all_pitches,'basic_pitches.yaml')

for i in range(130):
	print(i, Pitch(i).octave(), Pitch(i).notename())