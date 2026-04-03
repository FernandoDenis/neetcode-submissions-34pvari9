# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #    p d   c
        #  1,2,3,4
        curr = head
        for i in range(n):
            curr = curr.next

        delNode = head
        previous = ListNode(next = head)
        returnNode = previous
        while curr:
            previous = delNode
            curr = curr.next
            delNode = delNode.next

        if previous.next:
            previous.next = previous.next.next

        return returnNode.next

        

        