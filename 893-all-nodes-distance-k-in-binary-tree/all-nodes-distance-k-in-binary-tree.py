# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # dfs to create a associated list

        parent = defaultdict(TreeNode)

        def dfs(node):
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
            return

        dfs(root)
        bfs_q = deque()
        visited = set()
        # | | | | |
        # append(): Insert from rear/right
        # popleft(): delete from front/left
        

        bfs_q.append((target,0))
        res = []
        

        node_dist_dict = defaultdict(int)

        while len(bfs_q)>0:
            node,height = bfs_q.popleft()

            visited.add(node)
            
            # node_dist_dict[node]=height
            if height == k:
                res.append(node.val)
            
            if height > k:
                break

            
            if node in parent.keys() and parent[node] not in visited  :
                bfs_q.append((parent[node],height+1))

            if node.left and node.left not in visited :
                bfs_q.append((node.left,height+1))

            if node.right and node.right not in visited:
                bfs_q.append((node.right,height+1))

        

        return res  
        


        




        