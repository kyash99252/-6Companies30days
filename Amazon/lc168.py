class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column = []
        while columnNumber:
            columnNumber -= 1
            rem = columnNumber % 26
            column.append(chr(rem + ord('A')))
            columnNumber //= 26
        column = ''.join(column[::-1])
        return column