#!/usr/bin/python

from atmoswing.plots import montecarlo

baseDir = 'D:\\Projects\\ANALOGS\\Analyses\\Parameters space\\'

# 2Z
file = 'Monte Carlo\\Results\\51035\\results\\20181122-1551_station_35_tested_parameters.txt'
file_calib_cp = 'Calibration\\Results\\2510351\\results\\20181122-1548_station_35_best_parameters.txt'
file_calib_vp = 'Calibration\\Results\\2510352\\results\\20181123-0953_station_35_best_parameters.txt'
file_ga1 = 'GAs\\Results\\11510351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga2 = 'GAs\\Results\\11510352\\results\\20181125-2058_station_35_best_individual.txt'
file_ga3 = 'GAs\\Results\\12510351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga4 = 'GAs\\Results\\12510352\\results\\20181125-2133_station_35_best_individual.txt'
file_ga5 = 'GAs\\Results\\13510351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga6 = 'GAs\\Results\\13510352\\results\\20181125-2228_station_35_best_individual.txt'
file_ga7 = 'GAs\\Results\\14510351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga8 = 'GAs\\Results\\14510352\\results\\20181125-2342_station_35_best_individual.txt'
file_ga9 = 'GAs\\Results\\15510351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga10 = 'GAs\\Results\\15510352\\results\\20181126-0045_station_35_best_individual.txt'
file_ga11 = 'GAs\\Results\\16510351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga12 = 'GAs\\Results\\16510352\\results\\20181126-0244_station_35_best_individual.txt'
file_ga13 = 'GAs\\Results\\17510351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga14 = 'GAs\\Results\\17510352\\results\\20181126-0351_station_35_best_individual.txt'

# 2Z-2MI
file = 'Monte Carlo\\Results\\52035\\results\\20181122-1551_station_35_tested_parameters.txt'
#file = 'Monte Carlo\\Results\\520351\\results\\20181129-1955_station_35_tested_parameters.txt'
file_calib_cp = 'Calibration\\Results\\2520351\\results\\20181122-1549_station_35_best_parameters.txt'
file_calib_vp = 'Calibration\\Results\\2520352\\results\\20181123-0954_station_35_best_parameters.txt'
file_ga1 = 'GAs\\Results\\11520351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga2 = 'GAs\\Results\\11520352\\results\\20181126-0629_station_35_best_individual.txt'
file_ga3 = 'GAs\\Results\\12520351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga4 = 'GAs\\Results\\12520352\\results\\20181126-0719_station_35_best_individual.txt'
file_ga5 = 'GAs\\Results\\13520351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga6 = 'GAs\\Results\\13520352\\results\\20181126-0727_station_35_best_individual.txt'
file_ga7 = 'GAs\\Results\\14520351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga8 = 'GAs\\Results\\14520352\\results\\20181126-0828_station_35_best_individual.txt'
file_ga9 = 'GAs\\Results\\15520351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga10 = 'GAs\\Results\\15520352\\results\\20181126-1020_station_35_best_individual.txt'
file_ga11 = 'GAs\\Results\\16520351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga12 = 'GAs\\Results\\16520352\\results\\20181126-1137_station_35_best_individual.txt'
file_ga13 = 'GAs\\Results\\17520351\\results\\20181123-1328_station_35_best_individual.txt'
file_ga14 = 'GAs\\Results\\17520352\\results\\20181126-1251_station_35_best_individual.txt'


# PT-2Z-2MI
file = 'Monte Carlo\\Results\\53035\\results\\20181122-1551_station_35_tested_parameters.txt'
file_calib_cp = 'Calibration\\Results\\2530351\\results\\20181122-1550_station_35_best_parameters.txt'
file_calib_vp = 'Calibration\\Results\\2530352\\results\\20181123-0955_station_35_best_parameters.txt'
file_ga1 = 'GAs\\Results\\11530351\\results\\20181123-1421_station_35_best_individual.txt'
#file_ga2 = 'GAs\\Results\\11530352\\results\\20181125-2058_station_35_best_individual.txt'
file_ga3 = 'GAs\\Results\\12530351\\results\\20181123-1909_station_35_best_individual.txt'
#file_ga4 = 'GAs\\Results\\12530352\\results\\20181125-2133_station_35_best_individual.txt'
file_ga5 = 'GAs\\Results\\13530351\\results\\20181123-2119_station_35_best_individual.txt'
#file_ga6 = 'GAs\\Results\\13530352\\results\\20181125-2228_station_35_best_individual.txt'
file_ga7 = 'GAs\\Results\\14530351\\results\\20181123-2207_station_35_best_individual.txt'
#file_ga8 = 'GAs\\Results\\14530352\\results\\20181125-2342_station_35_best_individual.txt'
file_ga9 = 'GAs\\Results\\15530351\\results\\20181124-0028_station_35_best_individual.txt'
#file_ga10 = 'GAs\\Results\\15530352\\results\\20181126-0045_station_35_best_individual.txt'
file_ga11 = 'GAs\\Results\\16530351\\results\\20181124-0029_station_35_best_individual.txt'
#file_ga12 = 'GAs\\Results\\16530352\\results\\20181126-0244_station_35_best_individual.txt'
file_ga13 = 'GAs\\Results\\17530351\\results\\20181124-0205_station_35_best_individual.txt'
#file_ga14 = 'GAs\\Results\\17530352\\results\\20181126-0351_station_35_best_individual.txt'


# 4Z
file = 'Monte Carlo\\Results\\55035\\results\\20181122-1551_station_35_tested_parameters.txt'
file_calib_cp = 'Calibration\\Results\\2550351\\results\\20181122-1549_station_35_best_parameters.txt'
file_calib_vp = 'Calibration\\Results\\2550352\\results\\20181123-0954_station_35_best_parameters.txt'
file_ga1 = 'GAs\\Results\\11550351\\results\\20181124-0219_station_35_best_individual.txt'
#file_ga2 = 'GAs\\Results\\11550352\\results\\20181125-2058_station_35_best_individual.txt'
file_ga3 = 'GAs\\Results\\12550351\\results\\20181124-0330_station_35_best_individual.txt'
#file_ga4 = 'GAs\\Results\\12550352\\results\\20181125-2133_station_35_best_individual.txt'
file_ga5 = 'GAs\\Results\\13550351\\results\\20181124-0528_station_35_best_individual.txt'
#file_ga6 = 'GAs\\Results\\13550352\\results\\20181125-2228_station_35_best_individual.txt'
file_ga7 = 'GAs\\Results\\14550351\\results\\20181124-0745_station_35_best_individual.txt'
#file_ga8 = 'GAs\\Results\\14550352\\results\\20181125-2342_station_35_best_individual.txt'
file_ga9 = 'GAs\\Results\\15550351\\results\\20181124-0912_station_35_best_individual.txt'
#file_ga10 = 'GAs\\Results\\15550352\\results\\20181126-0045_station_35_best_individual.txt'
file_ga11 = 'GAs\\Results\\16550351\\results\\20181124-1144_station_35_best_individual.txt'
#file_ga12 = 'GAs\\Results\\16550352\\results\\20181126-0244_station_35_best_individual.txt'
file_ga13 = 'GAs\\Results\\17550351\\results\\20181124-1237_station_35_best_individual.txt'
#file_ga14 = 'GAs\\Results\\17550352\\results\\20181126-0351_station_35_best_individual.txt'


# 4Z-2MI
file = 'Monte Carlo\\Results\\56035\\results\\20181122-1551_station_35_tested_parameters.txt'
file_calib_cp = 'Calibration\\Results\\2560351\\results\\20181122-1550_station_35_best_parameters.txt'
file_calib_vp = 'Calibration\\Results\\2560352\\results\\20181123-0955_station_35_best_parameters.txt'
file_ga1 = 'GAs\\Results\\11560351\\results\\20181124-1251_station_35_best_individual.txt'
#file_ga2 = 'GAs\\Results\\11560352\\results\\20181125-2058_station_35_best_individual.txt'
file_ga3 = 'GAs\\Results\\12560351\\results\\20181124-1254_station_35_best_individual.txt'
#file_ga4 = 'GAs\\Results\\12560352\\results\\20181125-2133_station_35_best_individual.txt'
file_ga5 = 'GAs\\Results\\13560351\\results\\20181124-1940_station_35_best_individual.txt'
#file_ga6 = 'GAs\\Results\\13560352\\results\\20181125-2228_station_35_best_individual.txt'
file_ga7 = 'GAs\\Results\\14560351\\results\\20181125-0238_station_35_best_individual.txt'
#file_ga8 = 'GAs\\Results\\14560352\\results\\20181125-2342_station_35_best_individual.txt'
file_ga9 = 'GAs\\Results\\15560351\\results\\20181125-0248_station_35_best_individual.txt'
#file_ga10 = 'GAs\\Results\\15560352\\results\\20181126-0045_station_35_best_individual.txt'
file_ga11 = 'GAs\\Results\\16560351\\results\\20181125-0321_station_35_best_individual.txt'
#file_ga12 = 'GAs\\Results\\16560352\\results\\20181126-0244_station_35_best_individual.txt'
file_ga13 = 'GAs\\Results\\17560351\\results\\20181125-0536_station_35_best_individual.txt'
#file_ga14 = 'GAs\\Results\\17560352\\results\\20181126-0351_station_35_best_individual.txt'


# PT-2Z-4W-4MI
file = 'Monte Carlo\\Results\\57035\\results\\20181122-1552_station_35_tested_parameters.txt'
file_calib_cp = 'Calibration\\Results\\2570351\\results\\20181122-1552_station_35_best_parameters.txt'
file_calib_vp = 'Calibration\\Results\\2570352\\results\\20181123-0956_station_35_best_parameters.txt'
#file_ga1 = 'GAs\\Results\\11570351\\results\\20181124-1251_station_35_best_individual.txt'
#file_ga2 = 'GAs\\Results\\11570352\\results\\20181125-2058_station_35_best_individual.txt'
#file_ga3 = 'GAs\\Results\\12570351\\results\\20181124-1254_station_35_best_individual.txt'
#file_ga4 = 'GAs\\Results\\12570352\\results\\20181125-2133_station_35_best_individual.txt'
#file_ga5 = 'GAs\\Results\\13570351\\results\\20181124-1940_station_35_best_individual.txt'
#file_ga6 = 'GAs\\Results\\13570352\\results\\20181125-2228_station_35_best_individual.txt'
#file_ga7 = 'GAs\\Results\\14570351\\results\\20181125-0238_station_35_best_individual.txt'
#file_ga8 = 'GAs\\Results\\14570352\\results\\20181125-2342_station_35_best_individual.txt'
#file_ga9 = 'GAs\\Results\\15570351\\results\\20181125-0248_station_35_best_individual.txt'
#file_ga10 = 'GAs\\Results\\15570352\\results\\20181126-0045_station_35_best_individual.txt'
#file_ga11 = 'GAs\\Results\\16570351\\results\\20181125-0321_station_35_best_individual.txt'
#file_ga12 = 'GAs\\Results\\16570352\\results\\20181126-0244_station_35_best_individual.txt'
#file_ga13 = 'GAs\\Results\\17570351\\results\\20181125-0536_station_35_best_individual.txt'
#file_ga14 = 'GAs\\Results\\17570352\\results\\20181126-0351_station_35_best_individual.txt'

output_path = baseDir + '_Plots\\'

mc = montecarlo.PlotsParamsSensitivity(baseDir + file, output_path)
mc.add_param(baseDir + file_calib_cp, 's', 'calib')
mc.add_param(baseDir + file_calib_vp, 's', 'valid')
mc.add_param(baseDir + file_ga1, 'v', 'calib')
mc.add_param(baseDir + file_ga2, 'v', 'valid')
mc.add_param(baseDir + file_ga3, 'v', 'calib')
mc.add_param(baseDir + file_ga4, 'v', 'valid')
mc.add_param(baseDir + file_ga5, 'v', 'calib')
mc.add_param(baseDir + file_ga6, 'v', 'valid')
mc.add_param(baseDir + file_ga7, 'v', 'calib')
mc.add_param(baseDir + file_ga8, 'v', 'valid')
mc.add_param(baseDir + file_ga9, 'v', 'calib')
mc.add_param(baseDir + file_ga10, 'v', 'valid')
mc.add_param(baseDir + file_ga11, 'v', 'calib')
mc.add_param(baseDir + file_ga12, 'v', 'valid')
mc.add_param(baseDir + file_ga13, 'v', 'calib')
mc.add_param(baseDir + file_ga14, 'v', 'valid')
mc.print()
# mc.show()
