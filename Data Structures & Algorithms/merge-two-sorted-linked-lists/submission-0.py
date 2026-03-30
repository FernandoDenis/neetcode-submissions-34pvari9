# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #               m    t
        # 1-> 2 -> 3 -> 4 -> 5
        #     max
        #  4 ->

        if not list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        
        if list1.val <= list2.val:
            minNode = list1
            maxNode = list2
        else:
            minNode = list2
            maxNode = list1

        head = minNode
        temp = minNode.next

        while temp and maxNode:
            if temp.val <= maxNode.val:
                minNode = temp
                temp = temp.next
            else:
                minNode.next = maxNode
                maxNode = maxNode.next
                minNode = minNode.next
                minNode.next = temp

        if temp:
            minNode.next = temp

        if maxNode:
            minNode.next = maxNode

        return head

        


        