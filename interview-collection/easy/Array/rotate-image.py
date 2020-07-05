def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)


    # r,c = 0,0
    # curr = matrix[r][c]
    # count = 0
    #
    # while count < n:
    #     r,c = c, n-r-1
    #     nxt = matrix[r][c]
    #     matrix[r][c] = curr
    #     curr = nxt
    #     count += 1


def test_1():
    matrix = [[1, 2, 3], [4,5,6],[7,8,9]]
    expected = [[7,4,1],[8,5,2],[9,6,3]]
    rotate(matrix)
    if matrix == expected:
        print('passed test 1')
    else:
        print('failed test 1')
        print('expected {}'.format(expected))
        print('got {}'.format(matrix))

def test_2():
    matrix = [[1,2],[3,4]]
    expected = [[3,1],[4,2]]
    rotate(matrix)
    if matrix == expected:
        print('passed test 2')
    else:
        print('failed test 2')
        print('expected {}'.format(expected))
        print('got {}'.format(matrix))

def test_3():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

    expected = [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
    rotate(matrix)
    if matrix == expected:
        print('passed test 3')
    else:
        print('failed test 3')
        print('expected {}'.format(expected))
        print('got {}'.format(matrix))

test_1()
test_2()
# test_3()
