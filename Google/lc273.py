class Solution:
    def __init__(self):
        self.belowTen = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.belowTwenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tenMultiple = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num: int) -> str:
        if num >= 10**9:
            st = str(num)
            bil = int(st[0])
            rst = int(st[1:])
            if rst == 0:
                return self.belowTen[bil] + " Billion"
            else:
                return self.belowTen[bil] + " Billion " + self.numberToWords(rst)
        elif num >= 10**6:
            st = str(num)
            mil = int(st[:-6])
            rst = int(st[-6:])
            if rst == 0:
                return self.numberToWords(mil) + " Million"
            else:
                return self.numberToWords(mil) + " Million " + self.numberToWords(rst)
        elif num >= 10**3:
            st = str(num)
            thd = int(st[:-3])
            rst = int(st[-3:])
            if rst == 0:
                return self.numberToWords(thd) + " Thousand"
            else:
                return self.numberToWords(thd) + " Thousand " + self.numberToWords(rst)
        elif num >= 10**2:
            st = str(num)
            hun = int(st[0])
            rst = int(st[1:])
            if rst == 0:
                return self.belowTen[hun] + " Hundred"
            else:
                return self.belowTen[hun] + " Hundred " + self.numberToWords(rst)
        elif 11 <= num <= 19:
            return self.belowTwenty[num - 10]
        elif num in range(10, 100, 10):
            return self.tenMultiple[num // 10] 
        elif num in range(10, 100):
            return self.tenMultiple[num // 10] + " " + self.belowTen[num % 10]
        else:
            return self.belowTen[num]