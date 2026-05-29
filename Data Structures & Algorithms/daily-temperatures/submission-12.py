class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < v:
                popped = stack.pop()
                result[popped[0]] = i - popped[0]
            stack.append([i,v])
        return result