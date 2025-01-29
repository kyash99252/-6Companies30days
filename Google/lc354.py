class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        return self.lengthOfLIS(heights)
    
    def lengthOfLIS(self, nums: list[int]) -> int:
        from bisect import bisect_left
        lis = []
        for num in nums:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num
        return len(lis)