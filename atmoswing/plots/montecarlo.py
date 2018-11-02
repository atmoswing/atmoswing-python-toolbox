# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
from atmoswing.outputs.optimizer import params


class PlotsParamsSensitivity(object):
    """Plotting the results of the Monte Carlo analysis"""

    def __init__(self, file, output_path='', score='CRPSS'):
        self.fig = None
        self.results = params.ParamsArray(file)
        self.results.load()
        self.output_path = output_path
        self.score = score
        self.do_print = False

    def show(self):
        self.loop_structure()

    def print(self):
        if not self.output_path:
            raise Exception('Output path not provided')
        self.do_print = True
        self.loop_structure()

    def loop_structure(self):
        for i_step, step in enumerate(self.results.struct):
            title = 'Level {}'.format(i_step + 1)
            self.scatter(self.results.get_anbs(i_step), xlabel='Number of analogues', title=title)
            for i_ptor in range(0, step):
                title = 'Level {} - {}{} {}h'.format(i_step + 1, self.results.get_variable(i_step, i_ptor),
                                                     self.results.get_level(i_step, i_ptor),
                                                     self.results.get_time(i_step, i_ptor))
                self.scatter(self.results.get_xmins(i_step, i_ptor), xlabel='Minimum longitude [°]', title=title)
                self.scatter(self.results.get_xmaxs(i_step, i_ptor), xlabel='Maximum longitude [°]', title=title)
                self.scatter(self.results.get_ymins(i_step, i_ptor), xlabel='Minimum latitude [°]', title=title)
                self.scatter(self.results.get_ymaxs(i_step, i_ptor), xlabel='Maximum latitude [°]', title=title)

    def scatter(self, values, xlabel, title):
        self.fig = plt.figure(figsize=(5, 4))
        score = self.results.get_calib_scores()
        plt.scatter(values, score, c='', edgecolors=(0.2, 0.2, 0.2, 0.7), linewidths=0.5, s=30)
        xmargin = 0.02 * (values.max() - values.min())
        if xmargin == 0:
            xmargin = 0.1
        plt.xlim(values.min() - xmargin, values.max() + xmargin)
        plt.ylim(0.6 * score.max(), 1.1 * score.max())
        plt.xlabel(xlabel)
        plt.ylabel(self.score)
        plt.title(title)
        self.fig.tight_layout()
        self.print_or_show(title, xlabel)

    def print_or_show(self, title, xlabel):
        if self.do_print:
            filename = title + '_' + xlabel
            filename = filename.lower()
            filename = filename.replace('-', '')
            filename = filename.replace(' [°]', '')
            filename = filename.replace('  ', ' ')
            filename = filename.replace(' ', '_')
            filename = filename.replace('/', '_')
            filename = filename.replace('minimum', 'min')
            filename = filename.replace('maximum', 'max')
            filename = filename.replace('longitude', 'lon')
            filename = filename.replace('latitude', 'lat')
            filename = filename.replace('number_of', 'nb')
            self.fig.savefig(os.path.join(self.output_path, filename + '.pdf'))
            self.fig.savefig(os.path.join(self.output_path, filename + '.png'), dpi=300)
            plt.close(self.fig)
        else:
            plt.show()
