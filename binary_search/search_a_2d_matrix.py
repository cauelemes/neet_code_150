from typing import List

"""
Approach: we can convert the matrix to a single array by using a function that converts
doubled indexes (i,j) for the matrix to a single index k for the array. The matrix is alterady
sorted in such a way that this resulting single array is also sorted. Hence, we can perform a
regular binary search in the array to se if it contains the target (which means the matrix also
does). 
Time complexity: O(log(m*n))
Space complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = n*m-1
        
        while l <= r:
            
            m = (l+r)//2
            
            # obtaining matrix indexes
            mj = m % n 
            mi = (m - mj)//n
            
            # search in greater sublist
            if target > matrix[mi][mj]:
                l = m + 1
                
            # search in lesses sublist
            if target < matrix[mi][mj]:
                r = m - 1
                
            # found the guy!
            if target == matrix[mi][mj]:
                return True
            

        return False
    
    
sol1 = Solution()

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] 
target = 10    
print(sol1.searchMatrix(matrix, target))

    


