#!/usr/bin/python

import os

from atmoswing.files.create.predictors import generic
from atmoswing.files.parse.predictors import netcdf_dataset

dir_origin = 'path/to/data'
dir_target = 'path/to/outputs'

files_list = [['pressure', 'd', 'd'],
              ['pressure', 'pv', 'pv'],
              ['pressure', 'q', 'q'],
              ['pressure', 'r', 'r'],
              ['pressure', 't', 't'],
              ['pressure', 'u', 'u'],
              ['pressure', 'v', 'v'],
              ['pressure', 'vo', 'vo'],
              ['pressure', 'w', 'w'],
              ['pressure', 'z', 'z'],
              ['potential_temperature', 'd', 'd'],
              ['potential_temperature', 'mont', 'mont'],
              ['potential_temperature', 'pres', 'pres'],
              ['potential_temperature', 'pv', 'pv'],
              ['potential_temperature', 'q', 'q'],
              ['potential_temperature', 'u', 'u'],
              ['potential_temperature', 'v', 'v'],
              ['potential_temperature', 'vo', 'vo'],
              ['surface_analysis', 'd2m', 'd2m'],
              ['surface_analysis', 'msl', 'msl'],
              ['surface_analysis', 'sd', 'sd'],
              ['surface_analysis', 'sst', 'sst'],
              ['surface_analysis', 't2m', 't2m'],
              ['surface_analysis', 'tcw', 'tcw'],
              ['surface_analysis', 'tcwv', 'tcwv'],
              ['surface_analysis', 'u10', 'u10'],
              ['surface_analysis', 'v10', 'v10'],
              ['surface_analysis', 'tp', 'tp'],
              ['surface_forecast', 'cape', 'cape'],
              ['surface_forecast', 'ie', 'ie'],
              ['surface_forecast', 'ssr', 'ssr'],
              ['surface_forecast', 'ssrd', 'ssrd'],
              ['surface_forecast', 'str', 'str'],
              ['surface_forecast', 'strd', 'strd'],
              ['potential_vorticity', 'pres', 'pres'],
              ['potential_vorticity', 'pt', 'pt'],
              ['potential_vorticity', 'u', 'u'],
              ['potential_vorticity', 'v', 'v'],
              ['potential_vorticity', 'z', 'z']]

for file in files_list:
    dir_origin_files = os.path.join(dir_origin, file[0])
    dir_target_files = os.path.join(dir_target, file[0])
    var_name_origin = file[1]
    var_name_target = file[2]

    reanalysis = netcdf_dataset.NetCDF(directory=dir_origin_files,
                                       file_pattern='*.nc',
                                       var_name=var_name_origin)
    reanalysis.load()
    new_reanalysis = generic.Generic(directory=dir_target_files,
                                     var_name=var_name_target,
                                     ref_data=reanalysis)
    new_reanalysis.generate()
