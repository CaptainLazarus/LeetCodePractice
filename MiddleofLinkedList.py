# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head
        
        while node.next:
            arr.append(node)
            node = node.next
        arr.append(node)
        return arr[len(arr)//2]