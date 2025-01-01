class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        smooth_img = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                summ = 0
                cells = 0
                for k in range(max(0, i - 1), min(n, i + 2)):
                    for l in range(max(0, j - 1), min(m, j + 2)):
                        summ += img[k][l]
                        cells += 1
                smooth_img[i][j] = summ // cells
        return smooth_img