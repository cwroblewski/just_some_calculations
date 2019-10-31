from Ubrania.ubraniaClass import Prices
from Ubrania.params import o, dostawczy, magazynowy


def exc_4(dostawczy, magazynowy, o):

    a = dostawczy.all_costs + magazynowy.all_costs
    b = Prices(dostawczy.mount_of_personel + magazynowy.mount_of_personel, o, 'łączony').all_costs

    return b - a

print(exc_4(dostawczy, magazynowy, o))