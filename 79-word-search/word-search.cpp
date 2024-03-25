#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <utility> // For std::pair

// // Function to end recursion
// void print_end() {
//     std::cout << std::endl;
// }

// // Base case for single non-iterable argument
// template<typename T>
// typename std::enable_if<!std::is_same<T, std::string>::value && !std::is_same<T, std::vector<bool>>::value, void>::type
// print(const T& value) {
//     std::cout << value;
// }

// // Overload for strings to avoid treating them as iterables
// void print(const std::string& value) {
//     std::cout << "\"" << value << "\"";
// }

// // Special handling for vector<bool>
// void print(const std::vector<bool>& v) {
//     std::cout << '{';
//     for (size_t i = 0; i < v.size(); ++i) {
//         std::cout << (v[i] ? "true" : "false");
//         if (i != v.size() - 1) std::cout << ", ";
//     }
//     std::cout << '}';
// }

// // Recursive variadic template to handle multiple arguments
// template<typename T, typename... Args>
// void print(const T& first, const Args&... args) {
//     print(first); // Print the first argument
//     ((std::cout << ", ", print(args)), ...); // Fold expression for the rest
//     print_end(); // End line after all arguments are printed
// }

// // Template specialization for pairs
// template<typename T1, typename T2>
// void print(const std::pair<T1, T2>& p) {
//     std::cout << "(";
//     print(p.first);
//     std::cout << ", ";
//     print(p.second);
//     std::cout << ")";
// }

// // Template specialization for vectors
// template<typename T>
// void print(const std::vector<T>& vec) {
//     std::cout << "[";
//     for (size_t i = 0; i < vec.size(); ++i) {
//         print(vec[i]);
//         if (i != vec.size() - 1) std::cout << ", ";
//     }
//     std::cout << "]";
// }

// // New overload for arrays of vectors
// template<typename T>
// void print(T* arr, size_t N) {
//     std::cout << "[";
//     for (size_t i = 0; i < N; ++i) {
//         print(arr[i]); // Use existing print for vector
//         if (i < N - 1) std::cout << ", ";
//     }
//     std::cout << "]" << std::endl;
// }


// // Template specialization for maps
// template<typename K, typename V>
// void print(const std::map<K, V>& map) {
//     std::cout << "{";
//     for (auto it = map.begin(); it != map.end(); ) {
//         print(it->first);
//         std::cout << ": ";
//         print(it->second);
//         ++it;
//         if (it != map.end()) std::cout << ", ";
//     }
//     std::cout << "}";
// }


class Solution {
public:

    bool wordFind( vector<vector<char>>& board, string word, vector<vector<bool>>& visited, std::pair<int,int>& currLoc,int strIdx){

        // std::vector<std::pair<int,int>> 
        // unpacking: 
        int rowValue = currLoc.first;
        int colValue = currLoc.second;
        string str = "";

        str.insert(0, strIdx, ' ');
        // print(str,"at :",rowValue, colValue);

        if (word[strIdx] == board[rowValue][colValue] ) {
            strIdx+=1;
        }
        else{
            return false;
        }

        if (strIdx == word.length() ) {
                // finally reached!
                return true;
        }


        visited[rowValue][colValue] = true;

        vector<std::pair<int,int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        // print(directions);printf("\n-----\n");
        for (auto dir : directions){
            
            int newRow = rowValue + dir.first;
            int newCol = colValue + dir.second;     
            // print(str,"new idicies",newRow, newCol);

            if ( (0<=newRow && newRow < board.size() ) and ( 0<=newCol && newCol <board[newRow].size() ) ) {
                if (!visited[newRow][newCol]  ) {
                    // explore
                    std::pair<int,int> nextLoc = {newRow, newCol};
                    if ( wordFind(board, word, visited, nextLoc, strIdx ) ) {
                        return true;
                    }                    
                }
            }
        }
        visited[rowValue][colValue] = false;
        return false;
    }
  
    bool exist(vector<vector<char>>& board, string word) {


        
        vector<vector<bool>> visited( board.size(), vector<bool>(board[0].size(), false)  );

        // vector<vector<char>> visited;
        // first find the starting word

        for (int row = 0; row <board.size();row++){
            for (int col = 0; col <board[row].size();col++){

                // if (board[row][col] == word[0] ) {
                //     // check out its neighbours recursively 
                    std::pair<int,int> currLoc = {row, col};
                    int strIdx = 0;
                //     visited[row][col]= true;
                    if (wordFind(board, word, visited, currLoc, strIdx ) ){
                        return true;

                    }
                    // visited[row][col] = false;
                // }
            }
        }

        return false;
        
    }
};