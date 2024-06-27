'''22. Generate Parentheses
Solved
Medium
Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def bt(openN,closedN):
            if openN==closedN==n:
               res.append( "".join(stack))
            if openN<n:
                stack.append("(")
                bt(openN+1,closedN)
                stack.pop()

            if closedN<openN:
                stack.append(")")
                bt(openN,closedN+1)
                stack.pop()
        bt(0,0)
        return res

