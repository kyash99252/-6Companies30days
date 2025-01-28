from math import lcm

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, count1: int, count2: int) -> int:
        ceil_div_2 = lambda x: (x + abs(x)) // 2
        low, prev_count, common_multiple = count1 + count2, 0, lcm(divisor1, divisor2)

        while low > prev_count:
            prev_count = low
            len_group1, len_group2 = low // divisor2 - low // common_multiple, low // divisor1 - low // common_multiple
            low += ceil_div_2(ceil_div_2(count1 - len_group1) + ceil_div_2(count2 - len_group2) - low + low // common_multiple + len_group2 + len_group1)

        return low