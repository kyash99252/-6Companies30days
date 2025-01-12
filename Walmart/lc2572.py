import math

class Solution:
    def squareFreeSubsets(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        primes = set([2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30])
        prime_factors = {}
        for num in nums:
            if num in primes:
                prime_factors[num] = prime_factors.get(num, 0) + 1
        def foo(_set):
            if not _set:
                return 1
            current_set = []
            for num in _set[1:]:
                if math.gcd(num, _set[0]) == 1:
                    current_set.append(num)
            
            return (foo(_set[1:]) + prime_factors[_set[0]] * foo(current_set)) % MOD
        
        return (foo(list(prime_factors)) * 2 ** nums.count(1) - 1) % MOD