from tools.constants import *

class Pitch (int):
	def __init__ (self, _num:int):
		self.num = _num
		self.min = min(CONSTANTS.pitches)
		self.max = max(CONSTANTS.pitches)
	def octave(self):
		res = self.num / len(CONSTANTS.notenames) + CONSTANTS.zeropitch[1]
		return int(res) if res > 0 else -1
	def notename(self):
		return CONSTANTS.notenames[int(self.num / (self.octave() + 2))]


