class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        def backtrack(combination, remaining_sum, start_num):
            if len(combination) == k:
                if remaining_sum == 0:
                    result.append(combination[:])
                return

            if remaining_sum < 0:
                return

            for i in range(start_num, 10):
                combination.append(i)
                backtrack(combination, remaining_sum - i, i + 1)
                combination.pop()

        backtrack([], n, 1)
        return result