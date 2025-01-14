class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        
        lst = []
        for key, val in freq.items():
            lst.append((key, val))
        
        lst.sort(key=lambda x: (-x[1], x[0]))
        ans = [lst[i][0] for i in range(k)]
        return ans