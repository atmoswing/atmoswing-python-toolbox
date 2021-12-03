#!/usr/bin/python

import os
from atmoswing.plots.gas import variables

base_dir = 'D:\\_Unibe\\2020 Analogs IVS\\Analyses\\4 - GAs optim ERA5\\results\\2*/'
output_path = base_dir + '\\..\\'

res = variables.PlotsGAsVariables(base_dir, output_path)
res.marker_size_on_weight = True
res.marker_size_max = 40
res.marker_alpha = 0.8
res.load()

res.print_scatter('fig-1x')
res.print_syntheses('fig-1x-importance')
