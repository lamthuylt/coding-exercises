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


#####################
### solution 1 (SLOW)
#####################
def orangesRotting1(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    def rotting_one_minute(grid):
        new_grid = [row[:] for row in grid] # copy by slicing (in Python2) (for Python3, subtitute by list() or copy() function)
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


########################
### solution 2 (QUICKER)
########################
def orangesRotting2(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    minute = 0
    fresh, rotten = set(), set()
    
    # initial fresh and rotten set 
    Ny, Nx = len(grid), len(grid[0])
    for y in range(Ny):
        for x in range(Nx):
            if grid[y][x]==1:
                fresh.add((y,x))
            elif grid[y][x]==2:
                rotten.add((y,x))
    
    # if there are already no fresh oranges at minute 0, the answer is just 0
    while fresh:
        rotten_new = set()
        
        # after one minute rotting
        for (y,x) in rotten:
            rotten_new.add((y,x))
            for dy,dx in [(0,-1), (0,+1), (-1,0), (+1,0)]:
                 if (y+dy,x+dx) in fresh:
                     fresh.remove((y+dy,x+dx))
                     rotten_new.add((y+dy,x+dx))
        
        # if the rotting hasn't end, repeat the process 
        if rotten_new != rotten:
            rotten = rotten_new            
            minute += 1
        # if the rotting ends and there are still fresh oranges in the grid, return -1
        elif fresh:
                return -1
    
    # if there are no fresh oranges left, return minute
    return minute

                
            
   
if __name__ == '__main__':
    print('Test 1: {}'.format(orangesRotting2([[2,1,1],[1,1,0],[0,1,1]])))
    print('Test 2: {}'.format(orangesRotting2([[2,1,1],[0,1,1],[1,0,1]])))
    print('Test 3: {}'.format(orangesRotting2([[0,2]])))
    

