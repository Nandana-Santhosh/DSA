'''Evaluate Reverse Polish Notation
Solved 
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
               stack.append (stack.pop()+stack.pop())

            elif i=="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif i=="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            elif i=="*":
                stack.append (stack.pop()*stack.pop())
            else:
                stack.append(int(i))  
        return stack[0] 