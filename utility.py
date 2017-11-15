# Utility tools to support project functionality
import os


def abspaths_data(data_dir):
	"""
	:param data_dir: (str) path of data folder RELATIVE to the project home directory
	:return: (generator expression) absolute paths of data files in a given data directory
	"""
	abspath_proj_dir = os.path.dirname(os.path.abspath(__file__))
	abspath_data_dir = os.path.join(abspath_proj_dir, data_dir)
	abspaths_data_files = (os.path.join(abspath_data_dir, data) for data in os.listdir(abspath_data_dir))

	return abspaths_data_files
