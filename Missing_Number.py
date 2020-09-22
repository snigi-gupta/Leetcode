class MissingNumber:

    # O(n)
    def sumOfNumbers(self, arr):
        sum_of_numbers = (len(arr) + 1) * (len(arr) + 2)//2
        print("Sum of n numbers", sum_of_numbers)
        for i in arr:
            sum_of_numbers -= i
        return sum_of_numbers
    def using_xor(self, A):
        x1 = A[0]
        x2 = 1
        for i in range(1, len(A)):
            print("{} XOR {} = {}".format(x1,A[i],x1^A[i]))
            x1 = x1^A[i]
        for i in range(2, len(A)+2):
            print("{} XOR {} = {}".format(x2, i, x2 ^ i))
            x2 = x2^i
        print("x1 and x2:", x1,x2)
        return x1^x2




if __name__ == "__main__":
    A = [1, 2, 4] # ans 3

    obj = MissingNumber()
    print("Missing Number", obj.sumOfNumbers(A))
    print("Missing Number using XOR", obj.using_xor(A))
