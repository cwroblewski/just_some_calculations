from Kopalnie.params import f, houses, average_consumption_per_day, cost_per_unit, days_in_year, list_of_objects

class CoalMining():

    def __init__(self, name, mining_by_year, energy_per_unit, other_deposits):
        self.name = name
        self.mining_by_year = mining_by_year*1000000
        self.energy_per_unit = energy_per_unit
        self.other_deposits = other_deposits*1000000000

    def get_mount_of_energy(self):
        result = self.other_deposits * self.energy_per_unit
        return result

    def get_years_to_end(self):
        result = self.other_deposits/self.mining_by_year
        return result

    def get_year_energy_production(self):
        result = self.mining_by_year*self.energy_per_unit
        return result


def most_nutritive_coal_min(list_of_objects):
    result = sorted(list_of_objects, key=lambda x: x.get_mount_of_energy(), reverse=True)[0]
    return {'name': result.name, 'energy': result.get_mount_of_energy()}

def get_year_cost_for_uk(houses, average_consumption_per_day, cost_per_unit, days_in_year):
    result = average_consumption_per_day * cost_per_unit * houses * days_in_year
    return result

def get_whole_year_energy_production(list_of_objects):
    result = 0
    for x in list_of_objects:
        result += x.get_year_energy_production()
    return result


print('Exc 1: ', most_nutritive_coal_min(list_of_objects))

print('Exc 2: ', f.get_years_to_end())

print('Exc 3: ', get_year_cost_for_uk(houses, average_consumption_per_day, cost_per_unit, days_in_year))

print('Exc 4: ', get_whole_year_energy_production(list_of_objects))





