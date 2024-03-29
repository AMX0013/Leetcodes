/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void dfs(TreeNode* node, int* allBranches, int branch) {
        
        branch*=10;
        branch+=(node->val);
        
        if (node->left != NULL){
            dfs(node->left, allBranches, branch );           
        }
        
        if (node->right != NULL) {
            dfs(node->right, allBranches, branch );
        }
        if ((node->right == NULL) and (node->left == NULL)) {
            *allBranches += branch;
            // cout<< "\n"<< branch << " and total ="<< *allBranches << "\n" ;
        }        

    }

    int sumNumbers(TreeNode* root) {

        int allBranches = 0;

        dfs(root, &allBranches, 0);
        
        return allBranches;
        
        
    }
};