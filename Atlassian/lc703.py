class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        k = self.k
        if not self.nums:
            self.nums.append(val)
            return val
        lo, hi = 0, len(self.nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.nums[mid] < val:
                hi = mid - 1
            else:
                lo = mid + 1
        self.nums.insert(lo, val)
        return self.nums[k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)