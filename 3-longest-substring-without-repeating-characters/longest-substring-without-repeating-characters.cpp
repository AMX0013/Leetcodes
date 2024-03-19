// #include <iostream>
// #include <vector>
// #include <map>
// #include <tuple>
// #include <utility> // For std::pair
// #include <string>
// #include <bits/stdc++.h>
// // #include <algorithms>
using namespace std;
 
// //////////////////////////////////////////////////////////////////////////////////
// // SPLICE 
// std::string splice(const std::string& s, int start = 0, int end = -1) {
//     int n = static_cast<int>(s.size());
//     if (end < 0) end += n; // Adjust negative indices
//     if (end > n) end = n;  // Constrain end to size
//     if (start < 0) start += n; // Adjust negative indices
    
//     if (start > end || start >= n || end <= 0) return ""; // Return empty string for invalid ranges
    
//     start = std::max(start, 0); // Constrain start to valid range
//     return s.substr(start, end - start+1);
// }

// template<typename T>
// std::vector<T> splice(const std::vector<T>& v, int start = 0, int end = -1) {
//     int n = static_cast<int>(v.size());
//     if (end < 0) end += n; // Adjust negative indices
//     if (end > n) end = n;  // Constrain end to size
//     if (start < 0) start += n; // Adjust negative indices
    
//     std::vector<T> result;
//     if (start > end || start >= n || end <= 0) return result; // Return empty vector for invalid ranges
    
//     start = std::max(start, 0); // Constrain start to valid range
//     for (int i = start; i < end; ++i) {
//         result.push_back(v[i]);
//     }
//     return result;
// }

// //////////////////////////////////////////////////////////////////////////////////


// //////////////////////////////////////////////////////////////////////////////////
// // PRINT
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
// // Template specialization for sets
// template<typename T>
// void print(const std::set<T>& s) {
//     std::cout << "{";
//     for (auto it = s.begin(); it != s.end(); ) {
//         print(*it); // Use the existing print function for the element
//         ++it;
//         if (it != s.end()) std::cout << ", ";
//     }
//     std::cout << "}";
// }
// // Template specialization for std::unordered_set
// template<typename T>
// void print(const std::unordered_set<T>& s) {
//     std::cout << "{";
//     for (auto it = s.begin(); it != s.end(); ) {
//         print(*it); // Use the existing print function for the element
//         ++it;
//         if (it != s.end()) std::cout << ", ";
//     }
//     std::cout << "}";
// }
//////////////////////////////////////////////////////////////////////////////////////////////////////////

class Solution {
public:


    int lengthOfLongestSubstring(string s) {
        // sliding window
        int res =0;
        int anchor=0;
        vector<bool> vectorChar(256,0);


        
        for (int i=0; i< s.length(); i++) {
            // print(res, i, anchor);
            if (vectorChar[s[i]]) {
                // right met a duplicate char
                while (vectorChar[s[i]]){
                    vectorChar[s[anchor]] = 0;
                    anchor++;
                }
            }
            // }else{
                vectorChar[s[i]]=1;
                res = max(res, i-anchor+1);
                // i++;
            // }
            

        }
        // print(res, anchor);

        return res;
    }
};