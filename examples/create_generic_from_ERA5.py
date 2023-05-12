#!/usr/bin/python

import os

from atmoswing_toolbox.datasets import generic_dataset, netcdf_dataset

dir_origin = 'path/to/data'
dir_target = 'path/to/outputs'

files_list = [['pressure', 'cc', 'cc'],
              ['pressure', 'd', 'd'],
              ['pressure', 'pv', 'pv'],
              ['pressure', 'r', 'r'],
              ['pressure', 't', 't'],
              ['pressure', 'u', 'u'],
              ['pressure', 'v', 'v'],
              ['pressure', 'w', 'w'],
              ['pressure', 'z', 'z'],
              ['single', 'cape', 'cape'],
              ['single', 'cin', 'cin'],
              ['single', 'deg0l', 'deg0l'],
              ['single', 'lcc', 'lcc'],
              ['single', 'msl', 'msl'],
              ['single', 'slhf', 'slhf'],
              ['single', 'sshf', 'sshf'],
              ['single', 'ssr', 'ssr'],
              ['single', 'ssrd', 'ssrd'],
              ['single', 'str', 'str'],
              ['single', 'strd', 'strd'],
              ['single', 't2m', 't2m'],
              ['single', 'tcc', 'tcc'],
              ['single', 'tcw', 'tcw'],
              ['single', 'tsr', 'tsr'],
              ['single', 'ttr', 'ttr'],
              ['single', 'u10', 'u10'],
              ['single', 'v10', 'v10']]

for file in files_list:
    dir_origin_files = os.path.join(dir_origin, file[0])
    dir_target_files = os.path.join(dir_target, file[0])
    var_name_origin = file[1]
    var_name_target = file[2]

    reanalysis = netcdf_dataset.NetcdfDataset(
        directory=dir_origin_files,
        file_pattern=file[1] + '.*.nc',
        var_name=var_name_origin)
    reanalysis.load(spatial_stride=2)  # reduce resolution to 0.5°
    reanalysis.replace_nans(-32767, 0.0000001)  # avoid division by 0.
    new_reanalysis = generic_dataset.GenericDataset(
        directory=dir_target_files,
        var_name=var_name_target,
        ref_data=reanalysis)
    new_reanalysis.generate()
