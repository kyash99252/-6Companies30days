class Solution:
    def encode(self, s : str) -> str:
        # code here
        if not s:
            return ""
        
        result = ""
        count = 1
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == s[i+1]:
                count += 1
            else:
                result += s[i] + str(count)
                count = 1
        return result