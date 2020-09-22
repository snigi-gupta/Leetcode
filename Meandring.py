nums = [1,5,3,6,4,2,7]

sorted_nums = sorted(nums, reverse=True)
print(sorted_nums)
new_array = []

i = 0
j = len(sorted_nums)-1

while i < j:
    new_array.append(sorted_nums[i])
    i += 1
    new_array.append(sorted_nums[j])
    j -= 1

if i==j:
    new_array.append(sorted_nums[i])
print(new_array)