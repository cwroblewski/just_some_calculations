from Kopalnie.params import houses, average_consumption_per_day, cost_per_unit, days_in_year


def get_year_cost_for_uk(houses, average_consumption_per_day, cost_per_unit, days_in_year):
    result = average_consumption_per_day * cost_per_unit * houses * days_in_year
    return result

print(get_year_cost_for_uk(houses, average_consumption_per_day, cost_per_unit, days_in_year))