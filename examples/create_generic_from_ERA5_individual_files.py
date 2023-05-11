#!/usr/bin/python

import os

from atmoswing_toolbox.datasets import netcdf_dataset

dir_origin = 'path/to/data'
dir_target = 'path/to/outputs'
var_name_origin = 'z'
var_name_target = 'z'

spatial_stride = 4  # 1°

dir_origin_files = os.path.join(dir_origin)
dir_target_files = os.path.join(dir_target)

reanalysis = netcdf_dataset.NetCDF(
    directory=dir_origin_files,
    file_pattern=var_name_origin + '.*.nc',
    var_name=var_name_origin)

reanalysis.create_generic_individual_files(
    directory=dir_target_files,
    var_name=var_name_target,
    spatial_stride=spatial_stride)
