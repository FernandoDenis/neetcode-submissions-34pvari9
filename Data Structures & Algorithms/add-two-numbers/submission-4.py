# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()
        carry = 0

        while l1 and l2:
            addition = l1.val + l2.val

            if carry != 0:
                addition += carry
                carry = 0

            carry = addition // 10
            addition = addition % 10

            cur.next = ListNode(addition)
            cur = cur.next

            l1 = l1.next
            l2 = l2.next

        nums = None

        if l1:
            nums = l1
        if l2:
            nums = l2

        while nums:
            addition = nums.val

            if carry != 0:
                addition += carry
                carry = 0

            carry = addition // 10
            addition = addition % 10

            cur.next = ListNode(addition)
            cur = cur.next

            nums = nums.next

        if carry != 0:
            cur.next = ListNode(carry)
        
        return head.next

        