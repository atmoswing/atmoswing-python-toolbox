#!/usr/bin/python

# Imports
from atmoswing.plots.timeseries import forecasts
from atmoswing.external import jdcal
from atmoswing.parser.obs import idaweb
from atmoswing.parser.forecaster import forecast
import numpy as np
import math

# Parameters
stations = np.array([21, 24, 27, 39, 43, 44, 48, 53, 55])
stations = np.array([24])
time_lapses = [0, 1, 2, 3, 4, 5, 6, 7]  # 0 for day d, 1 for the forecast 1 day before, etc
start = [2016, 1]
end = [2018, 12]
nb_months = 6
methods = ['PC-AZ2', 'PC-AZ2-AHI2', 'PC-AZ4o', 'PC-AZ4o-AHI2o']
use_initial_analogs_nb = False

directory_fcts = 'D:\\Projects\\ANALOGS\\Analyses\\Forecasts performance\\Forecasts\\Suisse - VS\\v 1.2-1.3\\'
directory_obs = u'D:\\Projects\\ANALOGS\\Analyses\\Forecasts performance\\Observations\\'
output_path = 'D:\\Projects\\ANALOGS\\Analyses\\Forecasts performance\\Plots\\'

# Build dates vector
vect_period = []
for y in np.arange(start[0], end[0]+1):
    for m in np.arange(1, 13, nb_months):
        if y == start[0] and m < start[1]:
            continue
        if y == end[0] and m+nb_months-1 > end[1]:
            break
        vect_period.append([y, m])

for time_lapse in time_lapses:
    for method in methods:

        if time_lapse > 5 and 'HI' in method:
            continue

        for i_stat in np.arange(len(stations)):
            station_id = stations[i_stat]

            if method == 'PC-AZ2':
                if station_id in [24, 26, 61, 60, 59, 58]:
                    region = 'Cretes sud-est'
                elif station_id in [1, 2, 3, 4, 5, 6, 7, 22, 23]:
                    region = 'Vallee de Conches'
                else:
                    region = 'Partie principale'

            elif method == 'PC-AZ2-AHI2':
                if station_id in [24, 26, 61, 60, 59, 58]:
                    region = 'Cretes du sud-est'
                elif station_id in [21, 49, 50, 51, 52, 53, 54, 55, 56, 57]:
                    region = 'Chablais'
                elif station_id in [46, 47, 48]:
                    region = 'Vallee du Trient'
                else:
                    region = 'Partie principale'

            elif method in ['PC-AZ4o', 'PC-AZ4o-AHI2o', 'PC-AZ4po', 'PC-AZ4po-AHF2po']:
                if station_id in [31, 8, 9, 10, 11, 12, 13, 17]:
                    region = 'Alpes_bernoises_est'
                elif station_id in [14, 15, 16, 18, 19, 20, 32, 34]:
                    region = 'Alpes_bernoises_ouest'
                elif station_id in [21, 49, 50, 51, 52, 53, 54, 55, 56, 57]:
                    region = 'Chablais'
                elif station_id in [27, 43, 44]:
                    region = 'Cretes_sud'
                elif station_id in [24, 26, 61, 60, 59, 58]:
                    region = 'Cretes_sud_est'
                elif station_id in [1, 2, 3, 4, 5, 6, 7, 22, 23]:
                    region = 'Vallee_Conches'
                elif station_id in [25, 28, 29, 30]:
                    region = 'Vallee_Rhone_amont'
                elif station_id in [33, 38, 39, 40]:
                    region = 'Vallee_Rhone_aval'
                elif station_id in [46, 47, 48]:
                    region = 'Vallee_Trient'
                elif station_id in [35, 36, 37, 41, 42, 45]:
                    region = 'Vallees_laterales_gauches'

            # Extract observation
            parser = idaweb.Idaweb(directory_obs + str(station_id) + '.txt')
            obs_matrix = parser.parse()
            ymax = np.nanmax(obs_matrix[0:-1, 3]) * 1.2

            for curr_period in vect_period:

                plot_start_y = curr_period[0]
                plot_start_m = curr_period[1]
                plot_start_d = 1

                plot_end_m = plot_start_m + nb_months
                plot_end_y = plot_start_y
                if plot_end_m > 12:
                    plot_end_m -= 12
                    plot_end_y += 1
                plot_end_d = 1

                obs_start = np.where((obs_matrix[:, 0] == plot_start_y) &
                                     (obs_matrix[:, 1] == plot_start_m) &
                                     (obs_matrix[:, 2] == plot_start_d))
                i_obs_start = int(obs_start[0])
                obs_end = np.where((obs_matrix[:, 0] == plot_end_y) &
                                   (obs_matrix[:, 1] == plot_end_m) &
                                   (obs_matrix[:, 2] == plot_end_d))
                if len(obs_end[0]) > 0:
                    i_obs_end = int(obs_end[0])
                else:
                    i_obs_end = -1
                obs = obs_matrix[i_obs_start:i_obs_end, 3]

                date_ref = jdcal.gcal2jd(plot_start_y, plot_start_m, plot_start_d)[0]
                date_start = jdcal.gcal2jd(plot_start_y, plot_start_m, plot_start_d)[1] - time_lapse
                date_end = jdcal.gcal2jd(plot_end_y, plot_end_m, plot_end_d)[1] - time_lapse
                dates = np.arange(date_start, date_end, 1)

                hrs = ['00', '06', '12', '18']
                final_analogs_values = []
                v_target_dates = np.array([])
                nb_analogs = 0
                ref = []

                for i_hr in np.arange(len(hrs)):

                    v_analogs_values = np.array([])

                    counter = 0
                    for date in dates:
                        [year, month, day, rest] = jdcal.jd2gcal(date_ref, date)

                        version = 1.0
                        if year < 2012 or (year == 2012 and month < 11):
                            version = 1.0
                        elif year < 2014:
                            version = 1.01
                        elif (year == 2014 and month < 3) or (year == 2014 and month == 3 and day < 3):
                            version = 1.1
                        elif (method == 'PC-AZ2' or method == 'PC-AZ2-AHI2') and (year == 2014 or (year == 2015 and month < 2)):
                            version = 1.2
                        else:
                            version = 1.3

                        str_y = str(year)
                        str_m = str(month)
                        if len(str_m) < 2:
                            str_m = '0' + str_m
                        str_d = str(day)
                        if len(str_d) < 2:
                            str_d = '0' + str_d
                        str_h = hrs[i_hr]

                        if version == 1.0:
                            if method == 'PC-AZ2':
                                filename = str_y + str_m + str_d + str_h + '.R1 ' + region + ' v1.0.fcst'
                            elif method == 'PC-AZ2-AHI2':
                                filename = str_y + str_m + str_d + str_h + '.R2 ' + region + ' v1.0.fcst'
                            else:
                                filename = str_y + str_m + str_d + str_h + '.' + method + ' ' + region + ' v1.0.fcst'
                        elif version <= 1.2:
                            if method == 'PC-AZ2':
                                filename = str_y + str_m + str_d + str_h + '.R1 ' + region + '.fcst'
                            elif method == 'PC-AZ2-AHI2':
                                filename = str_y + str_m + str_d + str_h + '.R2 ' + region + '.fcst'
                            else:
                                filename = str_y + str_m + str_d + str_h + '.' + method + ' ' + region + '.fcst'
                        else:
                            if method in ['PC-AZ2', 'PC-AZ2-AHI2']:
                                new_region = region
                                if not region == 'Vallee du Trient':
                                    new_region = new_region.replace(' du ', '_')
                                new_region = new_region.replace('-', '_')
                                new_region = new_region.replace(' ', '_')
                                filename = str_y + str_m + str_d + str_h + '.' + method + '.' + new_region + '.asff'
                            else:
                                filename = str_y + str_m + str_d + str_h + '.' + method + '.' + region + '.asff'

                        filepath = directory_fcts + '\\' + str_y + '\\' + str_m + '\\' + str_d + '\\' + filename

                        fc = forecast.Forecast(filepath)
                        if not fc.open():
                            print('Not found: ' + filepath)
                            if v_analogs_values.size > 0:
                                v_analogs_values[counter, :] = np.NaN
                            counter = counter + 1
                            continue

                        if use_initial_analogs_nb:
                            fc.use_analogs_nb_t0()

                        station_name = fc.get_station_name(station_id)
                        analog_values = fc.get_analog_values(station_id, time_lapse)
                        ref = fc.get_reference(station_id)
                        nb_analogs = fc.get_analogs_nb(time_lapse)

                        if v_analogs_values.size == 0:
                            v_analogs_values = np.ones((len(dates), nb_analogs)) * np.NaN
                        if v_target_dates.size == 0:
                            v_target_dates = np.ones((len(dates), 1)) * np.NaN
                        v_analogs_values[counter, :] = analog_values[0, :]

                        if np.isnan(v_target_dates[counter]):
                            v_target_dates[counter] = fc.target_dates[time_lapse]

                        fc.close()
                        counter = counter + 1

                    final_analogs_values.append(v_analogs_values)

                # Figure
                fig = forecasts.TimeSeriesForecast(output_path)

                str_plot_start_y = str(plot_start_y)
                str_plot_start_m = str(plot_start_m)
                str_plot_end_m = str(plot_start_m + nb_months - 1)
                if len(str_plot_start_m) < 2:
                    str_plot_start_m = '0' + str_plot_start_m
                if len(str_plot_end_m) < 2:
                    str_plot_end_m = '0' + str_plot_end_m

                #plotTitle = stationname + ' (' + method + ' ' + groupment + '), ' + str_month_plot + '/' + str_year_plot

                v_target_dates = v_target_dates[:, 0]
                for idx, target_date in enumerate(v_target_dates):
                    if math.isnan(target_date):
                        if idx > 0:
                            v_target_dates[idx] = v_target_dates[idx - 1] + 1
                        else:
                            for idx2, target_date2 in enumerate(v_target_dates):
                                if not math.isnan(target_date2):
                                    v_target_dates[idx] = target_date2 - idx2

                print(station_name + ' ' + str_plot_start_m + '.' + str_plot_start_y)

                str_stname = str(station_name)
                str_stname = str_stname.replace('/', '')
                str_stname = str_stname.replace('  ', ' ')

                methodFilename = method
                methodFilename = methodFilename.replace('PC-', '')
                tag = ''
                if use_initial_analogs_nb:
                    tag = '_anb_cst'
                fig.set_output_name('fcst_' + str_stname + '_' + methodFilename + '_' + str_plot_start_y + '_' + str_plot_start_m + '-' + str_plot_end_m + '_l-' + str(time_lapse) + 'd' + tag)

                fig.set_reference_levels(ref['axis'], ref['values'])
                fig.set_data(v_target_dates, obs, final_analogs_values)
                fig.hide_legend()
                fig.set_max_val(ymax)
                fig.print()


print('Done.')
