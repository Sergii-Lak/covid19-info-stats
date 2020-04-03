from datetime import datetime, timedelta
import pandas as pd
from aditional_f import *

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


    def info_country(self, country):
        dispo_country_list = list_countries_dispo(self.confirmed_global)
        no_dispo_country_list = list_boat_counrties_NO_dispo_population_info(self.countries_population, self.confirmed_global)

        if country in no_dispo_country_list:
            confirmed_final = info_confirmed(self.confirmed_global, self.confirmed, country)
            death_final = info_confirmed(self.deaths_global, self.death, country)
            recovered_final = info_confirmed(self.recovered_global, self.recovered, country)

            print()
            print('--------------------COVID-19 statistic----------------------')
            print()
            print('Contry: {} / Last update: {}'.format(country, self.date_now))
            print()
            print('TOTAL population in {} no informations or this is cruise ship'.format(country))
            print('Recovered: {}'.format(recovered_final))
            print('Confirmed: {}'.format(confirmed_final))
            print('Death: {}'.format(death_final))
            print('Existing: {}'.format((confirmed_final - (recovered_final + death_final))))

        elif country in dispo_country_list:
            pop = (counry_pop_search(country, self.countries_population))

            confirmed_final = info_confirmed(self.confirmed_global, self.confirmed, country)
            death_final = info_confirmed(self.deaths_global, self.death, country)
            recovered_final = info_confirmed(self.recovered_global, self.recovered, country)

            print()
            print('--------------------COVID-19 statistic----------------------')
            print()
            print('Contry: {} / Last update: {}'.format(country, self.date_now))
            print()
            print('TOTAL population in {}: {}'.format(country, pop))
            print('Recovered: {}'.format(recovered_final))
            print('Confirmed: {}'.format(confirmed_final))
            print('Death: {}'.format(death_final))
            print('Existing: {}'.format((confirmed_final - (recovered_final + death_final))))
            print('Percentage infected and confirmed of total population: {}%'.format(
                percent_infected_in_counrie(confirmed_final, pop)))
            print('Percentage of deaths among infected people: {}%'.format(('%g' % (float(
                percent_infected_in_counrie(death_final,
                                            confirmed_final))))))  # rounding -  '%g'%(number) - removes all zeros after decimal point
            print('Percentage of recovered among infected people: {}%'.format(
                ('%g' % (float(percent_infected_in_counrie(recovered_final, confirmed_final))))))
            print('Percentage of existing among infected people: {}%'.format(('%g' % (
                float(percent_infected_in_counrie((confirmed_final - (recovered_final + death_final)),
                                                  confirmed_final))))))
        else:
            print('There is no such country, or you made a syntax error!!!!')

        # -----------------------------------------

if __name__ == "__main__":
    covid19 = Global_info()
