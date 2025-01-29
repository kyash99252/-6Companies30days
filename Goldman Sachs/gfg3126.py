class Solution:
    def printMinNumberForPattern(ob,S):
        # code here
        n = len(S)
        result = ""
        num = 1
        stack = []

        for i in range(n):
            stack.append(num)
            num += 1
            if S[i] == 'I':
                while stack:
                    result += str(stack.pop())
        
        stack.append(num)
        while stack:
            result += str(stack.pop())

        return result