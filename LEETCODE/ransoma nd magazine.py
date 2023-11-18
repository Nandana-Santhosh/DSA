'''Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false '''



from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        str1 = Counter(ransomNote)  # Frequency counter for the ransom note
        str2 = Counter(magazine)    # Frequency counter for the magazine
        
        # Check if all characters in the ransom note have enough occurrences in the magazine
        if str1 & str2 == str1:
            return True
        else:
            return False