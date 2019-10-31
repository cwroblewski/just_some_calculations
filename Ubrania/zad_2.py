from Ubrania.params import a_e2, b_e2, c_e2, d_e2, e_e2
def exc_2(a_e2, b_e2, c_e2, d_e2, e_e2):

    result = 100 - e_e2/(a_e2/100)
    return result

print(exc_2(a_e2, b_e2, c_e2, d_e2, e_e2))