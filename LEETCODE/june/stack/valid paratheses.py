''' Validate Parentheses
Solved 
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.'''

class Solution:
    def isValid(self, s: str) -> bool:
        l=['(','[','{']
        r=[')',']','}']
        stack=[]
        for i in s:
            stack.append(i)
            if len(stack)>1:
                top=stack[-1]
                prev=stack[-2]
                if top in r and prev in l and r.index(top)==l.index(prev):
                    stack.pop()
                    stack.pop()
        return False if stack else True
 
