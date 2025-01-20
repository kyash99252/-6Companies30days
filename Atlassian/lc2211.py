class Solution:
    def countCollisions(self, directions: str) -> int:
        res, n, i, carsFromRight = 0, len(directions), 0, 0
        
        while i < n and directions[i] == 'L':
               i+=1
        
        while i<n:
            if directions[i] == 'R':
                carsFromRight+=1
            else:
                res += carsFromRight if directions[i] == 'S' else carsFromRight+1
                carsFromRight = 0
            i+=1
                
        return res