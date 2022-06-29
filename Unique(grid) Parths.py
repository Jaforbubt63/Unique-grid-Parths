
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for _ in range(n):
            grid.append([0] * n)
            
        for i in range(n):
            grid[m-1][1] = 1
            
        for j in range(m):
            grid[j][n-1] = 1
            
        for j in range(m-2, -1, -1):
            for i in range(n-2, -1, -1):
                grid[j][i] = grid[j+1][i] = grid[j][i+1]
                
        return grid[0][0]