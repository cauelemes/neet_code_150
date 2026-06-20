from typing import List

"""
Approach 2: We can consider that any input string will be formed by a combination of  the 26
characters in the alphabet. Every anagram has the same count of characters used from this alphabet.
We could create a 26-sized tuple that identifies every anagram that uses that given character count.
Traversing the input list, we could store each word in a appropriate key-value pair by counting 
its character frequency

"""

class Solution:
    
    # For a given string, returns tuple with character count
    def charCount(self, s: str) -> tuple:
        
        # Creates empty 26-character count list
        count = 26*[0]
        
        for char in s:
            count[ord(char)-ord('a')]+=1
        
        return tuple(count)
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Start the dictionary of anagrams
        anagrams = {}
        
        for word in strs:
            
            freq_key = self.charCount(word)
            if freq_key in anagrams.keys():
                anagrams[freq_key].append(word)
            else:
                anagrams[freq_key]=[word]    
        
        ans = []
        for word_list in anagrams.values():
            ans.append(word_list)
        
        return ans
        



strs = ["act","pots","tops","cat","stop","hat"]
sol = Solution()
print(sol.groupAnagrams(strs))

strs = ["x"]
sol = Solution()
print(sol.groupAnagrams(strs))

strs = [""]
sol = Solution()
print(sol.groupAnagrams(strs))

strs = ["",""]
sol = Solution()
print(sol.groupAnagrams(strs))

# s = "abbcz"
# sol = Solution()
# print(sol.charCount(s))

