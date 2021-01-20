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
        self.marker_size_on_weight = False
        self.filter_min_weight = 0.05
        self.variables_importance_nb = 30
        self.marker_alpha = 1
        self.struct = []
        self.data = []
        self.vars = []
        self.vars_default = ['Z200', 'Z500', 'Z600', 'Z700', 'Z800', 'Z850', 'Z900', 'Z950', 'Z1000', 'ZA1000', 'PV/Z',
                             'U200', 'U300', 'U400', 'U500', 'U600', 'U700', 'U800', 'U1000', 'U10m', 'PT/U285',
                             'PT/U300', 'PT/U315', 'PT/U330', 'PT/U350', 'PT/U370', 'PT/U395', 'PV/U', 'V400', 'V500',
                             'V600', 'V700', 'V800', 'V900', 'V950', 'V1000', 'V10m', 'PT/V285', 'PT/V315', 'PT/V330',
                             'PT/V350', 'PT/V370', 'PT/V395', 'PV/V', 'PT/PRES285', 'PV/PRES', 'SLP', 'W200', 'W300',
                             'W400', 'W500', 'W600', 'W700', 'W800', 'W850', 'W900', 'W950', 'W1000', 'D300', 'D400',
                             'D800', 'D850', 'D900', 'D950', 'D1000', 'D2m', 'PT/D285', 'PT/D315', 'PT/D330', 'PT/D350',
                             'PT/D370', 'VO300', 'VO500', 'VO600', 'VO700', 'VO900', 'PV300', 'PV400', 'PV600', 'PV700',
                             'PV850', 'PV900', 'PV950', 'PT/PV285', 'PT/PV330', 'PT/PV350', 'PT/PV370', 'PT/PV395',
                             'PT/MONT285', 'PT/MONT300', 'PT/MONT330', 'PT/MONT350', 'PT/MONT370', 'RH500', 'RH600',
                             'RH700', 'RH800', 'RH850', 'RH900', 'RH950', 'RH1000', 'SH500', 'SH600', 'SH700',
                             'PT/SH315', 'PT/SH330', 'PT/SH350', 'PT/SH370', 'PT/SH395', 'TCW', 'CWAT', 'IE', 'T400',
                             'T600', 'T800', 'T850', 'T900', 'T950', 'T2m', 'PV/PT', 'SSR', 'SSRD', 'STR', 'STRD',
                             'CAPE', 'SD']
        self.use_vars_default = True
        self.stations = []
        self.crit = ['RMSE', 'S0', 'S1', 'S2', 'MD', 'DSD', 'DMV']
        self.colors = plt.get_cmap('tab10').colors
        self.markers = ['o', 'v', 's', 'P', '^', '<', '>', '8', 'p', '*', 'h', 'H', 'D', 'd', 'X']
        self.files = glob.glob(base_dir + '/**/*best_individual.txt', recursive=True)

    def show_scatter(self):
        plt.ion()
        self.__set_criteria_color()
        self.__set_marker_size()
        self.__make_scatter_plot()
        plt.show()

    def print_scatter(self, filename):
        if not self.output_path:
            raise Exception('Output path not provided')
        plt.ioff()
        self.__set_criteria_color()
        self.__set_marker_size()
        self.__make_scatter_plot()
        self.__print(filename)

    def print_variables_importance(self, filename):
        if not self.output_path:
            raise Exception('Output path not provided')
        plt.ioff()
        self.__make_variables_importance_plot()
        self.__print(filename)

    def load(self):
        self.__parse_results()
        self.__list_stations()
        self.__drop_bad_scores()
        self.__list_variables()
        self.__add_variable_index()

    def __parse_results(self):
        data = []
        resCheck = params.ParamsArray(self.files[0])
        resCheck.load()
        self.struct = resCheck.struct
        labels_slct = []

        # Create labels
        for step, ptors in enumerate(self.struct):
            for ptor in range(ptors):
                labels_slct.append('var_{}_{}'.format(step, ptor))
                labels_slct.append('criterion_{}_{}'.format(step, ptor))
                labels_slct.append('weight_{}_{}'.format(step, ptor))

        # Extract values
        for filename in self.files:
            results = params.ParamsArray(filename)
            results.load()
            data_slct = []
            for step, ptors in enumerate(self.struct):
                for ptor in range(ptors):
                    if ptor >= results.struct[step]:
                        continue
                    data_slct.append(results.get_variable_and_level(step, ptor))
                    data_slct.append(results.get_criterion(step, ptor))
                    data_slct.append(results.get_weight(step, ptor))

            vals = [int(results.get_station()), results.get_valid_score(), filename] + data_slct
            data.append(vals)

        labels = ['station', 'score', 'file'] + labels_slct
        self.data = pd.DataFrame(data, columns=labels)
        self.data.sort_values(by=['station', 'file'], inplace=True)

    def __list_variables(self):
        for step, ptors in enumerate(self.struct):
            for ptor in range(ptors):
                variables = self.data['var_{}_{}'.format(step, ptor)]
                if self.filter_min_weight > 0:
                    weight = self.data['weight_{}_{}'.format(step, ptor)]
                    variables = variables[weight >= self.filter_min_weight]
                if len(self.vars) == 0:
                    self.vars = variables
                else:
                    self.vars = self.vars.append(variables)

        self.vars = self.vars.drop_duplicates()
        self.vars = self.vars.sort_values(ascending=False)
        if self.use_vars_default:
            old_vars = list(self.vars)
            new_vars = []
            for var in self.vars_default:
                if var in old_vars:
                    new_vars.append(var)
                    old_vars.remove(var)
            if len(old_vars) > 0:
                new_vars += old_vars
            new_vars.reverse()
            self.vars = pd.Series(new_vars)
        self.vars = self.vars.reset_index(drop=True)

    def __list_stations(self):
        self.stations = self.data['station']
        self.stations = self.stations.drop_duplicates()
        self.stations = self.stations.sort_values(ascending=False)
        self.stations = self.stations.reset_index(drop=True)

    def __add_variable_index(self):
        for step, ptors in enumerate(self.struct):
            for ptor in range(ptors):
                label = 'var_index_{}_{}'.format(step, ptor)
                self.data[label] = None
                for idx, var in enumerate(self.vars):
                    self.data.loc[self.data['var_{}_{}'.format(step, ptor)] == self.vars[idx], label] = idx

    def __set_criteria_color(self):
        for step, ptors in enumerate(self.struct):
            for ptor in range(ptors):
                label = 'crit_color_{}_{}'.format(step, ptor)
                self.data[label] = None
                for icrit, crit in enumerate(self.crit):
                    indexes = self.data.loc[self.data['criterion_{}_{}'.format(step, ptor)] == crit].index
                    for index in indexes:
                        self.data[label].iloc[index] = self.colors[icrit]

    def __drop_bad_scores(self):
        for station in self.stations:
            indexes = self.data.loc[self.data['station'] == station].index
            scores = self.data['score'].loc[indexes]
            min_score = min(scores)
            sizes = self.marker_size_max * ((min_score * (1 + self.marker_size_range)) - scores) / \
                    (min_score * self.marker_size_range)
            drop_rows = indexes[sizes < 1]
            self.data.drop(index=drop_rows, inplace=True)
            self.data.reset_index(drop=True, inplace=True)

    def __set_marker_size(self):
        if self.marker_size_on_weight:
            max_weight = 0.2
            min_weight = 0.02
            for step, ptors in enumerate(self.struct):
                for ptor in range(ptors):
                    label = 'marker_size_{}_{}'.format(step, ptor)
                    self.data[label] = None
                    sizes = []
                    for weight in self.data['weight_{}_{}'.format(step, ptor)]:
                        size = self.marker_size_max * (weight - min_weight) / (max_weight - min_weight)
                        if size < 1:
                            size = 1
                        if size > self.marker_size_max:
                            size = self.marker_size_max
                        sizes.append(size)
                    self.data[label] = sizes
        else:
            self.data['marker_size'] = 0
            for station in self.stations:
                indexes = self.data.loc[self.data['station'] == station].index
                scores = self.data['score'].loc[indexes]
                min_score = min(scores)
                sizes = self.marker_size_max * ((min_score * (1 + self.marker_size_range)) - scores) / \
                        (min_score * self.marker_size_range)
                sizes[sizes < 1] = 1
                self.data.loc[indexes, 'marker_size'] = sizes

    def __make_scatter_plot(self):
        fig_height = 0.66 + float(len(self.vars)) * 3.7/25.0
        self.fig = plt.figure(figsize=(10, fig_height))
        plt.grid(axis='y', alpha=0.2)
        plt.xlim(0, len(self.data) + 1)
        plt.ylim(-1, len(self.vars))

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

        for step, ptors in enumerate(self.struct):
            marker = self.markers[step]
            for ptor in range(ptors):
                x = np.arange(1, len(self.data) + 1)
                variables = self.data['var_index_{}_{}'.format(step, ptor)]
                facecolors = self.data['crit_color_{}_{}'.format(step, ptor)]
                edgecolors = self.data['crit_color_{}_{}'.format(step, ptor)]
                if self.marker_size_on_weight:
                    sizes = self.data['marker_size_{}_{}'.format(step, ptor)]
                    facecolors='none'
                else:
                    sizes = self.data['marker_size']

                nodata = variables.isnull()
                if nodata.any():
                    indices = variables[nodata].index.tolist()
                    variables = variables.drop(indices)
                    edgecolors = edgecolors.drop(indices)
                    sizes = sizes.drop(indices)
                    x = np.delete(x, indices)

                plt.scatter(x, variables, marker=marker, facecolors=facecolors, edgecolors=edgecolors, s=sizes,
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

    def __make_variables_importance_plot(self):
        fig_height = 0.66 + self.variables_importance_nb * 3.7/25.0
        self.fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, fig_height))
        ax2.grid(axis='y', alpha=0.2)
        ax1.set_ylim(0, self.variables_importance_nb + 1)
        ax2.set_ylim(0, self.variables_importance_nb + 1)

        vars_weights = [[] for i in range(len(self.vars))]

        for step, ptors in enumerate(self.struct):
            for ptor in range(ptors):
                variables = self.data['var_index_{}_{}'.format(step, ptor)]
                weights = self.data['weight_{}_{}'.format(step, ptor)]

                nodata = variables.isnull()
                if nodata.any():
                    indices = variables[nodata].index.tolist()
                    variables = variables.drop(indices)
                    weights = weights.drop(indices)

                for i in range(len(variables)):
                    vars_weights[variables.iloc[i]].append(weights.iloc[i])

        sums = []
        counts = []
        for weights in vars_weights:
            sums.append(np.sum(weights))
            counts.append(len(weights))

        counts, sums, vars_weights, vars = (list(t) for t in zip(*sorted(zip(counts, sums, vars_weights, self.vars.tolist()), reverse=True)))

        y = range(1, self.variables_importance_nb + 1)

        ax1.barh(y, counts[0:self.variables_importance_nb])
        ax2.boxplot(vars_weights[0:self.variables_importance_nb], vert=False)

        y_ticks = vars[0:self.variables_importance_nb]
        ax1.set_yticks(y)
        ax1.set_yticklabels(y_ticks)
        ax1.invert_yaxis()
        ax2.set_yticks(y)
        ax2.set_yticklabels(y_ticks)
        ax2.invert_yaxis()

        ax1.set_xlabel('Number of selections')
        ax2.set_xlabel('Weights')

        self.fig.tight_layout()

    def __print(self, filename):
        self.fig.savefig(os.path.join(self.output_path, filename + '.pdf'))
        self.fig.savefig(os.path.join(self.output_path, filename + '.png'), dpi=300)
        plt.close(self.fig)
