def checkGrid(board, r_start, c_start):
    ''' checks whether entries are valid in board for a 3x3 grid'''
    r_end = r_start + 3
    c_end = c_start + 3
    elts = set()
    for r in range(r_start, r_end):
        for c in range(c_start, c_end):
            elt = board[r][c]
            if elt != ".":
                if elt in elts:
                    return False
                else:
                    elts.add(elt)
    return True




def isValidSudoku(board):
    n = 9 # n x n board

    ''' for each row, check no number repeats '''
    for r in range(n):
        row = board[r]
        elts = set()
        for elt in row:
            if elt != ".":
                if elt in elts:
                    return False
                else:
                    elts.add(elt)

    ''' for each col, check no number repeats'''
    for c in range(n):
        elts = set()
        for r in range(n):
            elt = board[r][c]
            if elt != ".":
                if elt in elts:
                    return False
                else:
                    elts.add(elt)

    ''' for each 3x3 grid, check no number repeats'''
    for r_start in range(0,9,3):
        for c_start in range(0,9,3):
            if not checkGrid(board,r_start,c_start):
                return False

    return True



def test_1():

    input = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    expected = True
    result = isValidSudoku(input)
    if expected == result:
        print('test 1: passed')
    else:
        print('test 1 failed. expected {} got {}'.format(expected, result))

test_1()
