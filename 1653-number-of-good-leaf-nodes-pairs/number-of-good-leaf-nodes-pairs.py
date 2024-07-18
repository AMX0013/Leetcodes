# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def create_graph(self, root: TreeNode):
        adj_list = defaultdict(list)
        leaves = set()
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.left:
                L = node.left
                # Edge L->node
                adj_list[L] = adj_list.get(L, [])
                adj_list[L].append(node)
                # Edge node->L
                adj_list[node] = adj_list.get(node, [])
                adj_list[node].append(L)
                stack.append(L)
            if node.right:
                L = node.right
                # Edge L->node
                adj_list[L] = adj_list.get(L, [])
                adj_list[L].append(node)
                # Edge node->L
                adj_list[node] = adj_list.get(node, [])
                adj_list[node].append(L)
                stack.append(L)

            if not node.left and not node.right:
                leaves.add(node)


        return adj_list, leaves

    def countPairs(self, root: TreeNode, distance: int) -> int:    

        # create adjacency matrix
        adj_list, leaves = self.create_graph(root)
        # print(adj_list, leaves)
        self.pairs = 0

        # bfs
        def bfs(leaf: TreeNode):
            q = deque()
            visited = set()
            src = leaf
            q.appendleft((src,0))

            while q:
                node, dist = q.pop()
                visited.add(node)
                if node != src and node in leaves:
                    self.pairs +=1
                if dist == distance:
                    # break ideally or even continue
                    continue
                    # return
                
                for dest in adj_list[node] :
                    if dest not in visited:
                        q.appendleft((dest,dist+1))


        for leaf in leaves:
            bfs(leaf)

        return self.pairs//2

