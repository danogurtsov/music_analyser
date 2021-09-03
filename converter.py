from objects.pitch import *
from tools.constants import *
from tools.file_loader import *

import pickle
from mido import MidiFile

def read (_path:str):
	with open(_path, 'rb') as file:
		res = pickle.load(file)
	return res

#n = read('note_table.txt')
#write(n,'basic_velocities')


#mid = MidiFile('bwv0202.mid')
#tracks = mid.tracks

n = CONSTANTS.velocities
print(n)