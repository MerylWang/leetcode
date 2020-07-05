import re

'''using regex '''
# def isPalindrome(s):
#     s = re.sub(r'[^\w]','',s)
#     s = s.lower()
#
#     n = len(s)
#     for i in range(n//2):
#         if not s[i] == s[n-i-1]:
#             return False
#     return True

'''without using regex'''
def isAlphanumeric(char):
    '''returns True is char is alphanumeric'''
    alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'
    if char in alphanumeric:
        return True
    else:
        return False
#
#
# def isPalindrome(s):
#     s = s.lower()
#     s = list(filter(isAlphanumeric, s))
#
#     n = len(s)
#     for i in range(n//2):
#         if not s[i] == s[n-i-1]: return False
#     return True

''' using two pointers'''
def isPalindrome(s):
    s = s.lower()
    s = list(filter(isAlphanumeric,s))

    n = len(s)
    p1 = 0
    p2 = n-1
    while p1 < p2:
        if s[p1] != s[p2]: return False
        p1 += 1
        p2 -= 1
    return True





def test_1():
    s = "A man,     a     plan, a canal: Panama"
    expected = True
    result = isPalindrome(s)
    if expected == result:
        print("passed test 1")
    else:
        print('failed test 1: expected {}, got {}'.format(expected, result))
def test_2():
    s = "race a car"
    expected = False
    result = isPalindrome(s)
    if expected == result:
        print("passed test 2")
    else:
        print('failed test 2: expected {}, got {}'.format(expected, result))

test_1()
test_2()
