from collections import deque, defaultdict

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: list[list[int]]) -> list[int]:
        def bfs(src, cities):
            visited = {src}
            q = deque([(src, 0)])
            farthestDist = 0
            while q:
                u, d = q.popleft()
                farthestDist = d
                for v in graph[u]:
                    if v not in visited and v in cities:
                        visited.add(v)
                        q.append((v, d+1))
            return farthestDist, visited

        def maxDistance(state):
            cities = set()
            for i in range(n):
                if (state >> i) & 1:
                    cities.add(i)
            if not cities:
                return 0
            ans = 0
            for i in cities:
                farthestDist, visited = bfs(i, cities)
                if len(visited) < len(cities):
                    return 0
                ans = max(ans, farthestDist)
            return ans

        graph = defaultdict(list)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
            
        ans = [0] * (n - 1)
        for state in range(1, 2 ** n):
            d = maxDistance(state)
            if d > 0:
                ans[d - 1] += 1
        return ans