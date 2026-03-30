# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = curr = ListNode()
        carry = 0

        while l1 and l2:
            addi = l1.val + l2.val

            if carry != 0:
                addi += carry
                carry = 0
    
            units = addi % 10

            curr.next = ListNode(units)
            curr = curr.next

            carry += addi // 10
            l1 = l1.next
            l2 = l2.next

        nums = None
        if l1:
            nums = l1
        elif l2:
            nums = l2

        while nums:
            addi = carry + nums.val
            units = addi % 10

            curr.next = ListNode(units)

            carry = addi // 10

            curr = curr.next
            nums = nums.next

        if carry != 0:
            curr.next = ListNode(carry)

        return head.next


        