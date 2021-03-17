"""
:param
    input: int or float
    if_binary: bool
    int_type: bool
"""
class ten2second():

    def __init__(self, input, if_binary = True, int_type = True):
        self.input = str(input)
        self.if_binary = if_binary
        self.length = len(str(input))
        self.int_type = int_type

    def method(self):

        if self.if_binary:
            decimal = 0
            for i in range(self.length):
                decimal += int(self.input[i]) * (2 ** (self.length - i -1))

            return decimal

        else:
            binary = self.method_reverseint()

            return binary


    def method_reverseint(self):

        if self.int_type:

            input = int(self.input)
            binary = ''

            while input > 0:
                Quotient = input//2
                Mod = input%2
                input = Quotient
                binary += str(Mod)
            binary = binary[::-1]

            return int(binary)

        else:

            input = self.input.split('.')
            num_1, num_2 = int(input[0]), int(str('0.') + input[1])
            binary_1, binary_2  = '', ''

            while num_1 > 0:
                Quotient = num_1 // 2
                Mod = num_1 % 2
                num_1 = Quotient
                binary_1 += str(Mod)

            while num_2 > 0:
                product = num_2 * 2
                Quotient = product // 1
                Mod = product % 1
                num_2 = Mod
                binary_2 += str(Quotient)

            binary = int(
                binary_1[::-1] + '.' + binary_2
            )

            return binary




























