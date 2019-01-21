# -*- coding: utf-8 -*-

import os
import glob
import dateutil.parser
import numpy as np
from netCDF4 import Dataset
from atmoswing.external import jdcal


class CFSR(object):
    """Extract CFSR data"""

    def __init__(self, directory, file_pattern, var_name):
        self.file_pattern = file_pattern
        self.directory = directory
        self.var_name = var_name
        self.data = []
        self.__files = None
        self.axis_level_units = ''
        self.axis_lat = []
        self.axis_lon = []
        self.axis_time = []
        self.axis_level = []

    def load(self):
        self.__list()
        self.__extract()

    def __list(self):
        if not os.path.isdir(self.directory):
            raise Exception('Directory {} not found'.format(self.directory))

        self.__files = glob.glob(os.path.join(self.directory, self.file_pattern))

        if len(self.__files) == 0:
            raise Exception('No file found as {}'.format(os.path.join(self.directory, self.file_pattern)))

        self.__files.sort()

    def __extract(self):
        for file in self.__files:
            if not os.path.isfile(file):
                raise Exception('File {} not found'.format(file))

            print('Reading ' + file)
            nc = Dataset(file, 'r')
            var = nc.variables[self.var_name]
            data = np.array(var)
            time = np.array(nc.variables[var.dimensions[0]])

            time = self.__convert_time(nc, var, time)

            has_levels = len(var.dimensions) == 4

            if not has_levels:
                new_shape = (data.shape[0], 1, data.shape[1], data.shape[2])
                data = np.reshape(data, new_shape)

            if len(self.data) == 0:
                self.data = data
                self.data_units = nc.variables[self.var_name].units
                self.axis_time = time
                if has_levels:
                    self.axis_level = np.array(nc.variables[var.dimensions[1]])
                    self.axis_level_units = nc.variables[var.dimensions[1]].units
                    self.axis_lat = np.array(nc.variables[var.dimensions[2]])
                    self.axis_lon = np.array(nc.variables[var.dimensions[3]])
                else:
                    self.axis_level = [0]
                    self.axis_level_units = ''
                    self.axis_lat = np.array(nc.variables[var.dimensions[1]])
                    self.axis_lon = np.array(nc.variables[var.dimensions[2]])
            else:
                self.data = np.append(self.data, data, axis=0)
                self.axis_time = np.append(self.axis_time, time, axis=0)

            nc.close()

    def __convert_time(self, nc, var, time):
        time_units = nc.variables[var.dimensions[0]].units
        str_space = time_units.find(' ')
        time_step = time_units[0:str_space]
        str_since = time_units.find('since')
        str_date = time_units[str_since + 6:]
        str_space = str_date.find(' ')
        if str_space > 0:
            str_date = str_date[0:str_space]

        ref_date = dateutil.parser.parse(str_date)
        ref_date_mjd = jdcal.gcal2jd(ref_date.year, ref_date.month, ref_date.day)[1]

        if time_step == "hours":
            time = time / 24

        time = time + ref_date_mjd

        return time
