class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            count = 1
            curr = num
            while curr + 1 in nums:
                count += 1
                curr += 1
            if count > longest:
                longest = count
        return longest
        