from . import file_loader
import os

class Constants (object):
	def __init__ (self):
		# paths
		self.path_root = os.getcwd()
		self.path_constants = self.path_root + r'\constants'
		self.path_tools = self.path_root + r'\tools'
	
		self.octaves    = self.read_constant('basic_octaves')
		self.pitches    = self.read_constant('basic_pitches')
		self.notenames  = self.read_constant('basic_notenames')
		self.velocities = self.read_constant('basic_velocities') 

		self.zeropitch = ['C', -1]
		self.maxpitch = max(self.pitches)
		self.minpitch = min(self.pitches)

	def read_constant (self,_name:str):
		return file_loader.read(self.path_constants+r'\{}'.format(_name))

CONSTANTS = Constants()
