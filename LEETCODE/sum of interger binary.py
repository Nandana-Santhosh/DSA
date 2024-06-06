Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff
        while (mask&b)>0:
            a,b=a^b,(a&b)<<1
        return (mask&a) if b>0 else a