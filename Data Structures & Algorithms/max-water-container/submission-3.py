class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0
        while (left < right):
            size = min(heights[left], heights[right]) * (right - left)
            if (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
            if size > result:
                result = size
        return result
        