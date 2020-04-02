

def checking_max(a):
    return a.shape[0]

def counry_pop_search(country, countries_population):
    res = 0
    for i in range(0, checking_max(countries_population)):
        if countries_population.loc[i][1] == country:
            res = int(str(countries_population.loc[i][2]).replace('.', ''))
            break
    return res

def list_boat_counrties_NO_dispo_population_info(countries_population, confirmed_global):
    countries_people_data = countries_population['name']
    countries_covid = confirmed_global['Country/Region']
    c_data = list(set(countries_people_data))
    c_check = list(set(countries_covid))
    no_dispo_list = []
    for i in c_check:
        if i not in c_data:
            no_dispo_list.append(i)
    return no_dispo_list

def list_countries_dispo(confirmed_global):
    countries_dispo = []
    for i in range(0, checking_max(confirmed_global)):
        countries_dispo.append(confirmed_global.loc[i][1])
    return countries_dispo


def info_confirmed(df_info, result, country):
    for i in range(0, checking_max(df_info)):
        if df_info.loc[i][1] == country:
            result += df_info.loc[i][-1]
    return result

def percent_infected_in_counrie(number_infected_confirmed, population):
    percent_infected = format(((number_infected_confirmed / population) * 100), '.10f') #rounding, 10 numbers after decimal point
    if percent_infected == 0:
        return 0
    else:
        return percent_infected