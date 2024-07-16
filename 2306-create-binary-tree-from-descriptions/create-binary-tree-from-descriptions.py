# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        is_root = set()
        tree_dict = defaultdict(TreeNode)

        # add all parents
        for par, child, isLeft in descriptions:
            if par not in tree_dict:
                tree_dict[par] = tree_dict.get(par, TreeNode(par))
                is_root.add(par)

        # add all children, and remove children nodes from set is_root

        for par, child, isLeft in descriptions:
            parent_node = tree_dict[par]
            child_node = tree_dict.get(child, TreeNode(child) )

            if isLeft:
                
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            if child in is_root:
                is_root.remove(child)

        for item in is_root:
            
            return tree_dict[item]




            
        