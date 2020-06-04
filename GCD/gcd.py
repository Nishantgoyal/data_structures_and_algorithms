class GCD:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.gcd = self.calculate_GCD()

    def calculate_GCD(self, num_1=None, num_2=None):
        if num_1 is None:
            num_1 = self.num_1
        if num_2 is None:
            num_2 = self.num_2
        if num_1 > num_2:
            num_1, num_2 = num_2, num_1
        # num_1 <= num_2, is established
        rem = num_2 % num_1
        if rem == 0:
            return num_1
        return self.calculate_GCD(rem, num_1)
