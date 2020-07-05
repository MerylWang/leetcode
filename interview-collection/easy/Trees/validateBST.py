from tree import arr_to_tree

''' using recursion. O(n) time. O(log n) space. '''
def isValidBST(root):
    return checkNode(root)


def checkNode(node, lower=float('-inf'), upper=float('inf')):
    if not node:
        return True

    val = node.val
    if val <= lower or val >= upper:
        return False
    if not checkNode(node.left, lower, val):
        return False
    if not checkNode(node.right, val, upper):
        return False
    return True

def test_1():
    arr = [2,1,3]
    root = arr_to_tree(arr)
    expected = True
    result = isValidBST(root)
    if expected == result:
        print('passed test 1')
    else:
        print("failed test 1. Expected {}, got {}".format(expected, result))

if __name__=='__main__':
    test_1()
