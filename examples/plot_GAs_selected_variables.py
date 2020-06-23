#!/usr/bin/python

import os
from atmoswing.plots.gas import variables

base_dir = os.path.join(base_path, experiment, reanalysis)
output_path = base_dir + '\\..\\'

res = variables.PlotsGAsVariables(base_dir, output_path)

#res.show()
res.print('CFSR-1')

