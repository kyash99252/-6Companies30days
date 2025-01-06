class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        if source == target:
            return 0
        n = len(cost)
        min_cost = [[float('inf')] * 26 for _ in range(26)]
        for i in range(n):
            min_cost[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = min(min_cost[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')], cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if i == j:
                        min_cost[i][j] = 0
                    else:
                        via = min_cost[i][k] + min_cost[k][j]
                        min_cost[i][j] = min(min_cost[i][j], via)

        m = len(source)
        total_cost = 0
        for i in range(m):
            if source[i] != target[i]:
                if min_cost[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == float('inf'):
                    return -1
                total_cost += min_cost[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
        return total_cost