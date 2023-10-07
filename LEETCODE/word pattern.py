'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new=s.split()
        if len(new)!=len(pattern):
            return False
        for i in range(len(new)):
            if pattern.find(pattern[i])!=new.index(new[i]):
                return False
        return True
        

class Solution:
  def wordPattern(self, pattern: str, str: str) -> bool:
    text = str.split()
    return [*map(pattern.index, pattern)] == [*map(text.index, text)]
 
        
