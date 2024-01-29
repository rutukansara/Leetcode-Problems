class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        difference = 0
        for i in range(len(points)-1):
            difference = max(difference, abs(points[i][0] - points[i+1][0]))
        return difference
            