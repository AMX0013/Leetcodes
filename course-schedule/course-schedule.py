class Solution:
    def recurCycleFound(self,adjacencyMatrix,node,visited,dfsStack):
        visited[node] = True
        dfsStack[node] = True
        for neighbor in adjacencyMatrix[node]:
            # process un visited nodes:
            # idea is to explore a subgraph from node, that was passed
            if visited[neighbor] == False:
                if self.recurCycleFound(adjacencyMatrix,neighbor,visited,dfsStack) :
                    print("->",neighbor)
                    return True # cycle found
            elif dfsStack[neighbor] :
                print("->",neighbor)
                return True     # cycle found
        # Cycle not found, loop broken
        dfsStack[node] = False # to permit further exploration here?
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canComplete =True
        # You are given an array prerequisites where prerequisites[i] = [ai, bi] 
        # indicates that you must take 
            # course bi first 
            # if you want to take course ai.
            # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        # look like a cycle detection problem in a Directed Graph 
        # [[1,0],[0,1]] >
            # Edges:
                #  1->0
                #  0->1
            # its a cycle!

        dfsStack = defaultdict(bool)

        visited = defaultdict(bool)

        coursesCompleted = 0
        adjacencyMatrix = defaultdict(list)
        for edges in prerequisites:
            adjacencyMatrix[edges[1]].append(edges[0])
            coursesCompleted = max(coursesCompleted, max(edges))
        # print(coursesCompleted)
        

        # Cycle detection
        for node in range(numCourses):
            cycleFound = self.recurCycleFound(adjacencyMatrix,node,visited,dfsStack)
            
            if cycleFound:
                print(node)
                canComplete = False
                break
            


        if coursesCompleted < numCourses and canComplete:
            return True
        else:
            return False
