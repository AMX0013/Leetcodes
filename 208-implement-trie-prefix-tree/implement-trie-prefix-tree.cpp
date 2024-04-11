#include <string>
#include <bits/stdc++.h>

class TrieNode
{

public:
    std::unordered_map<char, TrieNode *> children;
    bool endOfWord;
    TrieNode() : endOfWord(false) {}
};

class Trie
{
public:
    TrieNode *root;
    Trie()
    {
        root = new TrieNode();
    }

    void insert(std::string word)
    {
        TrieNode* node = root;
        for (char c : word)
        {
            if (!node->children.count(c))
            {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->endOfWord = true;
    }

    bool search(std::string word)
    {
        TrieNode* node = root;
        for (char c : word)
        {
            if (!node->children.count(c)){
                return false;
            }
            node = node->children[c];
        }
        return node->endOfWord;
    }

    bool startsWith(std::string prefix)
    {
        TrieNode* node = root;
        for (char c : prefix)
        {
            if (!node->children.count(c)){
                return false;
            }
            node = node->children[c];
        }
        return true;

    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */