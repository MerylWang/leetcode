def twoSum(nums, target):
    d = {}
    n = len(nums)

    for i in range(n): #O(n)
        value = target - nums[i]
        d[value] = i
    print('d: {}'.format(d))


    for i in range(n):
        elt = nums[i]
        if elt in d and i != d[elt]:
            return [i, d[elt]]

nums = [2,7,11,15]
target = 9
result = twoSum(nums,target)
print(result)
