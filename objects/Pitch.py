from tools.constants import *

class Pitch (int):
	# octave
	# notename

	def __init__ (self, _num:int):
		self.value = _num
	@property
	def octave(self):
		res = self / len(CONSTANTS.notenames) + CONSTANTS.zeropitch[1]
		return int(res) if res > 0 else -1
	@property
	def notename(self):
		return CONSTANTS.notenames[self % len(CONSTANTS.notenames)]
	
	def check(self, _target):
		assert _target < CONSTANTS.maxpitch, 'max pitch overflow'
		assert _target > CONSTANTS.minpitch, 'min pitch underflow'
	
	def __add__(self, _val):
		res = self.value + _val
		self.check(res)
		return Pitch(res)

	def __sub__(self, _val):
		res = self.value - _val
		self.check(res)
		return Pitch(res)









