from tools._external_imports import *

def write (_object, _path:str):
	_path = _path.replace('.yaml','')+'.yaml'
	with open(_path, 'w') as file:
		yaml.dump(_object, file)

def read (_path:str):
	_path = _path.replace('.yaml','')+'.yaml'
	with open(_path, 'r') as file:
		res = yaml.safe_load(file)
	return res
