#!/usr/bin/python

import os
from atmoswing.files.parse.predictors import netcdf_dataset

dir_origin = 'path/to/data'
dir_target = 'path/to/outputs'

files_list = [['', 'z', 'z']]

spatial_stride = 8  # 1°

for file in files_list:
    dir_origin_files = os.path.join(dir_origin, file[0])
    dir_target_files = os.path.join(dir_target, file[0])
    var_name_origin = file[1]
    var_name_target = file[2]

    reanalysis = netcdf_dataset.NetCDF(directory=dir_origin_files, file_pattern=file[1] + '.*.nc',
                                       var_name=var_name_origin)
    reanalysis.create_generic_individual_files(directory=dir_target_files, var_name=var_name_target,
                                               spatial_stride=spatial_stride)
