from . import Pitch


class Note (object):
	# pitch
	# starttime
	# duration
	# velocity
	def __init__(self, pitch, starttime, duration, velocity):
		self.pitch = Pitch(pitch)
		self.duration = duration
		self.velocity = velocity
	
	@property
	def octave(self):
		return self.pitch.octave
	@property
	def notename(self):
		return self.pitch.notename
	
	