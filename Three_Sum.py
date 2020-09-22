from itertools import islice
class ThreeSum:
    def __init__(self, num_list):
        self.num_list = num_list

    def get_zero_sum(self):

        result_array = set()
        checked_element = set()
        element_indexes = {num: i for i, num in enumerate(self.num_list)}

        # print(element_indexes)
        for i, val in enumerate(self.num_list):
            target = -val
            if val in checked_element:
                continue
            checked_element.add(val)

            for j, n in islice(enumerate(self.num_list), i+1, None):
                # print("val {}, target {}, thirdNo {}".format(val, target, n))
                # print("target - n", target - n)
                # print("j", j)
                # print("element_indexes.get(target - n, j)", element_indexes.get(target - n, j))
                if element_indexes.get(target - n, j) > j:
                    result_array.add(tuple(sorted([val, target-n, n])))

        # print(element_indexes)
        return [list(x) for x in result_array]


if __name__ == '__main__':

    array = [-1, 0, 1, 2, -1, -4]
    threeSum_obj = ThreeSum(array)
    result = threeSum_obj.get_zero_sum()
    print(result)
