'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true '''

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 != 0 : return False
        openb = ['(','[','{']
        closeb = [')',']','}']
        li = []

        l = r = 0
        for r in range(n):
            if s[r] in openb:
                 li.append(openb.index(s[r]))
            elif s[r] in closeb: 
                if li and closeb.index(s[r]) ==li[-1]:
                    li.pop()
                else: return False
        if li==[]:
            return True
        
##another approach
s=s.replace('()','').replace('{}','').replace('[]','')

##approach using dic
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","}":"{","]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif stack and mapping[char]==stack[-1]:
                stack.pop()
            else:
                return False
        return stack==[]
        