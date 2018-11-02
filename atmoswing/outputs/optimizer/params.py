# -*- coding: utf-8 -*-

import pandas as pd


class ParamsArray(object):
    """Parsing of the parameters resulting from the optimizer"""

    def __init__(self, path):
        self.path = path
        self.id = 0
        self.struct = []
        self.data = []

    def parse_headers(self):
        fid = open(self.path, "r")
        fid.readline()
        line = fid.readline().split('\t')
        self.id = line[1]

        headers = []
        cols = []
        step = 0
        ptor = 0
        for idx, row in enumerate(line):
            append = False
            if row[0:10] == '|||| Step(':
                step = int(row[10:-1])
                self.struct.append(0)
            if row[0:8] == '|| Ptor(':
                ptor = int(row[8:-1])
                self.struct[step] = ptor + 1
            if row == 'Anb':
                label = 'Anb_{}'.format(step)
                headers.append(label)
                cols.append(idx + 1)
            if row == 'Level':
                append = True
                label = 'Variable_{}_{}'.format(step, ptor)
                headers.append(label)
                cols.append(idx-1)
            if row == 'Time':
                append = True
            if row == 'xMin':
                append = True
            if row == 'xPtsNb':
                append = True
            if row == 'xStep':
                append = True
            if row == 'yMin':
                append = True
            if row == 'yPtsNb':
                append = True
            if row == 'yStep':
                append = True
            if row == 'Weight':
                append = True
            if row == 'Criteria':
                append = True
            if row == 'Calib':
                headers.append(row)
                cols.append(idx + 1)
            if row == 'Valid':
                headers.append(row)
                cols.append(idx + 1)

            if append:
                label = '{}_{}_{}'.format(row, step, ptor)
                headers.append(label)
                cols.append(idx + 1)

        fid.close()

        return [cols, headers]

    def load(self):
        file_struct = self.parse_headers()
        self.data = pd.read_csv(self.path, sep='\t', skiprows=1, usecols=file_struct[0], names=file_struct[1])

    def get_anbs(self, step):
        return self.data['Anb_{}'.format(step)]

    def get_variables(self, step, ptor):
        return self.data['Variable_{}_{}'.format(step, ptor)]

    def get_variable(self, step, ptor, index=0):
        var = self.data['Variable_{}_{}'.format(step, ptor)][index]
        if 'hgt' in var:
            var = 'Z'
        elif 'tcw' in var:
            var = 'TCW'
        elif 'omega' in var:
            var = 'W'
        elif 'press/rh' in var:
            var = 'RH'
        elif 'press/t' in var:
            var = 'T'
        return var

    def get_levels(self, step, ptor):
        return self.data['Level_{}_{}'.format(step, ptor)]

    def get_level(self, step, ptor, index=0):
        return self.data['Level_{}_{}'.format(step, ptor)][index]

    def get_times(self, step, ptor):
        return self.data['Time_{}_{}'.format(step, ptor)]

    def get_time(self, step, ptor, index=0):
        return self.data['Time_{}_{}'.format(step, ptor)][index]

    def get_xmins(self, step, ptor):
        return self.data['xMin_{}_{}'.format(step, ptor)]

    def get_xmaxs(self, step, ptor):
        return self.data['xMin_{}_{}'.format(step, ptor)] + \
               (self.data['xPtsNb_{}_{}'.format(step, ptor)] - 1) * self.data['xStep_{}_{}'.format(step, ptor)]

    def get_xptsnbs(self, step, ptor):
        return self.data['xPtsNb_{}_{}'.format(step, ptor)]

    def get_ymins(self, step, ptor):
        return self.data['yMin_{}_{}'.format(step, ptor)]

    def get_ymaxs(self, step, ptor):
        return self.data['yMin_{}_{}'.format(step, ptor)] + \
               (self.data['yPtsNb_{}_{}'.format(step, ptor)] - 1) * self.data['yStep_{}_{}'.format(step, ptor)]

    def get_yptsnbs(self, step, ptor):
        return self.data['yPtsNb_{}_{}'.format(step, ptor)]

    def get_weights(self, step, ptor):
        return self.data['Weight_{}_{}'.format(step, ptor)]

    def get_criteria(self, step, ptor):
        return self.data['Criteria_{}_{}'.format(step, ptor)]

    def get_calib_scores(self):
        return self.data['Calib']

    def get_valid_scores(self):
        return self.data['Valid']
