# -*- coding: utf-8 -*-

import os
import glob
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
from atmoswing.files.parse.optimizer import params


class PlotsGAsVariables(object):
    """Plotting the results of the Monte Carlo analysis"""

    def __init__(self, base_dir, output_path=''):
        self.fig = None
        self.base_dir = base_dir
        self.output_path = output_path
        self.marker_size_max = 50
        self.marker_size_range = 0.05
        self.marker_alpha = 1
        self.data = []
        self.vars = []
        self.stations = []
        self.crit = ['RMSE', 'S0', 'S1', 'S2', 'MD', 'DSD', 'DMV']
        self.colors = plt.get_cmap('tab10').colors
        self.files = glob.glob(base_dir + '/**/*best_individual.txt', recursive=True)

    def show(self):
        plt.ion()
        self.__parse_results()
        self.__list_stations()
        self.__list_variables()
        self.__add_variable_index()
        self.__set_criteria_color()
        self.__set_marker_size()
        self.__make_plot()
        plt.show()

    def print(self, filename):
        if not self.output_path:
            raise Exception('Output path not provided')
        self.__do_print = True
        plt.ioff()
        self.__parse_results()
        self.__list_stations()
        self.__list_variables()
        self.__add_variable_index()
        self.__set_criteria_color()
        self.__set_marker_size()
        self.__make_plot()
        self.__print(filename)

    def __parse_results(self):
        data = []
        for filename in self.files:
            results = params.ParamsArray(filename)
            results.load()
            data.append([int(results.get_station()),
                         results.get_variable_and_level(0, 0),
                         results.get_criterion(0, 0),
                         results.get_valid_score()])
        labels = ['station', 'var', 'criterion', 'score']
        self.data = pd.DataFrame(data, columns=labels)

    def __list_variables(self):
        self.vars = self.data['var']
        self.vars.drop_duplicates(inplace=True)
        self.vars = self.vars.sort_values(ascending=False)
        self.vars.reset_index(drop=True, inplace=True)

    def __list_stations(self):
        self.stations = self.data['station']
        self.stations.drop_duplicates(inplace=True)
        self.stations = self.stations.sort_values(ascending=False)
        self.stations.reset_index(drop=True, inplace=True)

    def __add_variable_index(self):
        self.data['var_index'] = -1
        for idx, var in enumerate(self.vars):
            self.data.loc[self.data['var'] == self.vars[idx], 'var_index'] = idx

    def __set_criteria_color(self):
        self.data['crit_color'] = None
        for icrit, crit in enumerate(self.crit):
            indexes = self.data.loc[self.data['criterion'] == crit].index
            for index in indexes:
                self.data['crit_color'].iloc[index] = self.colors[icrit]

    def __set_marker_size(self):
        self.data['marker_size'] = 0
        for station in self.stations:
            indexes = self.data.loc[self.data['station'] == station].index
            scores = self.data['score'].loc[indexes]
            min_score = min(scores)
            sizes = self.marker_size_max * ((min_score * (1 + self.marker_size_range)) - scores) / \
                    (min_score * self.marker_size_range)
            sizes[sizes < 1] = 1
            self.data.loc[indexes, 'marker_size'] = sizes

    def __make_plot(self):
        self.fig = plt.figure(figsize=(10, 4))
        x = np.arange(1, len(self.data) + 1)
        plt.grid(axis='y', alpha=0.2)
        plt.xlim(0, len(self.data) + 1)

        do_paint = False
        xticks = []
        for station in self.stations:
            indexes = self.data.loc[self.data['station'] == station].index
            index_min = min(indexes) + 1
            index_max = max(indexes) + 1
            xticks.append((index_min + index_max) / 2.0)
            if do_paint:
                plt.axvspan(index_min - 0.5, index_max + 0.5, facecolor='k', alpha=0.08)
            do_paint = not do_paint

        plt.scatter(x, self.data['var_index'], c=self.data['crit_color'], s=self.data['marker_size'],
                    alpha=self.marker_alpha, zorder=10)
        plt.xticks(xticks, self.stations)
        plt.yticks(self.vars.index.tolist(), self.vars)
        plt.tick_params(axis='both', which='both', bottom=False, top=False,
                        labelbottom=True, left=False, right=False, labelleft=True)

        patches = []
        for idx, criteria in enumerate(self.crit):
            patches.append(mpatches.Patch(color=self.colors[idx], label=criteria, alpha=self.marker_alpha))
        plt.legend(handles=patches, title="Criteria", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), frameon=False)

        self.fig.tight_layout()

    def __print(self, filename):
        self.fig.savefig(os.path.join(self.output_path, filename + '.pdf'))
        self.fig.savefig(os.path.join(self.output_path, filename + '.png'), dpi=300)
        plt.close(self.fig)
