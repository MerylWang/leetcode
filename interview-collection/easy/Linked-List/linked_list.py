class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def display_list(head):
    ''' given head, prints LL as an array '''
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    # print(arr)
    return arr


def arrToList(arr):
    ''' converts array to a LL & returns head '''
    head = ListNode()
    n = head

    for elt in arr:
        n.next = ListNode(elt)
        n = n.next

    return head.next


# if __name__=='__main__':
    # arr = [1, 2, 3, 4, 5]
    # arr = []
    # head = arrToList(arr)
    # display_list(head)
