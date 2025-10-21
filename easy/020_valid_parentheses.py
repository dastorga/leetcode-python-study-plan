"""
LeetCode #20: Valid Parentheses
Dificultad: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Problema:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

Conceptos clave:
- Stack (LIFO)
- String manipulation
- Pattern matching
- Time complexity: O(n)
- Space complexity: O(n)

Ejemplo:
Input: s = "()[]{}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach: Stack-based solution
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:  # opening bracket
                stack.append(char)
        
        return len(stack) == 0
    
def test_valid_parentheses():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1 - Valid
    s1 = "()"
    expected1 = True
    result1 = solution.isValid(s1)
    assert result1 == expected1, f"Expected {expected1}, got {result1}"
    
    # Test case 2 - Valid
    s2 = "()[]{}"
    expected2 = True
    result2 = solution.isValid(s2)
    assert result2 == expected2, f"Expected {expected2}, got {result2}"
    
    # Test case 3 - Invalid
    s3 = "(]"
    expected3 = False
    result3 = solution.isValid(s3)
    assert result3 == expected3, f"Expected {expected3}, got {result3}"
    
    # Test case 4 - Edge case empty
    s4 = ""
    expected4 = True
    result4 = solution.isValid(s4)
    assert result4 == expected4, f"Expected {expected4}, got {result4}"
    
    # Test case 5 - Invalid order
    s5 = "([)]"
    expected5 = False
    result5 = solution.isValid(s5)
    assert result5 == expected5, f"Expected {expected5}, got {result5}"
    
    print("Todos los test cases pasaron! ✅")


    # Stack (LIFO): Para rastrear paréntesis abiertos
    # Hash Table: Mapeo de paréntesis de cierre a apertura
    # String manipulation: Procesamiento carácter por carácter
    # Pattern matching: Validación de patrones válidos


if __name__ == "__main__":
    test_valid_parentheses()