# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #                c
    # 1 -> 2 -> 3 -> 4 ->
    #                t
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        curr = head
        two_steps_curr = head

        while two_steps_curr and two_steps_curr.next:
            curr = curr.next
            two_steps_curr = two_steps_curr.next.next

            if curr == two_steps_curr:
                return True

        return False
        