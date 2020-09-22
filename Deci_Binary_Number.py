"""
A deci-binary number is a number that has 0 or 1 as its digits. Ex: 10, 101, 111 are deci-binary numbers.
In order to convert a non-decibinary number to a decibinary number, we will replace each digit that is not a 0 or 1 by 1
Ex: 5201 is replaced as 1101 (5 and 2 is replaced by 1)
We store this number and then subtract is from 5201 and continue the process until number is 0 or below

This program tell how many min number of decibinary are needed to get the actual number, along with the decibinary nos.
https://www.geeksforgeeks.org/represent-number-sum-minimum-possible-psuedobinary-numbers/
"""
class DeciBinary():
    number_list = []

    def __init__(self, num):
        self.num = num

    def get_decibinary(self):
        while self.num > 0:
            temp = self.num
            new_num = 0
            x = 1

            #     print("temp = {}, new_num = {}, x = {} ".format(temp, new_num, x))
            while temp:
                #         print("inside 2nd while")
                #         print("temp = ", temp)
                last_digit = temp % 10
                #         print("last_digit = ", last_digit)
                temp = int(temp / 10)
                #         print("temp = ", temp)
                if last_digit != 0:
                    new_num = new_num + x
                x = x * 10
            #         print("x = ", x)
            #         print("new_num = ", new_num)

            #     print("outside inner while")
            #     print("new_num = ", new_num)
            self.number_list.append(str(new_num))
            self.num = self.num - new_num
        #     print("n =", n)

        print(len(self.number_list))
        print(" ".join(self.number_list))


if __name__ == '__main__':
    n = 5201
    decibinary_obj = DeciBinary(n)
    decibinary_obj.get_decibinary()
