'''
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''



# normal mode
normal = [  ['f', 'f', 'f', 'f'],
            ['t', 't', 'f', 't'],
            ['f', 'f', 'f', 'f'],
            ['f', 'f', 'f', 'f']]
# answer = 7
normalStart = [3,0]
normalEnd = [0,0]

# hard mode
long = [    ['f','f','f','f','f','f','f','f','f'],
            ['t','t','t','t','t','t','t','t','f'],
            ['f','f','f','t','f','f','f','t','f'],
            ['f','t','f','t','f','t','f','t','f'],
            ['f','t','f','f','f','t','f','f','f']]
# answer = 28
longStart = [4,0]
longEnd = [0,0]


def dfs(maze,start, end):
    width = len(maze[0])
    height = len(maze)
    start.append(0)
    listOfPos = [start]
    while(listOfPos):
        # print(listOfPos)
        thisPos = listOfPos.pop(0)
        maze[thisPos[0]][thisPos[1]] = 't'
        if(abs(thisPos[0] - end[0]) + abs(thisPos[1] - end[1]) == 1):
            return thisPos[2]+1
        if thisPos[0]-1 >= 0 and maze[thisPos[0] - 1][ thisPos[1]] == 'f':
            listOfPos.append([thisPos[0] - 1, thisPos[1], thisPos[2] + 1])
            # maze[thisPos[0] - 1][thisPos[1]] = 't'
        if thisPos[0]+1 < height and maze[thisPos[0] + 1][ thisPos[1]] == 'f':
            listOfPos.append([thisPos[0] + 1, thisPos[1], thisPos[2] + 1])
            # maze[thisPos[0] + 1][thisPos[1]] = 't'

        if thisPos[1]-1 >= 0 and maze[thisPos[0]][ thisPos[1] - 1] == 'f':
            listOfPos.append([thisPos[0], thisPos[1] - 1, thisPos[2] + 1])
            # maze[thisPos[0]][thisPos[1] - 1] = 't'
        if thisPos[1]+1 < width and maze[thisPos[0]][ thisPos[1] + 1] == 'f':
            listOfPos.append([thisPos[0], thisPos[1] + 1, thisPos[2] + 1])
            # maze[thisPos[0]][thisPos[1] + 1] = 't'
    return None

print(dfs(normal, normalStart, normalEnd))
print(dfs(long, longStart, longEnd))