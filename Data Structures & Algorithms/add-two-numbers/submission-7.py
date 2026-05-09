# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #       x
        # 9 9 9
        # 1 1 1 
        
        # 0 1 1 1
        # carry 1

        newList = curr = ListNode()

        carry = 0
        
        while l1 or l2:

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            addition = num1 + num2 + carry

            carry = addition // 10
            addition = addition % 10

            curr.next = ListNode(addition)
            curr = curr.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry:
            curr.next = ListNode(carry)

        return newList.next


            



        