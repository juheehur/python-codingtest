# Generated from blog post
# Title: Leetcode-21
# Date: 2025-02-25
# Code Block 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  
        current = dummy

        # 두 연결 리스트를 오름차순으로 병합
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 남은 노드 연결
        current.next = list1 if list1 else list2
        
        return dummy.next