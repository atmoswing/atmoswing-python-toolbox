from atmoswing.plots import montecarlo

file = '...'
output_path = '...'

mc = montecarlo.PlotsParamsSensitivity(file, output_path)
mc.print()
