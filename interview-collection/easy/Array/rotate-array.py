''' brute force '''
# def rotate(nums):
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     n = len(nums)
#     for i in range(k):
#         temp = nums[-1]
#         for j in range(n-1, 0, -1):
#             nums[j] = nums[j-1]
#         nums[0] = temp


def rotate(nums,k):
    ''' cyclic replacement O(n) '''
    n = len(nums)
    s = 0 # start
    t = (s + k) % n
    current = nums[s]
    count = 0

    while count < n:
        print(nums)
        nxt = nums[t]
        nums[t] = current
        s = t
        t = (s + k) % n
        current = nxt
        count += 1

def test_1():
    nums = [1,2,3,4,5,6,7]
    rotate(nums,3)

def test_2():
    # nums = [-1, -100, 3, 99]
    nums = [0,1, 2, 3]
    rotate(nums,2)

test_1()
test_2()
