from .pitch import *
from tools.constants import *


class Note (object):
	def __init__(self, p, v=65, st=0, d=1):
		self.pitch = Pitch(p)
		self.starttime = st
		self.duration = d
		self.velocity = v
		self.check()
	
	@property
	def octave(self):
		return self.pitch.octave
	@property
	def notename(self):
		return self.pitch.notename
		
	@property
	def p(self):
		return self.pitch
	@property
	def v(self):
		return self.velocity
	@property
	def st(self):
		return self.starttime
	@property
	def d(self):
		return self.duration

	def check(self):
		self.pitch.check()
		assert self.starttime >= 0 and self.starttime < 1
		assert self.velocity in CONSTANTS.velocities
	
	def __str__(self):
		return '(Note {}: p={}, v={}, st={}, d={})'.format(
			self.notename,
			self.pitch,
			self.velocity,
			self.starttime,
			self.duration)
	