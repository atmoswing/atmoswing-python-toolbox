#!/usr/bin/python

import os
os.environ.setdefault("ECCODES_DIR", "/usr/local/")
from atmoswing.files.parse.predictors import dataset
from atmoswing.files.parse.predictors import grib_dataset
from atmoswing.files.create.predictors import generic

dir_origin = 'path/to/data'
dir_target = 'path/to/outputs'

files_list = [['data', '10u_sfc_*.grib', '10u_sfc'],
              ['data', 'cp_sfc_*.grib', 'cp_sfc'],
              ['data', 'gh_500_*.grib', 'gh_500'],
              ['data', 'r_500_*.grib', 'r_500'],
              ['data', 't_500_*.grib', 't_500'],
              ['data', 't_700_*.grib', 't_700'],
              ['data', 'v_925_*.grib', 'v_925'],
              ['datader', 'q_850_*.grib', 'q_850'],
              ['datader', 'thetaES_500_*.grib', 'thetaES_500'],
              ['datader', 'thetaES_925_*.grib', 'thetaES_925'],
              ['vertdiff', 'DP500925_*.grib', 'DP500925'],
              ['vertdiff', 'MB500850_*.grib', 'MB500850'],
              ['vertdiff', 'MB500925_*.grib', 'MB500925'],
              ['vertdiff', 'MB700925_*.grib', 'MB700925']]

for file in files_list:
    dir_origin_files = os.path.join(dir_origin, file[0])
    dir_target_files = dir_target
    pattern = file[1]
    var_name_target = file[2]

    reanalysis = grib_dataset.Grib(directory=dir_origin_files, file_pattern=pattern)
    reanalysis.load()
    reanalysis.standardize(mode=dataset.DOMAIN_WISE)
    print('Creating new file.')
    new_reanalysis = generic.Generic(directory=dir_target_files, var_name=var_name_target, ref_data=reanalysis)
    new_reanalysis.generate(format=generic.NETCDF_4)
