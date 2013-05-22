# 6.00x Problem Set 10
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    graph = WeightedDigraph()
    nodes = {}
    for line in open(mapFilename, 'r'):
        record = line.split()
        src = record[0]
        if src not in nodes:
            nodes[src] = Node(src)            
            graph.addNode(nodes[src])
        dest = record[1]
        if dest not in nodes:
            nodes[dest] = Node(dest)
            graph.addNode(nodes[dest])
        total = int(record[2])
        outdoors = int(record[3])
        edge = WeightedEdge(nodes[src], nodes[dest], total, outdoors)
        graph.addEdge(edge)
    return graph
        

#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#

def countDistance(digraph, path):
    if  path == None:
        return (0, 0)
    total = 0
    outdoor = 0
    prevNode = path[0]
    for node in path[1:]:
        edges = digraph.childrenOf(Node(prevNode))
        for edge in edges:
            if edge[0] == Node(node):
                t, o = edge[1]
                total += t
                outdoor += o        
        prevNode = node
    return (total, outdoor)

def isShorter(digraph, path, shortest, maxTotalDist, maxOutdoorsDist):
    pathTotalDist, pathOutdoorsDist = countDistance(digraph, path)
    if pathTotalDist <= maxTotalDist and pathOutdoorsDist <= maxOutdoorsDist:
        if shortest != None:
            shortestTotalDist, shortestOutdoorsDist = countDistance(digraph, shortest)
            if pathTotalDist < shortestTotalDist:
                return True
            elif pathTotalDist == shortestTotalDist and len(path) < len(shortest):
                return True
        else:
            return True
    return False
        
def DFS(digraph, start, end, maxTotalDist, maxOutdoorsDist, minFun, path = [], shortest = None):
    path = path + [start]
    if start == end:
        return path
    for node in digraph.childrenOf(Node(start)):
        if str(node[0]) not in path:
            newPath = DFS(digraph, str(node[0]), end, maxTotalDist, maxOutdoorsDist, minFun, path)
            if newPath != None and minFun(digraph, newPath, shortest, maxTotalDist, maxOutdoorsDist):
                shortest = newPath
    return shortest

def DFSOptimized(digraph, start, end, maxTotalDist, maxOutdoorsDist, minFun, path = [], shortest = None):
    path = path + [start]
    if start == end:
        return path
    for node in digraph.childrenOf(Node(start)):
        if str(node[0]) not in path:
            pathTotalDist, pathOutdoorsDist = countDistance(digraph, path)
            shortestTotalDist, shortestOutdoorsDist = countDistance(digraph, shortest)
            if shortest == None or pathTotalDist < shortestTotalDist:
                newPath = DFSOptimized(digraph, str(node[0]), end, maxTotalDist, maxOutdoorsDist, minFun, path)
                if newPath != None and minFun(digraph, newPath, shortest, maxTotalDist, maxOutdoorsDist):
                    shortest = newPath
    return shortest    

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
      :
          start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    path = DFS(digraph, start, end, maxTotalDist, maxDistOutdoors, isShorter)
    if path == None:
        raise ValueError
    else:
        return path

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
        
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    path = DFSOptimized(digraph, start, end, maxTotalDist, maxDistOutdoors, isShorter)
    if path == None:
        raise ValueError
    else:
        return path

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
#     Test cases
    mitMap = load_map("mit_map.txt")
##    print isinstance(mitMap, Digraph)
##    print isinstance(mitMap, WeightedDigraph)
##    print 'nodes', mitMap.nodes
##    print 'edges', mitMap.edges


    LARGE_DIST = 1000000

#     Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1, "; distance: ", countDistance(mitMap, expectedPath1)
    print "Brute-force: ", brutePath1, "; distance: ", countDistance(mitMap, brutePath1)
    print "DFS: ", dfsPath1, "; distance: ", countDistance(mitMap, dfsPath1)
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2, "; distance: ", countDistance(mitMap, expectedPath2)
    print "Brute-force: ", brutePath2, "; distance: ", countDistance(mitMap, brutePath2)
    print "DFS: ", dfsPath2, "; distance: ", countDistance(mitMap, dfsPath2)
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3, "; distance: ", countDistance(mitMap, expectedPath3)
    print "Brute-force: ", brutePath3, "; distance: ", countDistance(mitMap, brutePath3)
    print "DFS: ", dfsPath3, "; distance: ", countDistance(mitMap, dfsPath3)
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4, "; distance: ", countDistance(mitMap, expectedPath4)
    print "Brute-force: ", brutePath4, "; distance: ", countDistance(mitMap, brutePath4)
    print "DFS: ", dfsPath4, "; distance: ", countDistance(mitMap, dfsPath4)
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5, "; distance: ", countDistance(mitMap, expectedPath5)
    print "Brute-force: ", brutePath5, "; distance: ", countDistance(mitMap, brutePath5)
    print "DFS: ", dfsPath5, "; distance: ", countDistance(mitMap, dfsPath5)
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6, "; distance: ", countDistance(mitMap, expectedPath6)
    print "Brute-force: ", brutePath6, "; distance: ", countDistance(mitMap, brutePath6)
    print "DFS: ", dfsPath6, "; distance: ", countDistance(mitMap, dfsPath6)
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
