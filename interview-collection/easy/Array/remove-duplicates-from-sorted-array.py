def removeDuplicates(nums):
    i = 0 # points to first occurrence

    while i < len(nums):
        j = i+1

        # if j < len(nums):
            # print("n: ", len(nums))
        while j < len(nums) and nums[j] == nums[i]:
            j += 1
            print('j: ', j)


        for ind in range(i+1, j):
            nums.pop(i+1)

        i += 1

    print(nums)
    return len(nums)

# input = [1,1,2]
# input = [0,0,1,1,1,2,2,3,3,4]
input = [1,1]

result = removeDuplicates(input)
print(result)
