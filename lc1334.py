class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        shortest_dist = [[float('inf')] * n for _ in range(n)]
        min_cities_no = float('inf')
        min_city = -1

        for i in range(n):
            shortest_dist[i][i] = 0
        
        for edge in edges:
            src, dst = edge[0], edge[1]
            wt = edge[2]
            shortest_dist[src][dst] = min(shortest_dist[src][dst], wt)
            shortest_dist[dst][src] = min(shortest_dist[dst][src], wt)
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    via = shortest_dist[i][k] + shortest_dist[k][j]
                    shortest_dist[i][j] = min(shortest_dist[i][j], via)
        
        for city in range(n):
            count = 0
            for city_dist in shortest_dist[city]:
                if city_dist <= distanceThreshold:
                    count += 1
            if count <= min_cities_no:
                min_city = city
                min_cities_no = count
        
        return min_city