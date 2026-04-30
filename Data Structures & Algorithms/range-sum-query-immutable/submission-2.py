class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0]
        prev = self.pre[0]
        for num in nums:
            self.pre.append(num+prev)
            prev = self.pre[len(self.pre) - 1]


    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)