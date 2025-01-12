class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        n = len(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        stt = set()
        for num in nums:
            can1, can2 = num - k, num + k
            if can1 == can2 == num:
                if freq[num] > 1 and (num, num) not in stt:
                    stt.add((num, num))
            else:
                if (can1 in freq) and ((can1, num) not in stt):
                    stt.add((can1, num))
                if (can2 in freq) and ((num, can2) not in stt):
                    stt.add((num, can2))
        
        return len(stt)