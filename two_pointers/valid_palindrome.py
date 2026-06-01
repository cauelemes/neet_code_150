from typing import List

"""
Approach 1: First, we will remove any non alphanumeric characters from the input string. Then,
we will make every character to be lower case. From there, we will treat the string as an array
which we'll traverse using two pointers simultaneously. Both pointers should start at the opposite
extremes, and go to the middle. If, in any given iteration, the pointers don't point to the same
value, then it is not a palindrome. 

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Processed version of s with only lower alphanumerical values
        s_proc = []
        for i in range(len(s)):
            if s[i].isalnum():
                s_proc.append(s[i].lower())
        
        l = 0
        r = len(s_proc)-1
        
        # Traverse from the extremes checking if characters are the same
        while(l <= r):
            if s_proc[l] != s_proc[r]:
                return False
            l+=1
            r-=1
        
        return True    

sol1 = Solution()
in1 = "Was it a car or a cat I saw?"
print(sol1.isPalindrome(in1))
in1 = "o v o"
print(sol1.isPalindrome(in1))
in1 = "o v o s"
print(sol1.isPalindrome(in1))
in1 = "tab a cat"
print(sol1.isPalindrome(in1))
in1 = "0P"
print(sol1.isPalindrome(in1))

# (*) Come back later with a solution that optimizes space complexity to O(1): just do 
# everything directly in place using pointers on the original string.

