# -*- coding: utf-8 -*-

import pandas as pd


class ResultsParamsArray(path):
    path = path
    data = {}

    def load(self):
        self.data = pd.read_csv(self.path, sep='\t', skiprows=1)
