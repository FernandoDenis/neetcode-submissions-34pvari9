# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # None <- 0 <- 1 <- 2 <- 3

        if not head:
            return head

        def reverseLinkedList(prev,act,nxt):
            if not nxt:
                act.next = prev
                return act

            act.next = prev

            root = reverseLinkedList(act,nxt,nxt.next)

            return root

        return reverseLinkedList(None,head,head.next)

                