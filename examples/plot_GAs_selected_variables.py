#!/usr/bin/python

import matplotlib.pyplot as plt

from atmoswing_toolbox.plots.gas import variables

era5_results = True

if era5_results:
    base_dir = 'path/to/data'
else:
    base_dir = 'path/to/data'

output_path = base_dir + '\\..\\'

res = variables.PlotsGAsVariables(base_dir, output_path)
res.marker_size_on_weight = True
res.marker_size_max = 40
res.marker_alpha = 0.8

if era5_results:
    res.crit = ['S0', 'S1', 'S2']
    res.colors = plt.get_cmap('tab10').colors[1:]
    res.time_step = 3

res.load()

res.print_scatter('fig-1x')
res.print_syntheses('fig-1x-importance')
