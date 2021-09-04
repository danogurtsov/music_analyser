from tools.constants import *

class Pitch (int):
	# octave
	# notename

	def __init__ (self, _num:int):
		self.value = _num
		self.check()
	@property
	def octave(self):
		res = self / len(CONSTANTS.notenames) + CONSTANTS.zeropitch[1]
		return int(res) if res > 0 else -1
	@property
	def notename(self):
		return CONSTANTS.notenames[self % len(CONSTANTS.notenames)]
	
	def check(self):
		None
		assert self < CONSTANTS.maxpitch, 'max pitch overflow'
		assert self > CONSTANTS.minpitch, 'min pitch underflow'
	
	def __add__(self, _val):
		before = self.value
		after = before + _val
		res = Pitch(after)
		res.check()
		return res

	def __sub__(self, _val):
		before = self.value
		after = before - _val
		res = Pitch(after)
		res.check()
		return res








