'''You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        temp = temp.next
        curr = head
        sum = 0
        while temp:
            if temp.val != 0:
                sum += temp.val
            else:
                curr = curr.next
                curr.val = sum
                sum = 0
            temp = temp.next
        curr.next = None
        return head.next
        

  
        