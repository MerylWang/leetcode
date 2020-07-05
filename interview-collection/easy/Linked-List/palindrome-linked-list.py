import linked_list

''' 1. convert LL to array and check whether array is palindrome '''
''' 2. find midpoint of array. Reverse second half of array. palindrom if two subsets are identical (except midpoint if odd)'''

def find_middle(head):
    ''' given head, find midpoint of LL '''
    p1,p2 = head, head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    return p1

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def isPalindrome(head):
    if not head: return True
    if not head.next: return True

    p = find_middle(head)
    head2 = reverse_list(p)

    while head.next:
        if head.val != head2.val: return False
        head = head.next
        head2 = head2.next
    return True




# false
def test_1():
    arr = [1,2]
    head = linked_list.arrToList(arr)
    result = isPalindrome(head)
    expected = False
    if result == expected:
        print('passed test 1')
    else:
        print('failed test 1. Expected {}, got {}'.format(expected, result))

# even
def test_2():
    arr = [1,2,2,1]
    head = linked_list.arrToList(arr)
    result = isPalindrome(head)
    expected = True
    if result == expected:
        print('passed test 2')
    else:
        print('failed test 2. Expected {}, got {}'.format(expected, result))

# odd
def test_3():
    arr = [1,2,3,2,1]
    head = linked_list.arrToList(arr)
    result = isPalindrome(head)
    expected = True
    if result == expected:
        print('passed test 3')
    else:
        print('failed test 3. Expected {}, got {}'.format(expected, result))

# empty
def test_4():
    arr = []
    head = linked_list.arrToList(arr)
    result = isPalindrome(head)
    expected = True
    if result == expected:
        print('passed test 4')
    else:
        print('failed test 4. Expected {}, got {}'.format(expected, result))

# singleton
def test_5():
    arr = [1]
    head = linked_list.arrToList(arr)
    result = isPalindrome(head)
    expected = True
    if result == expected:
        print('passed test 5')
    else:
        print('failed test 5. Expected {}, got {}'.format(expected, result))

if __name__=='__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
