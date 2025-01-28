class Solution:
    def stoneGameVI(self, aliceValues: list[int], bobValues: list[int]) -> int:
        totalValues = sorted(zip(aliceValues, bobValues), key=lambda x: -(x[0] + x[1]))
        aliceScore, bobScore = 0, 0
        for i, (a, b) in enumerate(totalValues):
            if i % 2 == 0:
                aliceScore += a
            else:
                bobScore += b
        return 1 if aliceScore > bobScore else -1 if bobScore > aliceScore else 0