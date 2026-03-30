# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return 

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev
        curr = head
        # [0, 1, 2, 3]    [6, 5 ,4]
        # 0 6 5
        while curr and second:
            temp1,temp2 = curr.next, second.next
            curr.next = second
            second.next = temp1
            curr = temp1
            second = temp2

        return 

        

            




        