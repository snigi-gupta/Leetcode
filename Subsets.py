import copy

class Solution:
    def subsets(self, nums):
        def check_subset(nums, index, result):
            print("Before if, result: ", result)
            if index == len(nums) - 1:
                result.append([])
                result.append([nums[index]])
                print("Inside if, after append, result: ", result) # [[], [3]]
            else:
                # check_subset(nums, index+1, result) #[1,2,3], 1, [[], [3]]
                # print("Inside else, after recursion call, result: ", result)
                # temp = copy.deepcopy(result)
                # for r in temp: #[]
                #     r.append(nums[index]) #[2]
                #     print("Element is: ", nums[index])
                #     print("After element append: ", r)
                #     # result.append(r)  # [[], [3], [2], [3,2]]
                #     print("In for loop, result: ", result)
                # result.extend(temp)

                check_subset(nums, index + 1, result)  # [1,2,3], 1, [[], [3]]
                print("Inside else, after recursion call, result: ", result)
                for i in range(len(result)):  # []
                    result.append(result[i] + [nums[index]])
                    print("Element is: ", nums[index])
                    # result.append(r)  # [[], [3], [2], [3,2]]
                    print("In for loop, result: ", result)



        if nums is None:
            return [[]]
        result = []
        check_subset(nums, 0, result)
        return result

        # def create_subsets(nums):
        #     output = [[]]
        #
        #     for val in nums:
        #         for i in range(len(output)):
        #             output.append(output[i]+[val])
        #       # output =  [out + [val] for out in output
        #     return output
        # return create_subsets(nums)


if __name__ == "__main__":
    nums = [1,2,3]
    obj = Solution()
    answer = obj.subsets(nums)
    print("Answer:", answer)

