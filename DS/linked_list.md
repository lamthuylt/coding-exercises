# Linked list

A linked list consists of nodes, where each node contains a data field and a reference (link) to the next node of the list.

## Singly linked list
#### Description
Singly linked lists contain nodes which have:
* a data field 
* 'next' field, which points to the next node in line of nodes.\

Operations that can be performed on singly linked lists include insertion, deletion and traversal.

<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg" alt="{{ include description }}">
  Figure 1 - A linked list whose nodes contain 2 fields: a value and a reference to the next node. The last node is linked to NULL, signifying the end of the list.
</figure>

#### Implementation
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__=='__main__':
    # create the linked list in Fig.1
    head = Node(12)
    node2 = Node(99)
    node3 = Node(37)
    head.next = node2
    node2.next = node3

    # add a new node with data value to the end of a singly linked list
    

```



