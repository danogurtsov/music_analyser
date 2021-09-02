from . import Pitch


class Note (object):
	# pitch
	# starttime
	# duration
	# velocity
	def __init__(self, pitch, starttime, duration, velocity):
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
		assert self.pitch.check()
		assert self.starttime >= 0 and self.starttime < 1
	
	