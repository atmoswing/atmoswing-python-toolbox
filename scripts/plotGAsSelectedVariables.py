#!/usr/bin/python

from atmoswing.plots.gas import variables

base_dir = 'D:\\Projects\\ANALOGS-VARIABLES\\Analyses\\GAs experiment 01\\CFSR\\'
output_path = base_dir + '\\..\\'

res = variables.PlotsGAsVariables(base_dir, output_path)

#res.show()
res.print('CFSR-1')

