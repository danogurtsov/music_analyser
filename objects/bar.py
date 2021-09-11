from .note import *

class Bar (list):
	def __init__(self, _notes=[]):
		if len(_notes) > 0:
			for n in _notes:
				assert isinstance(n, Note), "Bar init: some notes inputed are not Notes"
	@property
	def notes(self):
		return self

	def __str__(self):
		if len(self.notes) > 0:
			entry = ''
			for k in range(len(self)):
				if k != 0: entry += ', '
				
				entry += n.__str__()
		else: 
			entry = '<< empty >>'
		return 'BAR [{}]'.format(entry)


				


