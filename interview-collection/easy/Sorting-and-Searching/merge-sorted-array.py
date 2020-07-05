def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_end = m
    i,j = 0,0 # nums1, nums2 pointers
    while j < n:
        if i >= nums1_end:
            nums1[i] = nums2[j]
            i += 1
            j += 1
        else :
            if nums1[i] >= nums2[j]:
                # shift num1[i:num1_end] down
                for k in range(nums1_end-1, i-1, -1):
                    nums1[k+1] = nums1[k]
                nums1_end += 1
                nums1[i] = nums2[j]
                i += 2
                j += 1
            else:
                i += 1
    return nums1

def test_1():
    nums1 = [1,2,3,0,0,0]
    nums2 = [4,5,6]
    m, n = 3, 3
    result = merge(nums1, m, nums2, n)
    expected = [1,2,3,4,5,6]
    if expected == result:
        print('passed test 1')
    else:
        print("failed test 1. Expected {}, got {}".format(expected, result))

if __name__ == '__main__':
    test_1()
