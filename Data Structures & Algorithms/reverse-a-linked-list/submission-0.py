# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        root = self.reverseList(head.next)
        pointer = root
        while pointer.next is not None:
            pointer = pointer.next
        head.next = None
        pointer.next = head

        return root