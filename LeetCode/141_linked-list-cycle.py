"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



##########################
# Solution 1 
# Space complexity: O(n))
##########################
def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # we use a hash table to check whether a node has been visited before
    visited = {}

    if head==None:
        return False
    else:
        # go through each node one by one and record each node's reference in a hash table (key=reference, value=position)
        node = head        
        pos = 0
        while node!=None:
            # if the current node's reference is in the hash table, then return True
            if node in visited:
                return True, visited[node]
            else:
                visited[node] = pos
                node = node.next
                pos += 1
        # if the current node is none, we have reached the end of the list and it must not be cyclic
        return False
        
        
if __name__ == '__main__':
    # example 1    
    head1 = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    head1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1
    print(hasCycle(head1))
    
    # example 2
    head2 = ListNode(1)
    node1 = ListNode(2)
    head2.next = node1
    node1.next = head2
    print(hasCycle(head2))
    
    # example 2
    head3 = ListNode(1)
    print(hasCycle(head3))
    
            