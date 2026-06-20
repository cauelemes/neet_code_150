"""
Approach: for each string, if they are no the same length, we return False. If not, we build a dictionary
where each distinct character is the key and its value is the number of times it appears. 
Building it will take O(s.length + t.length). Then, we simply compare both dictionaries and check wether 
they are the same, which should O(s.length) since they're the same length.

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # start by checking lenghts for easy exlusions
        if len(s) != len(t):
            return False
        
        # building both dictionaries
        s_dict = {}
        t_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char]+=1
            else:
                s_dict.update({char: 1})
        for char in t:
            if char in t_dict:
                t_dict[char]+=1
            else:
                t_dict.update({char: 1})
                
            
        # compare dictionaries
        for char in s:
            if char not in t_dict:
                return False
            elif s_dict[char] != t_dict[char]:
                return False

        return True



# s = "racecar"
# t = "carrace"

# solution = Solution()
# print(solution.isAnagram(s,t))
# print(solution.isAnagram("aaa","aa"))
# print(solution.isAnagram("abc","abd"))
# s = "jar"
# t = "jam"
# print(solution.isAnagram(s,t))


# dict1 = {"a": 1}
# dict1.update({"b": 1})
# print(dict1)


