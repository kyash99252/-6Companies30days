class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        ans = idx = 0
        for i in range(len(g)):
            if idx < len(s) and g[i] > s[idx]:
                while idx < len(s) and g[i] > s[idx]:
                    idx += 1
            if idx < len(s) and g[i] <= s[idx]:
                idx += 1
                ans += 1
            if idx == len(s):
                break
        
        return ans