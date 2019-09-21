"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Example 2:
Input: (5) + (5)
Output: 0 -> 1 
Explanation: 5 + 5 = 10.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, node=None):
         self.val = x
         self.next = node
    
    def list_vals(self):
        temp = self
        vals = []
        while temp:
            vals.append(temp.val)
            temp = temp.next
        return vals


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    val = l1.val + l2.val
    lsum = temp = ListNode(val%10)
    carry = (val-val%10)/10
    
    while l1.next or l2.next:
        if not l1.next:
            while l2.next:
                val = l2.next.val + carry
                temp.next = ListNode(val%10)
                carry = (val-val%10)/10
                temp = temp.next
                l2 = l2.next
                
        elif not l2.next:
            while l1.next:
                val = l1.next.val + carry
                temp.next = ListNode(val%10)
                carry = (val-val%10)/10
                temp = temp.next
                l1 = l1.next
    
        else:
            val = l1.next.val + l2.next.val + carry
            temp.next = ListNode(val%10)
            carry = (val-val%10)/10
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
    
    if carry==1:
        temp.next = ListNode(carry)
        
    return lsum
    

if __name__ == "__main__":
    print('Addition 1: [2,4,3] + [5,6,4] -> ' + str(addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))), ListNode(5,ListNode(6,ListNode(4)))).list_vals()))
    print('Addition 1: [5] + [5] -> ' + str(addTwoNumbers(ListNode(5), ListNode(5)).list_vals()))