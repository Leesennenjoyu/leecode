class TransFormation:

    def __init__(self):
        pass

    def binary2Decimal(self, input):

        input = str(input)
        if '.' in input:
            input = input.split('.')
            input_1, input_2 = input[0], input[1]
            output_1, output_2 = 0, 0

            for i in range(len(input_1)):
                output_1 += int(input_1[i]) * 2 ** (len(input_1) - 1 - i)

            for i in range(len(input_2)):
                output_2 += int(input_2[i]) * 2 ** (-i - 1)

            output = float(output_1) + float(output_2)

            return output
        else:
            output = 0
            for i in range(len(input)):
                output += int(input[i]) * 2 ** (len(input) - 1 - i)

            return int(output)

    def Decima2binary(self, input):

        if isinstance(input, float):
            input_1 = int(input // 1)
            input_2 = input % 1
            output_1, output_2 = '', ''

            if input_1 == 0:
                output_1 = 0

            while input_1 > 0 :
                __ = input_1 // 2
                mod = input_1 % 2
                input_1 = __
                output_1 += str(mod)

            while input_2 > 0:
                __ = (input_2 * 2) % 1
                mod = int((input_2 * 2) // 1)
                input_2 = __
                output_2 += str(mod)

            output = float(
                str(output_1)[::-1] + '.' + output_2
            )

        if isinstance(input, int):

             output = ''
             while input > 0:
                 input = input // 2
                 mod = input % 2
                 output += str(mod)

             output = int(output)

        return output






if __name__ == '__main__':

    output_1 = TransFormation().binary2Decimal(input=1101.01)
    print(output_1)

    output_2 = TransFormation().Decima2binary(input = 255)
    print(output_2)

    output_3 = TransFormation().Decima2binary(input = 0.625)
    print(output_3)
