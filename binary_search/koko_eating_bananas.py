"""
Approach 1: Let's simply use a binary search in order to choose a testing
value for k that goes from 1 to max(piles[i]) = M. So we'll start with
K = M/2. Then we'll traverse the piles list and count the x hours it 
should take.

If x <= h, this means we can try to further minimize k and should repeat the
search for k in [1, M/2). 

If x > h, this means we need to use a greater value for k so we should repeat the
search for k in [M/2, M]. 
"""

from typing import List

class Solution:
    def countsHours(self, piles: List[int], k: int) -> int:
        """
        Returns how many hours Koko would take to eat all the piles with a
        a banana-per-hour rate of k
        """
        x = 0
        
        for i in range(len(piles)):    
            x += piles[i]//k
            if piles[i]%k != 0:
                x += 1
                
        return x

    
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Binary search between 1 and len(piles) untill we find the best solution
        """
        
        # We start by sorting in place O(nlogn)
        piles.sort()
        
        # print(piles) (*)
        
        # Start with the worst possible solution, which is guaranteed by the problem's constraints
        k = piles[len(piles)-1]
        
        # Binary search until we minimize k
        l = 1
        r = piles[len(piles)-1]
        while l <= r:
        
            m = (l+r)//2
            
            
            # count how many hours it would take at rate m
            h_test = self.countsHours(piles, m)
            print(l, r, m, "hours =", h_test)
            
            # if the solution takes less or equals h hours
            if h_test <= h:
                r = m-1    
            
                # if it is smaller then the minimum we've found so far
                if m < k:
                    k = m
            
            # if the solution takes more than h hours
            if h_test > h:
                # Then we need to look for bigger possible values for k   
                l = m+1       

        return k
    
sol1 = Solution()

piles = [1,4,3,2]
h = 9
print(sol1.countsHours(piles, 1))
print(sol1.countsHours(piles, 2))


piles = [25,10,23,4]
h = 4
print(sol1.minEatingSpeed(piles, h))
piles = [25, 25]
h = 4
print(sol1.minEatingSpeed(piles, h))



""" 
Some ideas:

1. By the constraint:
        piles.length <= h
    it is clear, that we will always have the solution k = max(piles[i]), cause
    it guarantees we'll eat one pile per hor.

2. Examples:
    piles = [4, 4, 4]
    
    if h=3: then k must be 4.
    if h=4: then k also must be 4, since if it is any lower, we'll take 
    2 hours for every pile, totalling 6 hours.
    
    But if piles = [3, 3, 4], then if h=4, then we could have k = 3.
    
3 .If k = 1, then we'll take h = sum(piles[i]) hours

4. Let's start with if k = max(piles[i]). This means we'll take x = len(piles) 
hours. If x = h, we've already found the best solution. But if x < h, then we
might be able to decrease k further, since we still have x - h hours more
to use. Then let's set k = max(piles[i])/2... Think I've got it. Let's write
an approach.


    
"""
