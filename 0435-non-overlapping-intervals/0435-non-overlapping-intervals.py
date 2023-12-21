class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        firstIntEnd = intervals[0][1] # original end value

        for start, end in intervals[1:]:
            if start >= firstIntEnd:
                firstIntEnd = end
            else:
                count += 1 # because we will have to remove the interval otherwise
                firstIntEnd = min(end, firstIntEnd)
        return count