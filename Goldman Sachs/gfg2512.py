class Solution:
    def findTwoElement(self, arr): 
        # code here
        n = len(arr)
        missing_sum = n * (n + 1) // 2 - sum(arr)
        xor = 0
        for x in arr:
            xor ^= x
        for i in range(1, n + 1):
            xor ^= i
        set_bit = xor & -xor
        x = 0
        y = 0
        for num in arr:
            if num & set_bit:
                x ^= num
            else:
                y ^= num
        for i in range(1, n + 1):
            if i & set_bit:
                x ^= i
            else:
                y ^= i
        if x in arr:
            return [x, y]
        else:
            return [y, x]