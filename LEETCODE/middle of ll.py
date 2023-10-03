'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.'''

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1 
        temp=head
        while temp.next : 
            count +=1 
            temp = temp.next 
        	
        middle = count//2+1 
     
        count = 1 
        temp = head 
        while count < middle:
            count+=1 
            temp = temp.next 
        return temp 