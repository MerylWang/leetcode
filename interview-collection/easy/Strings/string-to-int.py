def myAtoi(str):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    nums = '0123456789'
    n = len(str)

    s = None # start of num
    t = None # end of num

    i = 0 # current pointer

    while i < n:
        if str[i] == ' ':
            if s is not None:
                t = i
                break
            i += 1
        elif str[i] == '-' or str[i] == '+':
            if s is None:
                s = i
                i += 1
            else:
                t = i
                break

        elif str[i] in nums:
            if s is None: s = i
            i += 1
        else:
            t = i
            break

    if s is None:
        return 0
    else:
        if t is None: t = n

    try:
        result = int(str[s:t])
    except:
        return 0

    if result > INT_MAX:
        return INT_MAX
    elif result < INT_MIN:
        return INT_MIN
    else:
        return result


def test_1():
    str = '42'
    expected = 42
    result = myAtoi(str)
    if expected == result:
        print('passed test 1')
    else:
        print('failed test 1: expected {}, got {}'.format(expected, result))

def test_2():
    str = "   -42"
    expected = -42
    result = myAtoi(str)
    if expected == result:
        print('passed test 2')
    else:
        print('failed test 2: expected {}, got {}'.format(expected, result))

def test_3():
    str = "word"
    expected = 0
    result = myAtoi(str)
    if expected == result:
        print('passed test 3')
    else:
        print('failed test 3: expected {}, got {}'.format(expected, result))

def test_4():
    str = "-word"
    expected = 0
    result = myAtoi(str)
    if expected == result:
        print('passed test 4')
    else:
        print('failed test 4: expected {}, got {}'.format(expected, result))

def test_5():
    str = "4193 with words"
    expected = 4193
    result = myAtoi(str)
    if expected == result:
        print('passed test 5')
    else:
        print('failed test 5: expected {}, got {}'.format(expected, result))

def test_6():
    str = "-91283472332"
    expected = -2147483648
    result = myAtoi(str)
    if expected == result:
        print('passed test 6')
    else:
        print('failed test 6: expected {}, got {}'.format(expected, result))

def test_7():
    str = "words and 4193"
    expected = 0
    result = myAtoi(str)
    if expected == result:
        print('passed test 7')
    else:
        print('failed test 7: expected {}, got {}'.format(expected, result))

def test_8():
    str = " "
    expected = 0
    result = myAtoi(str)
    if expected == result:
        print('passed test 8')
    else:
        print('failed test 8: expected {}, got {}'.format(expected, result))

def test_9():
    str = ""
    expected = 0
    result = myAtoi(str)
    if expected == result:
        print('passed test 9')
    else:
        print('failed test 9: expected {}, got {}'.format(expected, result))

def test_10():
    str = "+"
    expected = 0
    result = myAtoi(str)
    if expected == result:
        print('passed test 10')
    else:
        print('failed test 10: expected {}, got {}'.format(expected, result))

def test_11():
    str = "+1"
    expected = 1
    result = myAtoi(str)
    if expected == result:
        print('passed test 11')
    else:
        print('failed test 11: expected {}, got {}'.format(expected, result))

def test_12():
    str = "    -88827   5655  U"
    expected = -88827
    result = myAtoi(str)
    if expected == result:
        print('passed test 12')
    else:
        print('failed test 12: expected {}, got {}'.format(expected, result))

def test_13():
    str = "-5-"
    expected = -5
    result = myAtoi(str)
    if expected == result:
        print('passed test 13')
    else:
        print('failed test 13: expected {}, got {}'.format(expected, result))

test_1()
test_2()
test_3()
test_4()
test_5()
test_6()
test_7()
test_8()
test_9()
test_10()
test_11()
test_12()
test_13()
