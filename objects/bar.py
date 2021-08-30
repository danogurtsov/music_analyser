from . import Note

class Bar (object):
	def __init__(self, _notes):
		for n in _notes:
			assert isinstance(n, Note), "Bar init: some notes inputed are not Notes"
		self.notes = _notes

class Bar (dict):
	def __init__(self, _notes):
		# как для каждой ноты тут должно появиться время?
		self.notes = _notes

	@property
	def notes (self):


	def is_full(self):
		assert len(self.notes) == len(self.starttimes)
