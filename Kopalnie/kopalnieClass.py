

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