import math


class Polynomial:
    def __init__(self, pol_arr_1=[], pol_arr_2=[]):
        self.pol_1 = self.convert_arr_into_pol(pol_arr_1)
        self.pol_2 = self.convert_arr_into_pol(pol_arr_2)

    def convert_arr_into_pol(self, arr):
        pol = {}
        exponent = len(arr) - 1
        for ele in arr:
            pol[exponent] = ele
            exponent -= 1
        print(pol)
        return pol

    def polinomial_multiply(self):
        mult_pol = {}
        for exp_1 in self.pol_1:
            for exp_2 in self.pol_2:
                exp_res = exp_1 + exp_2
                if exp_res not in mult_pol:
                    mult_pol[exp_res] = 0
                mult_pol[exp_res] += self.pol_1[exp_1] * self.pol_2[exp_2]
        return list(mult_pol.values())
