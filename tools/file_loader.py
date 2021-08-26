import yaml
import pickle

def write (_object,_path:str):
	with open(_path, 'w') as file:
		yaml.dump(_object, file)

def read (_path:str):
	with open(_path, 'r') as file:
		res = yaml.safe_load(file)
	return res
