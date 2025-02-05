# Generated from blog post
# Title: [Leetcode] 2. Add Two Numbers
# Date: 2025-02-05
# Code Block 1
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode()
        current = dummy_head
        carry = 0 #자리올림

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 # l1 이 none이면 0
            val2 = l2.val if l2 else 0

            total=val1+val2+carry

            carry = total//10 # 10으로 나눠지면 자리올림

            current.next = ListNode(total%10)

            current = current.next 

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next