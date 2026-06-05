class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        so_far = 0

        for r in range(len(s)):
            if s[r] in window:
                if len(window) > so_far:
                    so_far = len(window)
                
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
            window.add(s[r])
        
        if len(window) > so_far:
            so_far = len(window)
        return so_far