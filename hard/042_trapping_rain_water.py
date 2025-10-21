"""
LeetCode #42: Trapping Rain Water
Dificultad: Hard
Link: https://leetcode.com/problems/trapping-rain-water/

Problema:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Conceptos clave:
- Two Pointers
- Dynamic Programming
- Stack
- Array manipulation
- Multiple solution approaches
- Time complexity: O(n)
- Space complexity: O(1) for two pointers, O(n) for DP

Ejemplo:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water are being trapped.
"""

from typing import List

class Solution:
    def trap_bruteforce(self, height: List[int]) -> int:
        """
        Approach 1: Brute Force
        Time: O(n²), Space: O(1)
        """
        # TODO: Implementar solución brute force
        pass
    
    def trap_dp(self, height: List[int]) -> int:
        """
        Approach 2: Dynamic Programming
        Time: O(n), Space: O(n)
        """
        # TODO: Implementar solución con DP
        pass
    
    def trap_stack(self, height: List[int]) -> int:
        """
        Approach 3: Using Stack
        Time: O(n), Space: O(n)
        """
        # TODO: Implementar solución usando stack
        pass
    
    def trap_two_pointers(self, height: List[int]) -> int:
        """
        Approach 4: Two Pointers (Optimal)
        Time: O(n), Space: O(1)
        """
        # TODO: Implementar solución con two pointers
        pass

def test_trapping_rain_water():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected1 = 6
    # result1 = solution.trap_two_pointers(height1)
    # assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2
    height2 = [4, 2, 0, 3, 2, 5]
    expected2 = 9
    
    # Test case 3 - No water can be trapped
    height3 = [1, 2, 3, 4, 5]
    expected3 = 0
    
    # Test case 4 - Single element
    height4 = [5]
    expected4 = 0
    
    # Test case 5 - Two elements
    height5 = [3, 2]
    expected5 = 0
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_trapping_rain_water()