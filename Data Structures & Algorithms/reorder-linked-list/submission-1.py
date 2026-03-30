# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        array = []

        curr = head
        while curr:
            array.append(curr)
            curr = curr.next 

        curr = head
        temp = None
        prev = None
        #  2 8 4 6 None
        #      c
        # [2,4,6,8]
        for i in range(len(array) - 1, (len(array) // 2) - 1, -1): # 8,6
            temp = curr.next
            curr.next = array[i]
            curr.next.next = temp
            prev = curr.next
            curr = curr.next.next

        curr.next = None

        return 