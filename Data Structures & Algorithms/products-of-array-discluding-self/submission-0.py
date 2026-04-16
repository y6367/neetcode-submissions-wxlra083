class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = list()
        for num in nums:
            newList = list(nums)
            newList.remove(num)
            total = newList.pop(0)
            for newNum in newList:
                total *= newNum
            result.append(total)
        return result