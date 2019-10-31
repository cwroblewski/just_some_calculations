from Kopalnie.params import list_of_objects


def get_whole_year_energy_production(list_of_objects):
    result = 0
    for x in list_of_objects:
        result += x.get_year_energy_production()
    return result

print(get_whole_year_energy_production(list_of_objects))
