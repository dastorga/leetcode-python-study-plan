"""
LeetCode #21: Merge Two Sorted Lists
Dificultad: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Problema:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Conceptos clave:
- Linked Lists
- Two Pointers
- Recursion vs Iteration
- Time complexity: O(n + m)
- Space complexity: O(1) iterative, O(n + m) recursive

Ejemplo:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists_iterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 1: Iterative solution
        """
        # Create a dummy node to simplify the logic
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes from either list
        current.next = list1 or list2
        
        return dummy.next
    
    def mergeTwoLists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 2: Recursive solution
        """
        # Base cases
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursive case: choose the smaller head and recurse
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2

def create_linked_list(values):
    """Helper function para crear linked list desde array"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Helper function para convertir linked list a array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_merge_two_lists():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    expected1 = [1, 1, 2, 3, 4, 4]
    result1 = solution.mergeTwoLists_iterative(list1, list2)
    assert linked_list_to_array(result1) == expected1
    
    # Test case 2 - Empty lists
    list3 = create_linked_list([])
    list4 = create_linked_list([])
    expected2 = []
    result2 = solution.mergeTwoLists_iterative(list3, list4)
    assert linked_list_to_array(result2) == expected2
    
    # Test case 3 - One empty list
    list5 = create_linked_list([])
    list6 = create_linked_list([0])
    expected3 = [0]
    result3 = solution.mergeTwoLists_iterative(list5, list6)
    assert linked_list_to_array(result3) == expected3
    
    # Test case 4 - Test recursive solution
    list7 = create_linked_list([1, 2, 4])
    list8 = create_linked_list([1, 3, 4])
    result4 = solution.mergeTwoLists_recursive(list7, list8)
    assert linked_list_to_array(result4) == expected1
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_merge_two_lists()


#     Lógica:

# Mientras ambas listas tengan nodos (list1 and list2)
# Comparamos los valores actuales de ambas listas
# Conectamos el nodo menor a nuestra lista resultado
# Avanzamos el puntero de la lista de donde tomamos el nodo
# Avanzamos current para apuntar al último nodo añadido

#  ***** Ejemplo Visual ****
# Inicial:
# list1: 1 -> 2 -> 4 -> None
# list2: 1 -> 3 -> 4 -> None
# dummy: 0 -> None
# current: ^

# Iteración 1: Comparar 1 vs 1 (iguales, tomamos de list1)
# list1:      2 -> 4 -> None
# list2: 1 -> 3 -> 4 -> None  
# dummy: 0 -> 1 -> None
# current:    ^

# Iteración 2: Comparar 2 vs 1 (1 < 2, tomamos de list2)
# list1: 2 -> 4 -> None
# list2:      3 -> 4 -> None
# dummy: 0 -> 1 -> 1 -> None
# current:         ^

# Iteración 3: Comparar 2 vs 3 (2 < 3, tomamos de list1)
# list1:           4 -> None
# list2: 3 -> 4 -> None
# dummy: 0 -> 1 -> 1 -> 2 -> None
# current:              ^

# Iteración 4: Comparar 4 vs 3 (3 < 4, tomamos de list2)
# list1: 4 -> None
# list2:      4 -> None
# dummy: 0 -> 1 -> 1 -> 2 -> 3 -> None
# current:                   ^

# Iteración 5: Comparar 4 vs 4 (iguales, tomamos de list1)
# list1:      None
# list2: 4 -> None
# dummy: 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> None
# current:                        ^

# Fin del bucle: list1 = None, pero list2 = 4 -> None
# Conectamos los restantes:
# dummy: 0 -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

# Resultado final: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None