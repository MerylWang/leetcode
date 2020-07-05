from tree import arr_to_tree

def isSymmetric(root):
    # print('hi')
    if not root: return True

    q_left = [root.left]
    values_left = []
    while q_left:
        node = q_left.pop()
        if node:
            values_left.append(node.val)
            q_left.append(node.left)
            q_left.append(node.right)
        else:
            values_left.append(None)

    # print(values_left)

    q_rt = [root.right]
    values_rt = []
    while q_rt:
        node = q_rt.pop()
        if node:
            values_rt.append(node.val)
            q_rt.append(node.right)
            q_rt.append(node.left)
        else:
            values_rt.append(None)
    # print(values_rt)

    return values_left == values_rt



def test_1():
    arr = [1,2,2,3,4,4,3]
    root = arr_to_tree(arr)
    result = isSymmetric(root)
    expected = True
    if expected == result:
        print('passed test 1')
    else:
        print("failed test 1. Expected {}, got {}".format(expected, result))

def test_2():
    arr = [1,2,2,None,3,None,3]
    root = arr_to_tree(arr)
    result = isSymmetric(root)
    expected = True
    if expected == result:
        print('passed test 2')
    else:
        print("failed test 2. Expected {}, got {}".format(expected, result))


if __name__ == '__main__':
    test_1()
    test_2()
