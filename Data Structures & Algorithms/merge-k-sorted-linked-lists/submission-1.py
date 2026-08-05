# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ##brute force
        newList = []
        for lst in lists:
            curr = lst
            while curr:
                newList.append(curr.val)
                curr = curr.next
        
        newList.sort()
        tail = ListNode()
        head = tail
        for num in newList:
            newNode = ListNode(num)
            tail.next = newNode
            tail = tail.next
        return head.next
