# -*- coding: utf-8 -*-

import os
import glob
import dateutil.parser
import numpy as np
from eccodes import *
from atmoswing.external import jdcal


class Grib(object):
    """Extract Grib data"""

    def __init__(self, directory, file_pattern, var_name):
        self.grib_version = 0
        self.file_pattern = file_pattern
        self.directory = directory
        self.var_name = var_name
        self.data = []
        self.data_units = None
        self.__files = None
        self.axis_lat = []
        self.axis_lon = []
        self.axis_time = []
        self.axis_level = []
        self.param_code_1 = []
        self.param_code_2 = []
        self.param_code_3 = []

    def load(self):
        try:
            self.__list()
            self.__extract()
        except OSError as err:
            print("OS error: {0}".format(err))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

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

            f = open(file, 'rb')

            while True:
                msgid = codes_new_from_file(f, CODES_PRODUCT_GRIB)

                if msgid is None:
                    break

                if self.grib_version == 0:
                    self.grib_version = codes_get_long(msgid, "editionNumber")

                self.__extract_axes(msgid)
                self.__extract_level(msgid)
                self.__extract_time(msgid)
                self.__extract_grib_code(msgid)

                data = codes_get_array(msgid, "values")
                n_lats = len(self.axis_lat[len(self.axis_lat) - 1])
                n_lons = len(self.axis_lon[len(self.axis_lon) - 1])
                if len(self.data) == 0:
                    self.data = data.reshape((1, 1, n_lats, n_lons))
                else:
                    if self.data.shape[2] != n_lats or self.data.shape[3] != n_lons:
                        raise Exception("Issues in the size of the arrays.")
                    self.data = np.append(self.data, data.reshape((1, 1, n_lats, n_lons)), axis=0)

                units = codes_get(msgid, "units")
                if self.data_units is None:
                    self.data_units = units
                if self.data_units != units:
                    raise Exception("Only 1 type of data per file supported so far.")

            f.close()

    def __extract_axes(self, msgid):
        n_lats = codes_get_long(msgid, "Nj")
        n_lons = codes_get_long(msgid, "Ni")
        lat_start = codes_get_long(msgid, "latitudeOfFirstGridPointInDegrees")
        lon_start = codes_get_long(msgid, "longitudeOfFirstGridPointInDegrees")
        lat_end = codes_get_long(msgid, "latitudeOfLastGridPointInDegrees")
        lon_end = codes_get_long(msgid, "longitudeOfLastGridPointInDegrees")
        if lon_end < lon_start:
            lon_start -= 360

        self.axis_lat.append(np.linspace(lat_start, lat_end, n_lats))
        self.axis_lon.append(np.linspace(lon_start, lon_end, n_lons))

    def __extract_level(self, msgid):
        level = codes_get_double(msgid, "level")
        type = codes_get(msgid, "typeOfLevel")
        if type == "isobaricInPa":
            level /= 100

        self.axis_level.append(level)

    def __extract_time(self, msgid):
        ref_date = dateutil.parser.parse(codes_get_string(msgid, "dataDate"))
        ref_date_mjd = jdcal.gcal2jd(ref_date.year, ref_date.month, ref_date.day)[1]
        ref_time = codes_get(msgid, "dataTime")

        forecast_time = 0
        if self.grib_version == 2:
            forecast_time = codes_get_double(msgid, "forecastTime")
        elif self.grib_version == 1:
            forecast_time = codes_get_double(msgid, "endStep")

        time_unit = codes_get_long(msgid, "stepUnits")
        if time_unit == 0:
            forecast_time /= 1440
        elif time_unit == 1:
            forecast_time /= 24

        time = ref_date_mjd + ref_time / 24 + forecast_time

        self.axis_time.append(time)

    def __extract_grib_code(self, msgid):
        discipline = 0
        category = 0
        number = 0
        if self.grib_version == 2:
            discipline = codes_get_long(msgid, "discipline")
            category = codes_get_long(msgid, "parameterCategory")
            number = codes_get_long(msgid, "parameterNumber")
        elif self.grib_version == 1:
            category = codes_get_long(msgid, "table2Version")
            number = codes_get_long(msgid, "indicatorOfParameter")

        self.param_code_1.append(discipline)
        self.param_code_2.append(category)
        self.param_code_3.append(number)

    def replace_nans(self, nan_val, new_val):
        self.data[self.data == nan_val] = new_val
