class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * nums[i] for i in range(n))
        max_value = f
        
        for i in range(1, n):
            f += total_sum - n * nums[-i]
            max_value = max(max_value, f)
        
        return max_value