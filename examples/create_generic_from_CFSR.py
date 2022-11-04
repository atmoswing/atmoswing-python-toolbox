#!/usr/bin/python

import os

from atmoswing.files.create.predictors import generic
from atmoswing.files.parse.predictors import netcdf_dataset

dir_origin = 'path/to/data'
dir_target = 'path/to/outputs'

files_list = [['isobaric', 'HGT_L100', 'z'],
              ['isobaric', 'GP_A_L100', 'gpa'],
              ['isobaric', 'R_H_L100', 'r'],
              ['isobaric', 'SPF_H_L100', 'q'],
              ['isobaric', 'TMP_L100', 't'],
              ['isobaric', 'V_VEL_L100', 'w'],
              ['isobaric', 'U_GRD_L100', 'u'],
              ['isobaric', 'V_GRD_L100', 'v'],
              ['isobaric', 'V_POT_L100', 'vpot'],
              ['isobaric', '5WAVH_L100', '5wavh'],
              ['isobaric', '5WAVA_L100', '5wava'],
              ['isobaric', 'ABS_V_L100', 'absv'],
              ['isobaric', 'CLWMR_L100', 'clwmr'],
              ['isobaric', 'STRM_L100', 'strm'],
              ['entire_atmosphere', 'R_H_L200', 'r'],
              ['entire_atmosphere', 'C_WAT_L200', 'cwat'],
              ['entire_atmosphere', 'P_WAT_L200', 'pwat'],
              ['ground', 'PRES_L1', 'pres'],
              ['ground', '4LFTX_L1', '4lftx'],
              ['ground', 'LFT_X_L1', 'lftx'],
              ['ground', 'CAPE_L1', 'cape'],
              ['ground', 'CIN_L1', 'cin'],
              ['ground', 'HGT_L1', 'z'],
              ['msl', 'PRES_L101', 'pres'],
              ['msl', 'PRMSL_L101', 'msl'],
              ['isentropic', 'LAPR_L107', 'lapr'],
              ['isentropic', 'MNTSF_L107', 'msf'],
              ['isentropic', 'PVORT_L107', 'pv'],
              ['isentropic', 'R_H_L107', 'r'],
              ['isentropic', 'TMP_L107', 't'],
              ['isentropic', 'U_GRD_L107', 'u'],
              ['isentropic', 'V_GRD_L107', 'v'],
              ['isentropic', 'V_VEL_L107', 'w'],
              ['pv_surface', 'HGT_L109', 'z'],
              ['pv_surface', 'PRES_L109', 'pres'],
              ['pv_surface', 'TMP_L109', 't'],
              ['pv_surface', 'U_GRD_L109', 'u'],
              ['pv_surface', 'V_GRD_L109', 'v'],
              ['pv_surface', 'VW_SH_L109', 'ws']]

for file in files_list:
    dir_origin_files = os.path.join(dir_origin, file[0])
    dir_target_files = os.path.join(dir_target, file[0])
    var_name_origin = file[1]
    var_name_target = file[2]

    reanalysis = netcdf_dataset.NetCDF(directory=dir_origin_files,
                                       file_pattern='*.grb2.nc',
                                       var_name=var_name_origin)
    reanalysis.load()
    new_reanalysis = generic.Generic(directory=dir_target_files,
                                     var_name=var_name_target,
                                     ref_data=reanalysis)
    new_reanalysis.generate()
