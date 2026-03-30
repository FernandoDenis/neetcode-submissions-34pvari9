class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #                 l      r
        # [[1,3],[1,5],[6,7]]
        if len(intervals) <= 1: # 3
            return intervals

        intervals.sort()

        merge_intervals = [] # [[1,5],[6,7]]

        l, r = 0, 1 

        while r < len(intervals): # 1
            if intervals[r][0] <= intervals[l][1]:
                if intervals[l][1] > intervals[r][1]:
                    intervals[r][1] = intervals[l][1]
                    
                intervals[r][0] = intervals[l][0]
                l += 1
                r += 1
            else:
                merge_intervals.append(intervals[l])
                l += 1
                r += 1

        merge_intervals.append(intervals[l])

        return merge_intervals

        