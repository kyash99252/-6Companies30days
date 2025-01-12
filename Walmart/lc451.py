class Solution:
    def frequencySort(self, s: str) -> str:
        mpp = {}
        for ch in s:
            mpp[ch] = mpp.get(ch, 0) + 1
        
        ls = sorted(list(s), key=lambda x: (-mpp[x], ord('a') - ord(x)))
        return ''.join(ls)