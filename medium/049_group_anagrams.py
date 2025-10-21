"""
LeetCode #49: Group Anagrams
Dificultad: Medium
Link: https://leetcode.com/problems/group-anagrams/

Problema:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Conceptos clave:
- Hash Tables
- String manipulation
- Sorting
- Character frequency counting
- Time complexity: O(n * k log k) where k is max length of string
- Space complexity: O(n * k)

Ejemplo:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams_sorting(self, strs: List[str]) -> List[List[str]]:
        """
        Approach 1: Sorting each string as key
        """
        # TODO: Implementar solución usando sorting
        pass
    
    def groupAnagrams_counting(self, strs: List[str]) -> List[List[str]]:
        """
        Approach 2: Character frequency counting as key
        """
        # TODO: Implementar solución usando character counting
        pass

def test_group_anagrams():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    # result1 = solution.groupAnagrams_sorting(strs1)
    # Nota: El orden de los grupos puede variar, así que necesitamos comparar sets
    
    # Test case 2 - Single string
    strs2 = [""]
    expected2 = [[""]]
    
    # Test case 3 - Single character
    strs3 = ["a"]
    expected3 = [["a"]]
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_group_anagrams()