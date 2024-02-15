class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # problem : find all rooths such that we get a mht of height h
        # here, only the non leaf nodes should be chosento create a mht
        # AMong the non-leaft nodes, there may be a node that gives the least height? : Greedyness?
        # While checking heights, we may calculate several times : DP?
        # most times, no. of mhts = no of unique non leaf nodes 

        adjList = defaultdict(set)

        for u,v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        # iterate thru all nodes

        max_Outdeg = 0
        res = []
        leaves = []
        newLeaves = []
        inDegree = []

        # Round 1: identify leaves and find all indegree
        for i in range(n):
           
            if len(adjList[i]) <=1:
                # its a leaf node
                leaves.append(i)
            # maintain everyone's inDegree nonetheless
            inDegree.append(len(adjList[i]))
        
        # leaf deletion dp

        # a mht can atleast contain 2 roots nodes right?
        nodesLeft = n
        # print(leaves, inDegree)


        while nodesLeft > 2:
            for leafNode in leaves:
                # inDegree[leafNode] -=1 redundant
                for innerNode in adjList[leafNode]:
                    inDegree[innerNode] -=1
                    if inDegree[innerNode] == 1:
                        # next leaves detected
                        newLeaves.append(innerNode)
            # leaves deleted            # 
            nodesLeft -= len(leaves)
            # assign new Leaves 
            leaves = newLeaves.copy()
            
            newLeaves.clear()

            # print(leaves)

        return leaves