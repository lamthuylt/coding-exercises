"""
In a given grid, each cell can have one of three values:
* the value 0 representing an empty cell;
* the value 1 representing a fresh orange;
* the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:
* 1 <= grid.length <= 10
* 1 <= grid[0].length <= 10
* grid[i][j] is only 0, 1, or 2.
"""


def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def rotting_one_minute(grid):
        new_grid = [row[:] for row in grid]
        Ny = len(grid)
        Nx = len(grid[0])
        for y in range(Ny):
            for x in range(Nx):
                if grid[y][x]==2:
                    if x-1>=0 and x-1<Nx and y>=0 and y<Ny: # left
                        if grid[y][x-1] == 1:                        
                            new_grid[y][x-1] = 2
                    if x+1>=0 and x+1<Nx and y>=0 and y<Ny: # right
                        if grid[y][x+1] == 1:                        
                            new_grid[y][x+1] = 2
                    if x>=0 and x<Nx and y-1>=0 and y-1<Ny: # up
                        if grid[y-1][x] == 1:                        
                            new_grid[y-1][x] = 2
                    if x>=0 and x<Nx and y+1>=0 and y+1<Ny: # down
                        if grid[y+1][x] == 1:                                                
                            new_grid[y+1][x] = 2                            
        return new_grid             


    minute = 0   
    # if there are already no fresh oranges at minute 0, the answer is just 0
    if [val for row in grid for val in row].count(1) == 0:
        return 0
    # otherwise, repeat the rotting process until all fresh oranges adjacent to rotten oranges have become rotten
    else:    
        while rotting_one_minute(grid) != grid:
            grid = rotting_one_minute(grid)          
            minute += 1
        # if there are no fresh orange left, return minute
        if [val for row in grid for val in row].count(1) == 0:
            return minute
        # if there are still fresh oranges in the grid, return -1
        else:
            return -1
        
        
    
if __name__ == '__main__':
    print('Test 1: {}'.format(orangesRotting([[2,1,1],[1,1,0],[0,1,1]])))
    print('Test 2: {}'.format(orangesRotting([[2,1,1],[0,1,1],[1,0,1]])))
    print('Test 3: {}'.format(orangesRotting([[0,2]])))
    


