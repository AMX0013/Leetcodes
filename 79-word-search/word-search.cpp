#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <utility> // For std::pair



class Solution {
public:
    // optimization: prevent usage of visited, memory space by temporarily changing the curr loc var
    bool wordFind( vector<vector<char>>& board, string word, int row,int col,int height,int width  ,int strIdx){
    
        if ( -1<row && -1<col && row < height  && col <width  ) {
        
            if (word[strIdx] == board[row][col] ) {
                strIdx+=1;
            }
            else{
                return false;
            }
            if (strIdx == word.size() ) {
                    // finally reached!
                    return true;
            }
            else{
                char temp = board[row][col];
                board[row][col] = '*';
                if ( wordFind(board, word, row +1, col   ,height,width, strIdx ) ) return true;
                if ( wordFind(board, word, row -1, col   ,height,width, strIdx ) ) return true;
                if ( wordFind(board, word, row   , col +1,height,width, strIdx ) ) return true;
                if ( wordFind(board, word, row   , col -1,height,width, strIdx ) ) return true;
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
 
                    if (wordFind(board, word, row,col,height,width, 0 ) ){
                        return true;

                    }
                    
            }
        }

        return false;
        
    }
};