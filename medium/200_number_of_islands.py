"""
LeetCode #200: Number of Islands
Dificultad: Medium
Link: https://leetcode.com/problems/number-of-islands/

Problema:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

Conceptos clave:
- Graph traversal
- DFS (Depth-First Search)
- BFS (Breadth-First Search)
- Matrix manipulation
- Connected components
- Time complexity: O(m * n)
- Space complexity: O(m * n) worst case

Ejemplo:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

from typing import List
from collections import deque

class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        """
        Approach 1: DFS (Depth-First Search)
        """
        # TODO: Implementar solución usando DFS
        pass
    
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        """
        Approach 2: BFS (Breadth-First Search)
        """
        # TODO: Implementar solución usando BFS
        pass
    
    def numIslands_union_find(self, grid: List[List[str]]) -> int:
        """
        Approach 3: Union Find (Disjoint Set)
        """
        # TODO: Implementar solución usando Union Find
        pass

def test_number_of_islands():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    expected1 = 1
    # result1 = solution.numIslands_dfs(grid1)
    # assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    expected2 = 3
    
    # Test case 3 - Single cell
    grid3 = [["1"]]
    expected3 = 1
    
    # Test case 4 - No islands
    grid4 = [["0"]]
    expected4 = 0
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_number_of_islands()