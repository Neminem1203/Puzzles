def remove_islands(matrix):
    height = len(matrix)-1 # last height ind
    width = len(matrix[0])-1 # last width ind
    solution_matrix = [[0 for _ in range(width+1)] for _ in range(height+1)]
    # make the corners 1
    corners = [[0,0], [0, width], [height, 0], [height, width]]
    for x, y in corners:
        if matrix[x][y] == 1:
            solution_matrix[x][y] = 1
    # find all the connected 1s in the top and bottom
    for i in range(1, width):
        possible_islands = [[0,i],[height,i]]
        while len(possible_islands) > 0:
            x, y = possible_islands.pop(0)
            if matrix[x][y] == 1:
                solution_matrix[x][y] = 1
                if x > 0 and matrix[x-1][y] == 1 and solution_matrix[x-1][y] == 0:
                    possible_islands.append([x-1, y])
                if x < width and matrix[x+1][y] == 1 and solution_matrix[x+1][y] == 0:
                    possible_islands.append([x+1, y])

                if y > 0 and matrix[x][y-1] == 1 and solution_matrix[x][y-1] == 0:
                    possible_islands.append([x, y-1])
                if y < height and matrix[x][y+1] == 1 and solution_matrix[x][y+1] == 0:
                    possible_islands.append([x, y+1])
    # find all the connect 1s at the left and right
    for i in range(1, height):
        possible_islands = [[i, 0], [i, width]]
        while len(possible_islands) > 0:
            x, y = possible_islands.pop(0)
            if matrix[x][y] == 1:
                solution_matrix[x][y] = 1
                if x > 0 and matrix[x - 1][y] == 1 and solution_matrix[x - 1][y] == 0:
                    possible_islands.append([x - 1, y])
                if x + 1 < width and matrix[x + 1][y] == 1 and solution_matrix[x + 1][y] == 0:
                    possible_islands.append([x + 1, y])

                if y > 0 and matrix[x][y - 1] == 1 and solution_matrix[x][y - 1] == 0:
                    possible_islands.append([x, y - 1])
                if y + 1 < height and matrix[x][y + 1] == 1 and solution_matrix[x][y + 1] == 0:
                    possible_islands.append([x, y + 1])

    return solution_matrix

test_input = [  [1,0,0,0,0,0],
                [0,1,0,1,1,1],
                [0,0,1,0,1,0],
                [1,1,0,0,1,0],
                [1,0,1,1,0,0],
                [1,0,0,0,0,1],
                ]

solution = [[1,0,0,0,0,0],
            [0,0,0,1,1,1],
            [0,0,0,0,1,0],
            [1,1,0,0,1,0],
            [1,0,0,0,0,0],
            [1,0,0,0,0,1],
            ]

test_output = remove_islands(test_input)
for line in test_output:
    print(line)
print(test_output == solution)