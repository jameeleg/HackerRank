"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if not head:
        return 0
   
    first_ptr = head
    second_ptr = head.next
    while first_ptr != second_ptr:
        first_ptr = first_ptr and first_ptr.next
        second_ptr = second_ptr and second_ptr.next and second_ptr.next.next
    
    if second_ptr:
        return 1
    
    return 0
    
