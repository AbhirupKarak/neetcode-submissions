# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = head.next #we start with the second node in the linked list
        halves = []
        while start:
            halves.append(start)
            start = start.next
    
        start = head
        #now we use two pointers:
        left = 0
        right = len(halves) - 1
        if len(halves) % 2:
            while(left < right):
                start.next = halves[right]
                start = start.next
                start.next = halves[left]
                start = start.next
                left += 1
                right -= 1
            if (left == right):
                start.next = halves[right]
                start = start.next
            start.next = None
        else:
            while(left <= right):
                start.next = halves[right]
                start = start.next
                start.next = halves[left]
                start = start.next
                left += 1
                right -= 1
            start.next = None
        
            



