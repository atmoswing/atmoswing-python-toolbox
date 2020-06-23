#!/usr/bin/python

import os
from atmoswing.files.parse.predictors import netcdf
from atmoswing.files.create.predictors import generic

files_list = [['anl_column125', 'anl_column125.054_pwat.*', 'PWAT_GDS0_EATM', 'pwat'],
              ['anl_column125', 'anl_column125.152_vwv.*', 'VWV_GDS0_EATM', 'vwv'],
              ['anl_column125', 'anl_column125.157_uwv.*', 'UWV_GDS0_EATM', 'uwv'],
              ['anl_column125', 'anl_column125.190_uthe.*', 'UTHE_GDS0_EATM', 'uthe'],
              ['anl_column125', 'anl_column125.191_vthe.*', 'VTHE_GDS0_EATM', 'vthe'],
              ['anl_isentrop125', 'anl_isentrop125.001_pres.*', 'PRES_GDS0_THEL', 'pres'],
              ['anl_isentrop125', 'anl_isentrop125.004_pvor.*', 'pVOR_GDS0_THEL', 'pvor'],
              ['anl_isentrop125', 'anl_isentrop125.007_hgt.*', 'HGT_GDS0_THEL', 'hgt'],
              ['anl_isentrop125', 'anl_isentrop125.033_ugrd.*', 'UGRD_GDS0_THEL', 'ugrd'],
              ['anl_isentrop125', 'anl_isentrop125.034_vgrd.*', 'VGRD_GDS0_THEL', 'vgrd'],
              ['anl_isentrop125', 'anl_isentrop125.037_mntsf.*', 'MNTSF_GDS0_THEL', 'mntsf'],
              ['anl_isentrop125', 'anl_isentrop125.039_vvel.*', 'VVEL_GDS0_THEL', 'vvel'],
              ['anl_isentrop125', 'anl_isentrop125.132_bvf2.*', 'BVF2_GDS0_THEL', 'bvf2'],
              ['anl_land125', 'anl_land125.065_snwe.*', 'SnWe_GDS0_SFC', 'snwe'],
              ['anl_land125', 'anl_land125.085_soilt.*', 'SoilT_GDS0_ESOIL', 'soilt'],
              ['anl_land125', 'anl_land125.144_tsc.*', 'TSC_GDS0_SFC', 'tsc'],
              ['anl_land125', 'anl_land125.145_tsg.*', 'TSG_GDS0_SFC', 'tsg'],
              ['anl_land125', 'anl_land125.225_soilw.*', 'SoilW_GDS0_ULN', 'soilw'],
              ['anl_p125', 'anl_p125.007_hgt.*', 'HGT_GDS0_ISBL', 'hgt'],
              ['anl_p125', 'anl_p125.011_tmp.*', 'TMP_GDS0_ISBL', 'tmp'],
              ['anl_p125', 'anl_p125.018_depr.*', 'DEPR_GDS0_ISBL', 'depr'],
              ['anl_p125', 'anl_p125.033_ugrd.*', 'UGRD_GDS0_ISBL', 'ugrd'],
              ['anl_p125', 'anl_p125.034_vgrd.*', 'VGRD_GDS0_ISBL', 'vgrd'],
              ['anl_p125', 'anl_p125.035_strm.*', 'STRM_GDS0_ISBL', 'strm'],
              ['anl_p125', 'anl_p125.036_vpot.*', 'VPOT_GDS0_ISBL', 'vpot'],
              ['anl_p125', 'anl_p125.039_vvel.*', 'VVEL_GDS0_ISBL', 'vvel'],
              ['anl_p125', 'anl_p125.043_relv.*', 'xRELV_GDS0_ISBL', 'relv'],
              ['anl_p125', 'anl_p125.044_reld.*', 'RELD_GDS0_ISBL', 'reld'],
              ['anl_p125', 'anl_p125.051_spfh.*', 'SPFH_GDS0_ISBL', 'spfh'],
              ['anl_p125', 'anl_p125.052_rh.*', 'RH_GDS0_ISBL', 'rh'],
              ['anl_snow125', 'anl_snow125.066_snowd.*', 'SnowD_GDS0_SFC', 'snowd'],
              ['anl_surf125', 'anl_surf125.001_pres.*', 'PRES_GDS0_SFC', 'pres'],
              ['anl_surf125', 'anl_surf125.002_prmsl.*', 'PRMSL_GDS0_MSL', 'prmsl'],
              ['anl_surf125', 'anl_surf125.011_tmp.*', 'TMP_GDS0_HTGL', 'tmp'],
              ['anl_surf125', 'anl_surf125.013_pot.*', 'POT_GDS0_SFC', 'pot'],
              ['anl_surf125', 'anl_surf125.018_depr.*', 'DEPR_GDS0_HTGL', 'depr'],
              ['anl_surf125', 'anl_surf125.033_ugrd.*', 'UGRD_GDS0_HTGL', 'ugrd'],
              ['anl_surf125', 'anl_surf125.034_vgrd.*', 'VGRD_GDS0_HTGL', 'vgrd'],
              ['anl_surf125', 'anl_surf125.051_spfh.*', 'SPFH_GDS0_HTGL', 'spfh'],
              ['anl_surf125', 'anl_surf125.052_rh.*', 'RH_GDS0_HTGL', 'rh'],
              ['fcst_column125', 'fcst_column125.054_pwat.*', 'PWAT_GDS0_EATM', 'pwat'],
              ['fcst_column125', 'fcst_column125.152_vwv.*', 'VWV_GDS0_EATM', 'vwv'],
              ['fcst_column125', 'fcst_column125.157_uwv.*', 'UWV_GDS0_EATM', 'uwv'],
              ['fcst_column125', 'fcst_column125.190_uthe.*', 'UTHE_GDS0_EATM', 'uthe'],
              ['fcst_column125', 'fcst_column125.191_vthe.*', 'VTHE_GDS0_EATM', 'vthe'],
              ['fcst_column125', 'fcst_column125.227_cw.*', 'CW_GDS0_EATM', 'cw'],
              ['fcst_land125', 'fcst_land125.065_snwe.*', 'SnWe_GDS0_SFC', 'snwe'],
              ['fcst_land125', 'fcst_land125.066_snowd.*', 'SnowD_GDS0_SFC', 'snowd'],
              ['fcst_land125', 'fcst_land125.085_soilt.*', 'SoilT_GDS0_ESOIL', 'soilt'],
              ['fcst_land125', 'fcst_land125.145_tsg.*', 'TSG_GDS0_SFC', 'tsg'],
              ['fcst_land125', 'fcst_land125.224_msg.*', 'MSG_GDS0_SFC', 'msg'],
              ['fcst_land125', 'fcst_land125.225_soilw.*', 'SoilW_GDS0_ULN', 'soilw'],
              ['fcst_p125', 'fcst_p125.221_cwat.*', 'CWAT_GDS0_ISBL', 'cwat'],
              ['fcst_p125', 'fcst_p125.228_clwc.*', 'CLWC_GDS0_ISBL', 'clwc']]
dir_origin = 'F:\\Reanalyses\\JRA-55-sub-more-vars\\'
dir_target = 'F:\\Reanalyses\\JRA-55-sub-more-vars-generic'


for file in files_list:
    dir_origin_files = os.path.join(dir_origin, file[0])
    dir_target_files = os.path.join(dir_target, file[0])
    var_name_origin = file[2]
    var_name_target = file[3]

    reanalysis = netcdf.NetCDF(directory=dir_origin_files, file_pattern=file[1], var_name=var_name_origin)
    reanalysis.load()
    new_reanalysis = generic.Generic(directory=dir_target_files, var_name=var_name_target, ref_data=reanalysis)
    new_reanalysis.generate()



