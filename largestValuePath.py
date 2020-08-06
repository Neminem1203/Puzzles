'''
Daily Coding Problem: Problem #72
In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A

[(0, 0)]

Should return null, since we have an infinite loop.
'''

def largestValuePath(str, edgeList):
    def helper(currentEdgeList, current, visited):
        maxList = []
        value = {}
        value[str[current]] = 1
        for ind in visited:
            char = str[ind]
            if char not in value:
                value[char] = 0
            value[char] += 1

        max = 0
        for key in value:
            if max < value[key]:
                    max = value[key]
        maxList += [max]
        if len(currentEdgeList) == 0:
            return max

        # print("currentEdgeList: ",currentEdgeList,"\ncurrent:", current,"\nvisited:", visited,"\nvalue:", value, "\n")
        for edgeInd in range(len(currentEdgeList)):
            frm, to = currentEdgeList[edgeInd]
            if frm == current:
                if to in visited:
                    return None
                val = helper(currentEdgeList[:edgeInd] + currentEdgeList[edgeInd+1:], to, visited + [current])
                if val == None:
                    return None
                maxList += [val]

        largest = 0
        for num in maxList:
            if num > largest:
                largest = num

        return largest






    largest = 0
    for edgeInd in range(len(edgeList)):
        edge = edgeList[edgeInd]
        if edge[0] == edge[1]: # if a node points to itself, it's an infinite loop
            return None
        # print(edgeList[:edgeInd] + edgeList[edgeInd+1:])
        val = helper(edgeList[:edgeInd] + edgeList[edgeInd+1:], edge[1], [edge[0]])
        if val == None: # None means there was an infinite loop deteted
            return None
        if largest < val:
            largest = val
    return largest





print(largestValuePath("ABACA",
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]))

print(largestValuePath("ABCAA", [(0, 1),(0, 2),(0,3),(1,3), (3,2), (4,0)]))