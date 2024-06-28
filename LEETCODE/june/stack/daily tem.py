'''739. Daily Temperatures
Solved
Medium
Topics
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[] #pair:[temp,index]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t >stack[-1][0]:
                stack_t,stack_i=stack.pop()
                res[stack_i]=(i-stack_i)
            stack.append((t,i))
        return res

        #time=O(n)
        #s=O(n)
