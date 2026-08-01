# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        length = 1
        while start.next:   
            length += 1
            start = start.next
        if length == 1:
            return None
        start = head
        for i in range(length - n - 1):
            start = start.next
        if n == length:
            #removing head of linked list
            rem = start.next
            start.next = None
            head = rem
        else:
            rem = start.next
            start.next = start.next.next
            rem.next = None
        return head

