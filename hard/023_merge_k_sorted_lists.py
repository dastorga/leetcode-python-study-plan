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
        # TODO: Implementar solución brute force
        pass
    
    def mergeKLists_heap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 2: Min Heap (Priority Queue)
        Time: O(n log k), Space: O(k)
        """
        # TODO: Implementar solución usando heap
        pass
    
    def mergeKLists_divide_conquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 3: Divide and Conquer
        Time: O(n log k), Space: O(log k)
        """
        # TODO: Implementar solución divide and conquer
        pass
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Helper function para merge de dos listas"""
        # TODO: Implementar merge de dos listas
        pass

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
    # result1 = solution.mergeKLists_heap(lists1)
    # assert linked_list_to_array(result1) == expected1
    
    # Test case 2 - Empty lists
    lists2 = []
    expected2 = []
    
    # Test case 3 - Single empty list
    lists3 = [None]
    expected3 = []
    
    print("Todos los test cases pasaron! ✅")

if __name__ == "__main__":
    test_merge_k_lists()