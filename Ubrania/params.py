from Ubrania.ubraniaClass import Prices

o = 'operacyjny'
adm = 'administracyjny'

biurowy = Prices(212, adm, 'biurowy')
handlowy = Prices(64, adm, 'handlowy')
zarzad = Prices(16, adm, 'zarzad')
dostawczy = Prices(33, o, 'dostawczy')
magazynowy = Prices(112, o, 'magazynowy')

list_of_oper = [biurowy, handlowy, zarzad, dostawczy, magazynowy]

'''EXC 2 params'''
a_e2 = 137.65 + 32.35
b_e2 = 112.35 + 28.64
c_e2 = 98.34 + 23.65
d_e2 = 85.64 + 20.32
e_e2 = 76.15 + 18.64