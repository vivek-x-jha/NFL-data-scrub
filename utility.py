# Utility tools to support project functionality
import os
import numpy as np


def abspaths_data(data_dir):
	"""
	Outputs iterable of absolute paths of data files in a given data directory
	:param data_dir: (str) path of data folder RELATIVE to the project home directory
	:return: generator expression
	"""
	abspath_proj_dir = os.path.dirname(os.path.abspath(__file__))
	abspath_data_dir = os.path.join(abspath_proj_dir, data_dir)
	abspaths_data_files = (os.path.join(abspath_data_dir, data) for data in os.listdir(abspath_data_dir))

	return abspaths_data_files


def testRowColumnSizes(rows_list, columns_list, dimensions_list):
	"""
	Used to assert that given rows_list/columns_list have same shape as dimensions_list
	:param rows_list: (sequence-type of ints) elements represent # of rowSizes for a collection of dataframes
	:param columns_list: (sequence-type of ints) elements represent # of columnSizes for a collection of dataframes
	:param dimensions_list: (sequence-type of ordered pairs) elements represent dimensions/shape for a collection of dataframes
	:return: bool
	"""
	d_list = zip(rows_list, columns_list)
	for dim1, dim2 in zip(d_list, dimensions_list):
		if dim1 != dim2:
			return False

	return True


def isEqualNumberOfColumns(columns_list):
	"""
	Used to assert that each dataframe has the same number of columnSizes
	:param columns_list: (sequence-type of ints) elements represent # of columnSizes for a collection of dataframes
	:return: bool
	"""
	isEqual = min(columns_list) == max(columns_list)

	return isEqual


def testMergeDimensions(rows_list, columns_list, mergedDataframe):
	"""
	Used to assert that merged dataframe has correct dimensions
	:param rows_list: (sequence-type of ints) elements represent # of rowSizes for a collection of dataframes
	:param columns_list: (sequence-type of ints) elements represent # of columnSizes for a collection of dataframes
	:param mergedDataframe: (dataframe obj) vertically stacked dataframe from
	:return: bool
	"""
	rand_column_size = columns_list[np.random.randint(len(columns_list))]
	correctDimensions = sum(rows_list), rand_column_size
	isEqual = mergedDataframe.shape == correctDimensions

	return isEqual

