'''
21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result=l3=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                
                l3.next=list1
                list1=list1.next
            else:
                l3.next=list2.val
                list2=list2.next
            l3=l3.next
        if list1:
            l3.next=list1
        else:
            l3.next=list2

        return result.next
