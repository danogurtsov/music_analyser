from objects.pitch import *
from objects.note import *
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

n = Note(55,0,0.5,50)
print(dir(n))
print(n.__str__())