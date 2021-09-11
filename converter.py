from objects.pitch import *
from objects.note import *
from objects.bar import *
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

n1 = Note(p=55, v=65, st=0.5, d=1) 
n2 = Note(p=53, v=63, st=0, d=1)

b = Bar()

print(b)

b.append([n1,n2])

print(b)