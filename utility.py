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


def dimensionsEqual(rows_list, columns_list, dimensions_list):
	"""
	:param rows_list: (sequence-type of ints) elements represent # of rows for a collection of dataframes
	:param columns_list: (sequence-type of ints) elements represent # of rows for a collection of dataframes
	:param dimensions_list: (sequence-type of ordered pairs) elements represent dimensions/shape for a collection of dataframes
	:return: (bool) Used to assert that given rows_list/columns_list have same shape as dimensions_list
	"""
	d_list = zip(rows_list, columns_list)
	for dim1, dim2 in zip(d_list, dimensions_list):
		if dim1 != dim2:
			return False
	return True
