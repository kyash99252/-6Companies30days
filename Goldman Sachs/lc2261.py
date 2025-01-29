class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        n = len(nums)
        distinct_subarrays = set()

        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    count += 1
                if count <= k:
                    distinct_subarrays.add(tuple(nums[i:j+1]))

        return len(distinct_subarrays)