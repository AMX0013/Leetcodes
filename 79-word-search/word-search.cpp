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
    // optimization: prevent usage of visited, memory space by temporarily changing the curr loc var
    bool wordFind( vector<vector<char>>& board, string word, int row,int col  ,int strIdx){
    
        if ( (0<=row && row < board.size() ) and ( 0<=col && col <board[row].size() ) ) {
        
            if (word[strIdx] == board[row][col] ) {
                strIdx+=1;
            }
            else{
                return false;
            }
            if (strIdx == word.length() ) {
                    // finally reached!
                    return true;
            }
            else{
                char temp = board[row][col];
                board[row][col] = '*';
                if ( wordFind(board, word, row +1, col   , strIdx ) ) return true;
                if ( wordFind(board, word, row -1, col   , strIdx ) ) return true;
                if ( wordFind(board, word, row   , col +1, strIdx ) ) return true;
                if ( wordFind(board, word, row   , col -1, strIdx ) ) return true;
                board[row][col] = temp;
            }
            

        }
        return false;
    }
  
    bool exist(vector<vector<char>>& board, string word) {

        int height = board.size();
        int width = board [0].size();

        vector<vector<bool>> visited( height, vector<bool>(width, false)  );

        for (int row = 0; row <height;row++){
            for (int col = 0; col <width;col++){
 
                    if (wordFind(board, word, row,col, 0 ) ){
                        return true;

                    }
                    
            }
        }

        return false;
        
    }
};