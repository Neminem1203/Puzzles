'''
Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether
each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.
'''
connected = True  # the value to find whether the nodes are connected
debug = True

def diffColors(adjMatrix, k):
    nodes = len(adjMatrix) # number of nodes
    if debug: # prints the Adjancency Matrix
        print("Adjacency Matrix")
        for x in adjMat:
            print(x)
        print()
    if k >= nodes: # if k is greater than or equal to the number of nodes, it's definitely True
        return connected
    elif k == 1 and nodes > 1: # if k is 1 and there's more than 1 node, then it's definitely False
        return not connected
    connection = [[] for x in range(nodes)]
    for i in range(nodes):
        for j in range(nodes):
            if adjMatrix[i][j] == connected:
                connection[i] += [j]
    if debug: print(connection)
    for i in range(nodes):
        # only check if there's more than 1 node connected to this node
        if(len(connection[i]) <= 2):
            continue
        # makes a copy of connection at index i
        similarity = []
        for x in connection[i]:
            similarity += [x]
        # check for well connectedness
        for x in connection[i]:
            # we don't need to check x if it's == to i because they're the same
            if(x == i):
                continue
            # go through the similarity list to see how well connected it is
            ind = 0
            end = len(similarity)
            # convoluted loop for a dynamic array
            while(ind < end):
                if(similarity[ind] not in connection[x]):
                    # remove the nodes that are not well connected
                    similarity = similarity[:ind] + similarity[ind+1:]
                    end -= 1
                    continue
                ind += 1

        if debug: print("Well Connectedness of", i, ":",similarity)
        # the amount of well connectedness is how many colors are required for this node
        if len(similarity) > k:
            return (not connected)
    return connected

'''
                0
                |
                |
                |
            1---2   4
                |  /|
                | / |
                |/  |
                3---5
'''

numNodes = 6
adjMat = [[not connected for y in range(numNodes)] for x in range(numNodes)]
# all nodes are connected to themselves
for x in range(numNodes):
    adjMat[x][x] = connected
# These are the edges
connectedNodes = [[0,2], [1,2], [2,3], [3,4], [3,5], [4,5]]
# Settings the edges connected
for i in connectedNodes:
    adjMat[i[0]][i[1]] = connected
    adjMat[i[1]][i[0]] = connected

print(diffColors(adjMat, 2))
