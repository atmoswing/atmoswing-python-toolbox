# -*- coding: utf-8 -*-

import pandas as pd


class ResultsParamsArray(path):
    path = path
    id = 0
    struct = []
    data = []

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
            if row[0:8] == '|| Ptor(':
                ptor = int(row[8:-1])
            if row == '|':
                label = 'Variable_{}_{}'.format(step, ptor)
                headers.append(label)
                cols.append(idx + 2)
            if row == 'Anb':
                label = 'Anb_{}'.format(step)
                headers.append(label)
                cols.append(idx + 1)
            if row == 'Level':
                append = True
            if row == 'Time':
                append = True
            if row == 'xMin':
                append = True
            if row == 'xPtsNb':
                append = True
            if row == 'yMin':
                append = True
            if row == 'yPtsNb':
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

    def get_anb(self, step):
        return self.data['Anb_{}'.format(step)]

    def get_level(self, step, ptor):
        return self.data['Level_{}_{}'.format(step, ptor)]

    def get_time(self, step, ptor):
        return self.data['Time_{}_{}'.format(step, ptor)]

    def get_xmin(self, step, ptor):
        return self.data['xMin_{}_{}'.format(step, ptor)]

    def get_xptsnb(self, step, ptor):
        return self.data['xPtsNb_{}_{}'.format(step, ptor)]

    def get_ymin(self, step, ptor):
        return self.data['yMin_{}_{}'.format(step, ptor)]

    def get_yptsnb(self, step, ptor):
        return self.data['yPtsNb_{}_{}'.format(step, ptor)]

    def get_weight(self, step, ptor):
        return self.data['Weight_{}_{}'.format(step, ptor)]

    def get_criteria(self, step, ptor):
        return self.data['Criteria_{}_{}'.format(step, ptor)]

    def get_calib_score(self):
        return self.data['Calib']

    def get_valid_score(self):
        return self.data['Valid']
