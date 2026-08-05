# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(0)
        dummy.next =  head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        n = size // k
        curr = head
        prevTail = dummy.next
        for i in range(n):
            j = k
            print(curr.val)
            currHead = curr
            prev = None
            while j and curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                j -= 1
            #here i must link prevTail to nextHead
            prevTail.next = prev
            currTail = currHead
            prevTail = currHead
            currTail.next = curr
            if i == 0:
                dummy.next = prev

        return dummy.next
            
        

    