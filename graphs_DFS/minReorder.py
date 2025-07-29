# 1466
# n: int, connections: List[List[int]] -> int
# Time : O(n), Space : O(n)

def minReorder(n, connections):
    # start at city 0
    # recursively check its neighbors
    # count outgoing edges (how many edges should be changed?)

    edges = {(a,b) for  a,b in connections}
    # find the neighbors of each city(node)
    neighbors =  { city:[] for city in range(n)}
    # we only wanna visit each node once
    visitedNodes = set()
    numChanges = 0

    for a, b in range(n):
        neighbors[a].append(b)
        neighbors[b].append(a)

    def dfs(city):
        # nonlocal variables so we dont have to pass them for every function call
        nonlocal edges, neighbors, visitedNodes, numChanges
        # for each city we wanna iterate through each of its neighbors
        for neighbor in neighbors[city]:
            if neighbor in visitedNodes:
                continue
            # check if this neighbor can reach city 0
            # if neighbor and city exist in edges that means the neighbor can reach the city directly if not we have to reorder the edge
            if (neighbor, city)  not in edges:
                numChanges +=1
            visitedNodes.add(neighbor)
            # check if its neighbors neighbors can reach the city 0 so do it recursively 
            dfs(neighbor)

        visitedNodes.add(0)
        dfs(0) # our starting point
        return numChanges






# My Note:
# The nonlocal keyword is used to work with variables inside nested functions,
# where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local.