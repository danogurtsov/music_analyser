from tools import file_loader
import os
import pickle

fs = os.listdir(r'C:\_MAIN\open_source\music_analyser\constants')

file_loader.write(all_pitches,'basic_pitches.yaml')
