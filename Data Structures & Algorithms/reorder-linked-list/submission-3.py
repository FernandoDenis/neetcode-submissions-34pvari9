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

        curr1, curr2 = head, prev
        #           c  t         c  t 
        # [0, 1, 2, 3,] [6, 5, 4]
        # 0 6 1 5 2 4 3
        # c c
        while curr1 and curr2:
            temp1, temp2 = curr1.next, curr2.next 
            curr1.next = curr2
            curr2.next = temp1
            curr1 = temp1
            curr2 = temp2

        return 


            




        