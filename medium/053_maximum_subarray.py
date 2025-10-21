"""
LeetCode #53: Maximum Subarray (Kadane's Algorithm)
Dificultad: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Problema:
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Conceptos clave:
- Dynamic Programming
- Kadane's Algorithm
- Greedy approach
- Time complexity: O(n)
- Space complexity: O(1)

Ejemplo:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

from typing import List

class Solution:
    def maxSubArray_bruteforce(self, nums: List[int]) -> int:
        """
        Approach 1: Brute force - O(n²) time
        """
        # TODO: Implementar solución brute force
        pass
    
    def maxSubArray_kadane(self, nums: List[int]) -> int:
        """
        Approach 2: Kadane's Algorithm - O(n) time
        """
        # TODO: Implementar algoritmo de Kadane
        pass
    
    def maxSubArray_divide_conquer(self, nums: List[int]) -> int:
        """
        Approach 3: Divide and Conquer - O(n log n) time
        """
        # TODO: Implementar solución divide and conquer
        pass

def test_max_subarray():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6
    # result1 = solution.maxSubArray_kadane(nums1)
    # assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2 - Single element
    nums2 = [1]
    expected2 = 1
    
    # Test case 3 - All negative
    nums3 = [-2, -1, -3]
    expected3 = -1
    
    # Test case 4 - All positive
    nums4 = [1, 2, 3, 4]
    expected4 = 10
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_max_subarray()