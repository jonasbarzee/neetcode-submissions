# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        node = head
        saved = node.next
        node.next = None
        prev = node
        node = saved
        while node is not None:
            saved = node.next
            node.next = prev
            prev = node
            node = saved

        return prev
        