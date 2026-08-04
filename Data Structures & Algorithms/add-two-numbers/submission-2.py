# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1
        num2 = l2
        carry = 0
        dummy = ListNode()
        tail = dummy
        while(num1 or num2):
            v1 = num1.val if num1 else 0
            v2 = num2.val if num2 else 0
            newNode = ListNode((v1 + v2 + carry) % 10)
            carry = (v1 + v2 + carry) // 10
            tail.next = newNode
            tail = tail.next
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
        if carry == 1:
            newNode = ListNode(carry)
            tail.next = newNode
            tail = tail.next
        return dummy.next