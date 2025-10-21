"""
LeetCode #23: Merge k Sorted Lists
Dificultad: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Problema:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Conceptos clave:
- Heap (Priority Queue)
- Divide and Conquer
- Linked Lists
- Multiple merge strategies
- Time complexity: O(n log k) where n is total nodes and k is number of lists
- Space complexity: O(k) for heap, O(log k) for divide and conquer

Ejemplo:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
"""

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists_bruteforce(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 1: Brute Force - Collect all values and sort
        Time: O(n log n), Space: O(n)
        """
        values = []
        for head in lists:
            current = head
            while current:
                values.append(current.val)
                current = current.next
        
        values.sort()
        
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
    
    def mergeKLists_heap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 2: Min Heap (Priority Queue)
        Time: O(n log k), Space: O(k)
        """
        heap = []
        
        # Initialize heap with first node of each list
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, list_idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        return dummy.next
    
    def mergeKLists_divide_conquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 3: Divide and Conquer
        Time: O(n log k), Space: O(log k)
        """
        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists
        
        return lists[0]
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Helper function para merge de dos listas"""
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 or l2
        return dummy.next

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

def test_merge_k_lists():
    """Test cases para validar la solución"""
    solution = Solution()
    
    # Test case 1
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]
    
    # Test brute force
    result1_bf = solution.mergeKLists_bruteforce(lists1)
    print(f"Brute Force result: {linked_list_to_array(result1_bf)}")
    assert linked_list_to_array(result1_bf) == expected1
    
    # Recreate lists for heap test
    lists1_heap = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result1_heap = solution.mergeKLists_heap(lists1_heap)
    print(f"Heap result: {linked_list_to_array(result1_heap)}")
    assert linked_list_to_array(result1_heap) == expected1
    
    # Recreate lists for divide and conquer test
    lists1_dc = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result1_dc = solution.mergeKLists_divide_conquer(lists1_dc)
    print(f"Divide & Conquer result: {linked_list_to_array(result1_dc)}")
    assert linked_list_to_array(result1_dc) == expected1
    
    # Test case 2 - Empty lists
    lists2 = []
    expected2 = []
    result2 = solution.mergeKLists_heap(lists2)
    assert linked_list_to_array(result2) == expected2
    
    # Test case 3 - Single empty list
    lists3 = [None]
    expected3 = []
    result3 = solution.mergeKLists_heap(lists3)
    assert linked_list_to_array(result3) == expected3
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_merge_k_lists()




# Complejidad de las soluciones:
    # Brute Force (O(n log n))
    # Min Heap (O(n log k))
    # Divide and Conquer (O(n log k))



# Logica de Brute Force
# Input: [[1,4,5], [1,3,4], [2,6]]
# Después de este paso: values = [1,4,5,1,3,4,2,6]

# Paso 2: Ordenar todos los valores
    # values.sort()
    # Usa el algoritmo de ordenamiento de Python (Timsort)
    # Ordena todos los valores en orden ascendente

# Paso 3: Crear una nueva lista enlazada ordenada
    # dummy = ListNode(0)
    # current = dummy
    # for val in values:
    #     current.next = ListNode(val)
    #     current = current.next

    # return dummy.next


    # Ventajas:
    #     Fácil de entender e implementar
    #     Funciona correctamente para cualquier entrada
    #     No requiere conocimientos avanzados de estructuras de datos




#  ***** Enfoque Min Heap *****
# 🔄 Visualización completa del proceso:

# Input: [[1,4,5], [1,3,4], [2,6]]

# Estado inicial del heap:
# [(1,0,Node), (1,1,Node), (2,2,Node)]

# Iteración 1: Pop (1,0) → Resultado: [1]
# Heap: [(1,1,Node), (2,2,Node), (4,0,Node)]

# Iteración 2: Pop (1,1) → Resultado: [1,1]
# Heap: [(2,2,Node), (4,0,Node), (3,1,Node)]

# Iteración 3: Pop (2,2) → Resultado: [1,1,2]
# Heap: [(3,1,Node), (4,0,Node), (6,2,Node)]

# Iteración 4: Pop (3,1) → Resultado: [1,1,2,3]
# Heap: [(4,0,Node), (6,2,Node), (4,1,Node)]

# Iteración 5: Pop (4,0) → Resultado: [1,1,2,3,4]
# Heap: [(4,1,Node), (6,2,Node), (5,0,Node)]

# Iteración 6: Pop (4,1) → Resultado: [1,1,2,3,4,4]
# Heap: [(5,0,Node), (6,2,Node)]

# Iteración 7: Pop (5,0) → Resultado: [1,1,2,3,4,4,5]
# Heap: [(6,2,Node)]

# Iteración 8: Pop (6,2) → Resultado: [1,1,2,3,4,4,5,6]
# Heap: []

# Final: [1,1,2,3,4,4,5,6]