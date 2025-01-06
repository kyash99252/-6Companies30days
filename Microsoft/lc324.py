class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        mid = (len(nums) + 1) // 2
        j, k = mid - 1, len(nums) - 1
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = sorted_nums[j]
                j -= 1
            else:
                nums[i] = sorted_nums[k]
                k -= 1