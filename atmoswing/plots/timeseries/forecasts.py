# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib.font_manager as fontmanager
import numpy as np


class TimeSeriesForecast(object):
    """Base class to create a time serie of forecast"""

    def __init__(self, output_path=''):
        self.fig = None
        self.ax = None
        self.output_path = output_path
        self.dates = None
        self.obs_values = None
        self.analogs_values = None
        self.start = 0
        self.end = 0
        self.ref_periods = []
        self.ref_precip = []
        self.__do_print = False
        self.__show_legend = True
        self.__show_dots = False

    def show(self):
        plt.ion()
        self.__make_figure()

    def print(self):
        if not self.output_path:
            raise Exception('Output path not provided')
        self.__do_print = True
        plt.ioff()
        self.__make_figure()

    def __make_figure(self):
        self.fig = plt.figure(figsize=(18, 4.5))
        self.ax = self.fig.add_subplot(111)
        self.build()

    def limit_period(self, start, end):
        # Using datetime: ex: datetime.date(1987, 7, 4)
        self.start = start
        self.end = end

    def set_reference_levels(self, ref_periods, ref_precip):
        self.ref_periods = ref_periods
        self.ref_precip = ref_precip

    def hide_legend(self):
        self.__show_legend = False

    def show_all_dots(self):
        self.__show_dots = True

    def set_data(self, dates, obs_values, analogs_values):
        self.dates = dates
        self.obs_values = obs_values
        self.analogs_values = analogs_values

    def build(self):
        # Split data if we focus on a period
        if self.start and self.end:
            start_array = np.searchsorted(self.dates, self.start.toordinal() - 678575 - 1)
            end_array = np.searchsorted(self.dates, self.end.toordinal() - 678575)
            self.analogs_values = self.analogs_values[start_array:end_array, :]
            self.dates = self.dates[start_array:end_array]
            self.obs_values = self.obs_values[start_array:end_array]

        # Convert time for plotting
        plotdates = self.dates + 678575 + 1

        # Plot the reference values
        self.ax.plot(plotdates, self.obs_values, '-', linewidth=2, color='b', label="observations")

        # Extract quantiles
        q000 = np.mean(np.percentile(self.analogs_values, 0, axis=2), axis=0)
        q030 = np.mean(np.percentile(self.analogs_values, 30, axis=2), axis=0)
        q060 = np.mean(np.percentile(self.analogs_values, 60, axis=2), axis=0)
        q090 = np.mean(np.percentile(self.analogs_values, 90, axis=2), axis=0)
        q100 = np.mean(np.percentile(self.analogs_values, 100, axis=2), axis=0)

        # Plot areas and lines
        self.ax.fill_between(plotdates, q030, q060, facecolor=[0.6, 0.6, 0.6], edgecolor='None')
        self.ax.fill_between(plotdates, q060, q090, facecolor=[0.6, 0.6, 0.6], edgecolor='None')
        self.ax.plot(plotdates, q030, ':', linewidth=1, color='k', label="quantile 30\%")
        self.ax.plot(plotdates, q060, '-', linewidth=1, color='k', label="quantile 60\%")
        self.ax.plot(plotdates, q090, '--', linewidth=1, color='k', label="quantile 90\%")
        self.ax.plot(plotdates, q100, 'x', markersize=3, color='0.5', label="maximum")

        # Plot the dots
        if self.__show_dots:
            for i in range(self.analogs_values.shape[0]):
                self.ax.plot(plotdates, self.analogs_values[:, i], 'ko')

        # Format the ticks
        if self.start and self.end:
            days = mdates.DayLocator()
            some_days = mdates.DayLocator(interval=5)
            days_fmt = mdates.DateFormatter('%d.%m.%Y')
            self.ax.xaxis.set_major_locator(some_days)
            self.ax.xaxis.set_minor_locator(days)
            self.ax.xaxis.set_major_formatter(days_fmt)
        else:
            self.ax.xaxis.set_major_locator(mdates.MonthLocator())
            self.ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonthday=15))
            self.ax.xaxis.set_major_formatter(ticker.NullFormatter())
            self.ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))

            for tick in self.ax.xaxis.get_minor_ticks():
                tick.tick1line.set_markersize(0)
                tick.tick2line.set_markersize(0)
                tick.label1.set_horizontalalignment('center')

            imid = len(plotdates) // 2
            date = plotdates[imid]
            if np.isnan(date):
                date = plotdates[0]
            if np.isnan(date):
                date = plotdates[-1]
            y = mdates.num2date(date).year
            self.ax.set_xlabel(str(y))

        # Draw grid and set axis label
        self.ax.grid(True)
        plt.ylabel('Precipitation (mm/d)')

        # Draw line return periods P10
        if not self.ref_periods and not self.ref_precip:
            p10_index = np.searchsorted(self.ref_periods, 10)
            plt.axhline(y=self.ref_precip[p10_index], linewidth=2, color='r', label="return period of 10 years")

        # Set correct limits
        plt.ylim(ymin=0)

        if self.start and self.end:
            self.ax.set_xlim(self.start, self.end)
        else:
            plt.xlim(plotdates[0], plotdates[-1])

        # Legends
        if self.__show_legend:
            handles, labels = self.ax.get_legend_handles_labels()
            self.ax.legend(handles, labels, loc='upper left', prop=fontmanager.FontProperties(size="smaller"))
