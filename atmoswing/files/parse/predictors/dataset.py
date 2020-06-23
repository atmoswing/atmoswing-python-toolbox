# -*- coding: utf-8 -*-

import os
import numpy as np
from math import nan

DOMAIN_WISE = 0
""" Domain wise """
POINT_WISE = 1
""" Point wise """


class Dataset(object):
    """Generic (parent) class not to be used directly. Use Grib or Netcdf datasets."""

    def __init__(self, directory, file_pattern):
        self.file_pattern = file_pattern
        self.directory = directory
        self.data = []
        self.data_units = None
        self.__files = None
        self.axis_lat = []
        self.axis_lon = []
        self.axis_time = []
        self.axis_level = []
        self.is_standardized = False
        self.mean = nan
        self.sd = nan

    def standardize(self, mode=DOMAIN_WISE):
        if mode == DOMAIN_WISE:
            self.mean = np.mean(self.data)
            self.sd = np.std(self.data)
            print("mean = {}, sd = {}".format(self.mean, self.sd))
            self.data = (self.data - self.mean) / self.sd
        elif mode == POINT_WISE:
            raise Exception("Not tested and likely not working properly.")

            self.mean = np.mean(self.data, axis=0)
            self.sd = np.std(self.data, axis=0)
            print("mean = {}, sd = {}".format(self.mean, self.sd))
            self.data = (self.data - self.mean) / self.sd
        else:
            raise Exception("Wrong mode for the standardization.")

    def replace_nans(self, nan_val, new_val):
        self.data[self.data == nan_val] = new_val