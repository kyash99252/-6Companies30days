from typing import List
from collections import defaultdict, deque

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if len(s) < 10:
            return []
        else:
            sequences = defaultdict(int)
            right = 10
            sequences[s[:right]] += 1
            ls = deque(s[:right])

            while right < n:
                ls.popleft()
                ls.append(s[right])
                sequences[''.join(ls)] += 1
                right += 1

            ans = []
            for string, freq in sequences.items():
                if freq > 1:
                    ans.append(string)
            
            return ans