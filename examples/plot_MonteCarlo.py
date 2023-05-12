#!/usr/bin/python

from atmoswing_toolbox.plots.montecarlo import MonteCarloPlot

base_dir = '...'
output_path = base_dir + '_Plots\\'

# Paths
file = '..._tested_parameters.txt'
file_calib_cp = '..._best_parameters.txt'
file_calib_vp = '..._best_parameters.txt'
file_ga1 = '..._best_individual.txt'
file_ga2 = '..._best_individual.txt'
file_ga3 = '..._best_individual.txt'


mc = MonteCarloPlot(base_dir + file, output_path)
mc.add_param(base_dir + file_calib_cp, 's', 'calib')
mc.add_param(base_dir + file_calib_vp, 's', 'valid')
mc.add_param(base_dir + file_ga1, 'v', 'calib')
mc.add_param(base_dir + file_ga2, 'v', 'valid')
mc.add_param(base_dir + file_ga3, 'v', 'calib')
mc.print()
# mc.show()
