
class Solution {
public:
   bool backTrackingSol(string *S, int strIdx, unordered_map<string, bool> *dict)
    {

        int l = 0;
        int Size = (*S).size();
        vector<bool> memo(Size + 1, false);
        string substring;
        int scaffold = Size;
        memo[scaffold] = true;
        

        while (l < Size)
        {
            // cout << "At idx L= " << l << endl;

            for (const auto &[key, val] : (*dict))
            {
                if ((l + int(key.size())) > Size)
                {
                    continue;
                }

                substring = (*S).substr(l, key.size());
                // cout << "\n substr:" << substring << endl;
                if ((substring == key) && memo[scaffold])
                {
                    // print("\n");
                    memo[l + key.size() - 1] = true;
                    // print(memo);
                }
            }
            l +=1;
            scaffold = l - 1;
        }
        return memo[Size - 1];
    }

    //
    bool wordBreak(string s, vector<string> &wordDict)
    {
        // The calling code receives a pointer or reference to the newly initialized object
        //  as part of the allocation expression (new TrieNode()), not from the constructor itself.
        // Trie *root = new Trie();

        unordered_map<string, bool> dict;

        for (string words : wordDict)
        {

            // backtracking solution
            dict[words] = true;
            // cout << "Added dict[" << words << "] ?: " << dict[words] << endl;
            // root->insert(words);
        }

        // backtracking soluchan
        return backTrackingSol(&s, 0, &dict);

        // find a character in the board
        // if it matches with root
    }
};