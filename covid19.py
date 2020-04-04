from datetime import datetime, timedelta
import pandas as pd
from aditional_f import *
import numpy as np

np.seterr(divide='ignore', invalid='ignore')  # for ignor this: '--RuntimeWarning: invalid value encountered in longlong_scalars--'

class Global_info():
    # ------------------------------------
    def __init__(self):
        self.countries_population = pd.read_csv('data_population.csv')

        self.confirmed_global = pd.read_csv(
            'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        self.deaths_global = pd.read_csv(
            'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        self.recovered_global = pd.read_csv(
            'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

        self.date_update = datetime.date(datetime.now() - timedelta(days=1))
        self.date_now = datetime.date(datetime.now())

        self.recovered = 0
        self.death = 0
        self.confirmed = 0

    # --------------------------------------------------------------

    def country_infected_list(self):
        dispo_country_list = list(set(list_countries_dispo(self.confirmed_global)))
        return sorted(dispo_country_list)

    def date_valid_list(self):
        return dates_dispo_list(self.confirmed_global)

    def info_country(self, country, date):
        dispo_country_list = list_countries_dispo(self.confirmed_global)
        no_dispo_country_list = list_boat_counrties_NO_dispo_population_info(self.countries_population, self.confirmed_global)
        dates_list = dates_dispo_list(self.confirmed_global)

        if country in no_dispo_country_list and date in dates_list:
            confirmed_final = info_confirmed(self.confirmed_global, self.confirmed, country, date)
            death_final = info_confirmed(self.deaths_global, self.death, country, date)
            recovered_final = info_confirmed(self.recovered_global, self.recovered, country, date)


            print()
            print('--------------------COVID-19 statistic----------------------')
            print()
            print('Contry: {} / In this date: {}'.format(country, date))
            print()
            print('TOTAL population in {} no informations or this is cruise ship'.format(country))
            print('Recovered: {}'.format(recovered_final))
            print('Confirmed: {}'.format(confirmed_final))
            print('Death: {}'.format(death_final))
            print('Existing: {}'.format((confirmed_final - (recovered_final + death_final))))

        elif country in dispo_country_list and date in dates_list:
            pop = (counry_pop_search(country, self.countries_population))

            confirmed_final = info_confirmed(self.confirmed_global, self.confirmed, country, date)
            death_final = info_confirmed(self.deaths_global, self.death, country, date)
            recovered_final = info_confirmed(self.recovered_global, self.recovered, country, date)

            print()
            print('--------------------COVID-19 statistic----------------------')
            print()
            print('Contry: {} / For this date: {}'.format(country, date))
            print()
            print('TOTAL population in {}: {}'.format(country, pop))
            print('Recovered: {}'.format(recovered_final))
            print('Confirmed: {}'.format(confirmed_final))
            print('Death: {}'.format(death_final))
            print('Existing: {}'.format((confirmed_final - (recovered_final + death_final))))
            print('The percentage infected and confirmed of total population: {}%'.format(
                percent_infected_in_counrie(confirmed_final, pop)))
            print('The percentage of deaths among infected people: {}%'.format(('%g' % (float(
                percent_infected_in_counrie(death_final,
                                            confirmed_final))))))  # rounding -  '%g'%(number) - removes all zeros after decimal point
            print('The percentage of recovered among infected people: {}%'.format(
                ('%g' % (float(percent_infected_in_counrie(recovered_final, confirmed_final))))))
            print('The percentage of existing among infected people: {}%'.format(('%g' % (
                float(percent_infected_in_counrie((confirmed_final - (recovered_final + death_final)),
                                                  confirmed_final))))))
        elif country in dispo_country_list or country in no_dispo_country_list and date not in dates_list:
            print('Date not valid!!!')
        elif country not in dispo_country_list or country not in no_dispo_country_list and date in dates_list:
            print('There is no such country!!!')
        else:
            print('You made a syntax error!!!!')

        print(start_date_infection_country(self.confirmed_global, country))

        # -----------------------------------------

if __name__ == "__main__":
    covid19 = Global_info()