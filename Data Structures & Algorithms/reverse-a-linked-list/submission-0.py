# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        curr = head
        previousNode = None
        while (curr != None):

            next_ = curr.next
            curr.next = previousNode
            previousNode = curr
            curr = next_

        return previousNode
        