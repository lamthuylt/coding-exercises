"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode(object):    
    def __init__(self, x, node=None):
         self.val = x
         self.next = node
         
    def display(self):
        temp = self
        vals = []
        while temp:
            vals.append(temp.val)
            temp = temp.next
        print(vals)


# recursive solution
def mergeTwoLists1(l1, l2):
    l3 = ListNode(0)
    
    def merge(l1,l2,lr):
        if l1==None:
            if l2!=None:
                lr.next = ListNode(l2.val)
                merge(l1, l2.next, lr.next)
        elif l2==None:
            if l1!=None:
                lr.next = ListNode(l1.val)
                merge(l1.next, l2, lr.next)
        elif l1.val <= l2.val:
            lr.next = ListNode(l1.val)
            merge(l1.next, l2, lr.next)
        else:
            lr.next = ListNode(l2.val)
            merge(l1, l2.next, lr.next)
    
    merge(l1,l2,l3)
    
    return l3.next
    
    
# iterative solution
def mergeTwoLists2(l1, l2):    
    # initialize the return list (lr is fixed for return, temp will move for merging)
    lr = temp = ListNode(0)
    
    while l1 or l2:
        # if l1 exhausts first, fill lr with all the remaining nodes of l2
        if not l1:
            while l2:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
        # if l2 exhausts first, fill lr with all the remaining nodes of l1
        elif not l2:
            while l1:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
        # otherwise, fill lr with the smaller node between l1 and l2
        else:
            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next

    return lr.next
    

if __name__ == '__main__':
    l1 = ListNode(1,ListNode(2,ListNode(4)))
    l2 = ListNode(1,ListNode(3,ListNode(4)))
    mergeTwoLists2(l1,l2).display()