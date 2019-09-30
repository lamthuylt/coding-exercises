# Linked list

A linked list consists of nodes, where each node contains a data field and a reference (link) to the next node of the list.
<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg" alt="{{ include description }}">
  (source: https://en.wikipedia.org/wiki/File:Singly-linked-list.svg)
</figure>

## Singly linked list
Singly linked lists contain nodes which have:
* a data field 
* 'next' field, which points to the next node in line of nodes.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```
e.g. implementation of the following linked list
<figure class="image">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg" alt="{{ include description }}">
  (source: https://en.wikipedia.org/wiki/File:Singly-linked-list.svg)
</figure>

```python
# define new nodes
head = Node(12)
node2 = Node(99)
node3 = Node(37)
# make connections
head.next = node2
node2.next = node3
```

Operations that can be performed on singly linked lists include insertion, deletion and traversal.




