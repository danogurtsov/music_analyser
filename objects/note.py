from .pitch import *
from tools.constants import *


class Note (object):
	def __init__(self, pitch, velocity=65, starttime=0, duration=1):
		self.pitch = Pitch(pitch)
		self.starttime = starttime
		self.duration = duration
		self.velocity = velocity
		self.check()
	
	@property
	def octave(self):
		return self.pitch.octave
	@property
	def notename(self):
		return self.pitch.notename

	def check(self):
		self.pitch.check()
		assert self.starttime >= 0 and self.starttime < 1
		assert self.velocity in CONSTANTS.velocities
	
	def __str__(self):
		return 'Note {}: pitch={}, vel={}, st={}, dur={}'.format(self.notename,self.pitch,self.velocity,self.starttime,self.duration)
	