"""
LeetCode #1: Two Sum
Dificultad: Easy
Link: https://leetcode.com/problems/two-sum/

Problema:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Conceptos clave:
- Hash Tables
- Array manipulation
- Time complexity: O(n)
- Space complexity: O(n)

Ejemplo:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 1: Brute Force - O(n²) time, O(1) space
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_optimized(self, nums: List[int], target: int) -> List[int]:
        """
        Approach 2: Hash Table - O(n) time, O(n) space
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

def test_two_sum():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0, 1]
    result1 = solution.twoSum_optimized(nums1, target1)
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    expected2 = [1, 2]
    result2 = solution.twoSum_optimized(nums2, target2)
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3 - Edge case
    nums3 = [3, 3]
    target3 = 6
    expected3 = [0, 1]
    result3 = solution.twoSum_optimized(nums3, target3)
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_two_sum()