# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [[2],[1][3]] m * k
# 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        minHeap = []
        heapq.heapify(minHeap)
        i = 0

        for node in lists:
            i += 1
            if node:
                print(node.val)
                heapq.heappush(minHeap,(node.val, i, node))

        newList = ListNode()
        curr = newList

        while minHeap:
            _, idx, node = heapq.heappop(minHeap)
            temp = node.next

            curr.next = node
            curr = curr.next
            curr.next = None

            if temp:
                heapq.heappush(minHeap, (temp.val, idx, temp))

        return newList.next

        