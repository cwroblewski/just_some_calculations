from Ubrania.params import o, biurowy, handlowy, zarzad, dostawczy, magazynowy, a_e2, b_e2, c_e2, d_e2, e_e2
class Prices():

    def __init__(self, mount_of_personel, type, name):
        self.name = name
        self.mount_of_personel = mount_of_personel
        self.type = type
        self.get_prices_and_cost()

    def get_prices_and_cost(self):
        x = self.mount_of_personel
        if x < 1:
            raise Exception('UJEMNA LICZBA')

        if x > 0  and x < 11:
            a = 13.54
            b = 137.65
            c = 7.67
            d = 32.35

        elif x > 10 and x < 26:
            a = 8.64
            b = 112.35
            c = 5.23
            d = 28.64

        elif x > 25 and x < 51:
            a = 8.26
            b = 98.34
            c = 4.25
            d = 23.65
        elif x > 50 and x < 100:
            a = 7.64
            b = 85.64
            c = 4.05
            d = 20.32
        else:
            a = 7.49
            b = 76.15
            c = 3.26
            d = 18.64

        self.shoes = d

        if self.type == 'operacyjny':
            self.trousers = a
            self.shirts = c

            cost_of_clothes = d + a + c

        elif self.type == 'administracyjny':
            self.suits = b

            cost_of_clothes = d + b

        self.all_costs = self.mount_of_personel * cost_of_clothes


exc_1 = Prices(437, o, 'temp')

print('Exc 1: ', exc_1.all_costs)

def exc_2(a_e2, b_e2, c_e2, d_e2, e_e2):

    result = 100 - e_e2/(a_e2/100)
    return result

print('Exc 2: ', exc_2(a_e2, b_e2, c_e2, d_e2, e_e2))

def exc_3(a, b, c, d, e):
    list = [a, b, c, d, e]
    return sorted(list, key=lambda x: x.all_costs)[0].name

print('Exc 3: ', exc_3(biurowy, handlowy, zarzad, dostawczy, magazynowy))


def exc_4(dostawczy, magazynowy):
    o = 'operacyjny'

    a = dostawczy.all_costs + magazynowy.all_costs
    b = Prices(dostawczy.mount_of_personel + magazynowy.mount_of_personel, o, 'łączony').all_costs

    return b - a

print('Exc 4: ', exc_4(dostawczy, magazynowy))