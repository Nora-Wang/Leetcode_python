There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.


用一个二维数组存取start到每个点到distance + BFS

code:
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not len(maze) or not len(maze[0]):
            return -1
        
        #corner case
        if start == destination:
            return 0
        
        queue = collections.deque([(start)])
        #用一个二维数组distance记录maze中的每个点到start的距离
        distance = [[sys.maxsize for i in range(len(maze[0]))] for j in range(len(maze))]
        distance[start[0]][start[1]] = 0
        
        while queue:
            x,y = queue.popleft()
            #四个方向
            for direct in DIRECTIONS:
                count = distance[x][y]
                x_, y_ = x, y
                
                #注意这里的写法,因为想要最后得到的x_,y_为停下的点,而不是墙/超出范围,因此在判断是否valid的时候是用的x_ + direct[0], y_ + direct[1]
                while self.is_valid(maze, x_ + direct[0], y_ + direct[1]):
                    x_ += direct[0]
                    y_ += direct[1]
                    count += 1
                
                #这里要取最小值,因为判断这一次起点到该点是不是最短路程,如果是再加入队列中,更新该点值 
                #如果是第一次到该点，则一定小于极大值
                if count < distance[x_][y_]:
                    distance[x_][y_] = count
                    queue.append((x_,y_))

        #如果终点的distance为sys.maxsize,则说明从起点无法到达终点,因此返回-1
        if distance[destination[0]][destination[1]] == sys.maxsize:
            return -1
        return distance[destination[0]][destination[1]]
                
    
    def is_valid(self, maze, x, y):
        if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
            return False
        
        if maze[x][y] == 1:
            return False
        
        return True
                


