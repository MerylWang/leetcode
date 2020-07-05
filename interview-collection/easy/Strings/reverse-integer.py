


def reverse(x):
    # if x negative, set to positive for reverse and convert back to negative at end.
    x_neg = False

    if x < 0:
        x *= -1
        x_neg = True

    result = x % 10 # result = 3
    x = x // 10 # x = 12
    while x > 0:
        last_digit = x % 10
        result = (result * 10) + last_digit
        x = x // 10

    if abs(result) > (2**31 - 1): # return 0 if result out of range
        return 0
    else:
        return result if not x_neg else result*-1

'''
    * x is single digit
    * x is multi digit
    * x is negative
    * x is positive
    * x has trailing 0s
'''
def test_1():
    x = 123
    expected = 321
    result = reverse(x)
    if expected == result:
        print('passed test 1')
    else:
        print('failed test 1. Expected {}, got {}'.format(expected, rseult))

def test_2():
        x = -123
        expected = -321
        result = reverse(x)
        if expected == result:
            print('passed test 2')
        else:
            print('failed test 2. Expected {}, got {}'.format(expected, result))

def test_3():
        x = 120
        expected = 21
        result = reverse(x)
        if expected == result:
            print('passed test 3')
        else:
            print('failed test 3. Expected {}, got {}'.format(expected, rseult))

test_1()
test_2()
test_3()
