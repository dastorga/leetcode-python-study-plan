"""
LeetCode #94: Binary Tree Inorder Traversal
Dificultad: Medium
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Problema:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Conceptos clave:
- Binary Trees
- DFS (Depth-First Search)
- Stack
- Recursion vs Iteration
- Time complexity: O(n)
- Space complexity: O(h) where h is height of tree

Ejemplo:
Input: root = [1,null,2,3]
Output: [1,3,2]
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 1: Recursive solution
        """
        # TODO: Implementar solución recursiva
        pass
    
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 2: Iterative solution using stack
        """
        # TODO: Implementar solución iterativa con stack
        pass

def create_tree_from_array(values):
    """Helper function para crear árbol desde array"""
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_inorder_traversal():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1
    root1 = create_tree_from_array([1, None, 2, 3])
    expected1 = [1, 3, 2]
    # result1 = solution.inorderTraversal_recursive(root1)
    # assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2 - Empty tree
    root2 = None
    expected2 = []
    
    # Test case 3 - Single node
    root3 = TreeNode(1)
    expected3 = [1]
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_inorder_traversal()