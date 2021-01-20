#!/usr/bin/python

import os
from atmoswing.plots.gas import variables

base_dir = 'D:\\Projects_Unibe\\2020 Analogs IVS\\Analyses\\3 - GAs optim all catchments\\results\\1*/'
output_path = base_dir + '\\..\\'

res = variables.PlotsGAsVariables(base_dir, output_path)
res.marker_size_on_weight = True
res.marker_size_max = 40
res.marker_alpha = 0.8
res.load()

res.print_scatter('fig-1x')
res.print_variables_importance('fig-1x-importance')
