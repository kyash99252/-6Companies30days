class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()

        mhDiff = hDiff = 2
        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i - 1] == 1:
                hDiff += 1
            else:
                hDiff = 2
            mhDiff = max(hDiff, mhDiff)

        mvDiff = vDiff = 2
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i - 1] == 1:
                vDiff += 1
            else:
                vDiff = 2
            mvDiff = max(mvDiff, vDiff)
        
        return min(mhDiff, mvDiff) ** 2