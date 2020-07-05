# def isAnagram(s,t):
    ''' given strings s,t, return whether they are anagrams of each other '''
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for char in s:
        s_map.setdefault(char,0)
        s_map[char] += 1

    for char in t:
        t_map.setdefault(char,0)
        t_map[char] += 1

    return s_map == t_map


def isAnagram(s,t):
    ''' use counter array '''
    if len(s) != len(t):
        return False

    counter = [0]*26 #a...z

    for i in range(len(s)):
        s_index = ord(s[i]) - 97 #e.g. 'a' -> 0
        t_index = ord(t[i]) - 97
        counter[s_index] += 1
        counter[t_index] -= 1

    for c in counter:
        if c != 0:
            return False
    return True






def test_1():
    s = "anagram"
    t = "nagaram"
    expected = True
    result = isAnagram(s,t)
    if expected == result:
        print('passed test 1')
    else:
        print('failed test 1. Expected {}, got {}.'.format(expected, result))

def test_2():
    s = 'rat'
    t = 'car'
    expected = False
    result = isAnagram(s,t)
    if expected == result:
        print('passed test 2')
    else:
        print('failed test 2. Expected {}, got {}.'.format(expected, result))


test_1()
test_2()
