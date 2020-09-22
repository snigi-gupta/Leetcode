class TwoSum():

    def __init__(self, number_list, tar):
        self.num_list = number_list
        self.target = tar

    def get_index(self):

        temp_dict = dict()

        for index, value in enumerate(self.num_list):
            complement = self.target - value

            if complement in temp_dict:
                return [temp_dict[complement], index]
            else:
                temp_dict[value] = index


if __name__ == '__main__':
    num_list = [2, 5, 7, 11]
    target = 9
    twoSum_obj = TwoSum(num_list, target)
    result = twoSum_obj.get_index()
    print(result)
