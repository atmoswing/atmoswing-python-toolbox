#!/usr/bin/python

import os
from atmoswing.files.parse.reanalysis import cfsr
from atmoswing.files.create.reanalysis import generic

dir_origin = '/gpfs/homefs/giub/horton/data/CFSR'
dir_target = '/gpfs/homefs/giub/horton/data/CFSR-g'

files_list = [['pl', 'HGT_L100', 'z'],
              ['pl', 'GP_A_L100', 'gpa'],
              ['pl', 'R_H_L100', 'r'],
              ['pl', 'SPF_H_L100', 'q'],
              ['pl', 'TMP_L100', 't'],
              ['pl', 'V_VEL_L100', 'w'],
              ['pl', 'U_GRD_L100', 'u'],
              ['pl', 'V_GRD_L100', 'v'],
              ['pl', 'V_POT_L100', 'vpot'],
              ['pl', '5WAVH_L100', '5wavh'],
              ['pl', '5WAVA_L100', '5wava'],
              ['pl', 'ABS_V_L100', 'absv'],
              ['pl', 'CLWMR_L100', 'clwmr'],
              ['pl', 'STRM_L100', 'strm'],
              ['ea', 'R_H_L200', 'r'],
              ['ea', 'C_WAT_L200', 'cwat'],
              ['ea', 'P_WAT_L200', 'pwat'],
              ['sf', 'PRES_L1', 'pres'],
              ['sf', '4LFTX_L1', '4lftx'],
              ['sf', 'LFT_X_L1', 'lftx'],
              ['sf', 'CAPE_L1', 'cape'],
              ['sf', 'CIN_L1', 'cin'],
              ['sf', 'HGT_L1', 'z'],
              ['msl', 'PRES_L101', 'pres'],
              ['msl', 'PRMSL_L101', 'msl'],
              ['pt', 'LAPR_L107', 'lapr'],
              ['pt', 'MNTSF_L107', 'msf'],
              ['pt', 'PVORT_L107', 'pv'],
              ['pt', 'R_H_L107', 'r'],
              ['pt', 'TMP_L107', 't'],
              ['pt', 'U_GRD_L107', 'u'],
              ['pt', 'V_GRD_L107', 'v'],
              ['pt', 'V_VEL_L107', 'w'],
              ['pv', 'HGT_L109', 'z'],
              ['pv', 'PRES_L109', 'pres'],
              ['pv', 'TMP_L109', 't'],
              ['pv', 'U_GRD_L109', 'u'],
              ['pv', 'V_GRD_L109', 'v'],
              ['pv', 'VW_SH_L109', 'ws']]

for file in files_list:
    dir_origin_files = os.path.join(dir_origin, file[0])
    dir_target_files = os.path.join(dir_target, file[0])
    var_name_origin = file[1]
    var_name_target = file[2]

    reanalysis = cfsr.CFSR(directory=dir_origin_files, file_pattern='pgbhnl.gdas.*.grb2.nc', var_name=var_name_origin)
    reanalysis.load()
    new_reanalysis = generic.Generic(directory=dir_target_files, var_name=var_name_target, ref_data=reanalysis)
    new_reanalysis.generate()



