from Ubrania.params import biurowy, handlowy, zarzad, dostawczy, magazynowy


def exc_3(a, b, c, d, e):
    list = [a, b, c, d, e]
    return sorted(list, key=lambda x: x.all_costs)[0].name

print(exc_3(biurowy, handlowy, zarzad, dostawczy, magazynowy))