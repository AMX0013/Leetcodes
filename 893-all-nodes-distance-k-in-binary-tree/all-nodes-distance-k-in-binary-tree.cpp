/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


class Solution {
public:

    void dfs(TreeNode *node, std::unordered_map<TreeNode *, TreeNode *> *parentMap)
    {
        // Insert logic here
        // left traversal
        if (node->left != NULL)
        {
            /*TreeNode* is a pointer and it is a valid key type for std::unordered_map, because pointers can be hashed and compared by default.
            The actual issue seems to be related to how you're accessing the parentMap.
            Since parentMap is a pointer to an unordered_map, you need to dereference it before using the subscript operator ([]).
            You should be using (*parentMap)[child] = node; instead of parentMap[child] = node;.*/
            (*parentMap)[node->left] = node;
            dfs(node->left, parentMap);
        }
        // right traversal
        // right traversal
        if (node->right != NULL)
        {
            (*parentMap)[node->right] = node;
            dfs(node->right, parentMap);
        }
    }
    
    

    vector<int> distanceK(TreeNode *root, TreeNode *target, int k)
    {
        // create a parent mapping
        // do it with recursive dfs
        std::unordered_map<TreeNode *, TreeNode *> parentMap;
        // BFS Q
        queue<pair<TreeNode *, int>> bfsQ;
        // visited array
        vector<bool>visited(500);
        // result
        vector<int> res;


        // populate parents
        dfs(root, &parentMap);
        // init BFS
        bfsQ.push({target, 0});
        // Exec BFS 
        while (!bfsQ.empty())
        {

            pair<TreeNode *, int> package = bfsQ.front();
            bfsQ.pop();

            TreeNode *node = package.first;

            if ( node == NULL ) {
                continue;
            }

            if (visited[node->val]){
                
                // cout<< "revisiting" << node->val <<endl;
                continue;
            }

            int dist = package.second;
            visited[node->val] = true;
            
            // cout << "-----at" <<(*node).val <<endl;

            if (dist == k)
            {
                // stop further exploration
                
                // cout << (*node).val << "dist from " << (*target).val << "is " << dist<<endl;;
                res.push_back(node->val);
                continue;
            }
            // explore LEFT
            if ((node->left != NULL) )
            {   
                
                // cout<<"inserting left" << node->left->val << endl;
                bfsQ.push({node->left, dist + 1});
            }
            // explore RIGHT
            if ((node->right != NULL) )
            {   
                
                // cout<<"inserting right" << node->right->val << endl;
                bfsQ.push({node->right, dist + 1});
            }
            // explore Parent-wise
            
            // cout << "(parentMap[node] != NULL)" <<(parentMap[node] != NULL)   ;

            if ((parentMap[node] != NULL) )
            {   
                // cout<<"inserting parent" << parentMap[node]->val << endl;
                bfsQ.push({parentMap[node], dist + 1});
            }
        }

        return res;
    }
};