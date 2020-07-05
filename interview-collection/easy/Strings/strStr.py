def strStr(haystack, needle):
    if len(needle) < 1: return 0

    k =  len(needle)
    n = len(haystack)

    for i in range(n-k+1):
        substr = haystack[i:i+k]
        if substr == needle: return i
    return -1

def test_1():
    haystack = "mississippi"
    needle = "pi"
    expected = 9
    result = strStr(haystack,needle)
    if expected == result:
        print('passed test 1')
    else:
        print('failed test 1. Expected {}, got {}'.format(expected, result))


test_1()
