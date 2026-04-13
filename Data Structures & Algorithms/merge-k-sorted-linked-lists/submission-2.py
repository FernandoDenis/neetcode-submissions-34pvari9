# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # [[1,2,4],[1,3,5],[3,6]]
        #
        if not lists:
            return None

        minHeap = []

        i = 0
        for node in lists:
            minHeap.append((node.val, i, node))
            i += 1

        heapq.heapify(minHeap)

        head = curr = ListNode()

        # -> 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6
        while minHeap:

            val, i, node = heapq.heappop(minHeap)

            curr.next = ListNode(val)
            curr = curr.next

            if node.next:
                node = node.next
                heapq.heappush(minHeap, (node.val, i, node))

        return head.next


        
        