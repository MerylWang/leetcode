def countAndSay(n):
    ''' given int n such that 1 <= n <= 30, returns n-th term of count and say '''
    result = '1'
    i = 1
    while i < n:
        result = helper(result)
        i += 1

    return result

def helper(s):
    ''' given current string(nonempty), returns its count and say '''
    result = ""
    count = 0
    current = s[0]
    for char in s:
        if char != current:
            result += str(count) + current
            current = char
            count = 1
        else:
            count += 1

    result += str(count) + current
    return result


def test_1():
    n = 1
    expected = '1'
    result = countAndSay(n)
    if expected == result:
        print('passed test 1')
    else:
        print('failed test 1. Expected {}, got {}'.format(expected, result))

def test_2():
    n = 2
    expected = '11'
    result = countAndSay(n)
    if expected == result:
        print('passed test 2')
    else:
        print('failed test 2. Expected {}, got {}'.format(expected, result))

def test_3():
    n = 3
    expected = '21'
    result = countAndSay(n)
    if expected == result:
        print('passed test 3')
    else:
        print('failed test 3. Expected {}, got {}'.format(expected, result))

def test_4():
    n = 4
    expected = '1211'
    result = countAndSay(n)
    if expected == result:
        print('passed test 4')
    else:
        print('failed test 4. Expected {}, got {}'.format(expected, result))

test_1()
test_2()
test_3()
test_4()
