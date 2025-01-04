class Solution:
    def maxProduct(self, s: str) -> int:
        n, palindrome = len(s), {}

        for mask in range(1, 1 << n):
            subseq = ''
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                palindrome[mask] = len(subseq)
        
        res = 0
        for m1 in palindrome:
            for m2 in palindrome:
                if m1 & m2 == 0:
                    res = max(res, palindrome[m1] * palindrome[m2])
        
        return res