class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arr_to_tree(arr):
    '''given array, convert to tree & return root node '''
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    return root


def display_tree(root):
    '''given root node of tree, print tree '''
    # inOrder(root)

# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):

    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root

# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)

# Driver Code
if __name__ == '__main__':
    arr = [2,1,3]
    root = arr_to_tree(arr)
    inOrder(root)
