class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsS = set(nums)
        longest = 0
        for num in numsS:
            count = 1
            curr = num
            while curr + 1 in numsS:
                count += 1
                curr += 1
            if count > longest:
                longest = count
        return longest
        