class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height)-1

        while left <= right:
            area1 = (right - left) * min(height[left], height[right])
            area = max(area, area1)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area