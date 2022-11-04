import os

import numpy as np


class Idaweb:
    """Extract Idaweb (MeteoSwiss) time series"""

    def __init__(self, file_path='', header_lines=3):
        self.file_path = file_path
        self.header_lines = header_lines

    def parse(self):
        if not os.path.isfile(self.file_path):
            raise Exception(f'File {self.file_path} not found')

        matrix = []

        # Read content
        fid = open(self.file_path)
        file_content = fid.readlines()

        for line in file_content:
            self.header_lines -= 1
            if self.header_lines < 0:
                words_line = line.split()
                if len(words_line) > 1:
                    date_str = words_line[1]

                    y = int(float(date_str[0:4]))
                    m = int(float(date_str[4:6]))
                    d = int(float(date_str[6:8]))
                    if words_line[2] == '-':
                        val = np.NaN
                    else:
                        val = float(words_line[2])

                    line = [y, m, d, val]
                    matrix.append(line)

        np_matrix = np.array(matrix)

        return np_matrix
