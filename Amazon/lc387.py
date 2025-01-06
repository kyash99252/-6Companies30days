class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        mpp = {}
        for ch in s:
            if ch in mpp:
                mpp[ch] += 1
            else:
                mpp[ch] = 1
        
        for i in range(n):
            if mpp[s[i]] == 1:
                return i
        
        return -1