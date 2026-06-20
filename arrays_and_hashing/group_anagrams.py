from typing import List

"""
Approach 1 (naive): create a function isAnagram(s,t) that finds out wether s and t are anagrams.
Then, for each word in the list, compare it to every other word. If they are anagrams, 
then we group that together. I guess this is not very good, because the time complexity
would be O(n²*x), where x is the complexity of isAnagram(s, t).

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If they're not the same lenght, we can already discard as anagram:
        if len(s) != len(t):
            return False
        
        # Create a character dictionary for s O(len(s))
        sdict = {}
        for char in s:
            if char not in sdict:
                sdict[char] = 1
            elif char in sdict:   
                sdict[char] += 1 

        # Create a character dictionary for s O(len(t))
        tdict = {}
        for char in t:
            if char not in tdict:
                tdict[char] = 1
            elif char in tdict:   
                tdict[char] += 1 

        # Checks wether the dictionaries are the same
        if len(sdict) != len(tdict): 
            return False
        for key in sdict.keys():
            if key not in tdict:
                return False
            elif sdict[key] != tdict[key]:
                return False
        
        return True
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Answer dictionary of string-list[string] key-value pairs
        ans = {}
        
        # Traversing the input list
        for word in strs:
            
            # We should check if it already has a anagram as a key
            found = False
            for key in ans.keys():
                if self.isAnagram(word, key):
                    ans[key].append(word)
                    found = True
                    break
                    
            # If neither the word nor one of its anagrams is in the answer dict 
            if not found:
                ans.update({word: [word]})
            
        # We need to build the output as a list of lists of strings:
        ans_list = []
        for key in ans.keys():
            ans_list.append(ans[key])
        
        return ans_list
        



# s = "carrace"
# t = "manuald"
# sol = Solution()
# print(sol.isAnagram(s,t))

# s = "act"
# t = "cat"
# sol = Solution()
# print(sol.isAnagram(s,t))

# s = "jar"
# t = "jam"
# sol = Solution()
# print(sol.isAnagram(s,t))


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

