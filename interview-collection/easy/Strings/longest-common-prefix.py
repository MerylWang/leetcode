def longestCommonPrefix(strs):
    if len(strs) < 1:
        return "" 
    prefix = strs[0]
    for s in strs:
        prefix = updatePrefix(prefix, s)
    return prefix

def updatePrefix(prefix,s):
    '''truncate prefix until it fits s'''
    if len(prefix) > len(s):
        prefix = prefix[:len(s)]

    i = 0
    while i < len(prefix):
        if prefix[i] != s[i]:
            return prefix[:i]
        else:
            i += 1
    return prefix


def test_1():
    strs = ["flower","flow","flight"]
    expected = "fl"
    result = longestCommonPrefix(strs)
    if expected == result:
        print("passed test 1")
    else:
        print('failed test 1. Expected {} but got {}'.format(expected, result))

def test_2():
    strs =  ["dog","racecar","car"]
    expected = ""
    result = longestCommonPrefix(strs)
    if expected == result:
        print("passed test 2")
    else:
        print('failed test 2. Expected {} but got {}'.format(expected, result))

test_1()
test_2()
