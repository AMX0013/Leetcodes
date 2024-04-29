// template <typename ele_type>

// // print() function takes a vector as an input argument

// void print(const vector<ele_type>& V){

// copy(V.begin(),V.end(),ostream_iterator<ele_type>(cout, " "));

// }

class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();

        vector<int> right(n,1);
        vector<int> res(n,1);
        vector<int> left(n,1);
        
        for(int i = 1; i < n; i++){
            if (ratings[i] > ratings[i-1]){
                // cout<< "ratings["<<i<<"] > ratings["<<i-1<<"] : "<<(ratings[i] > ratings[i-1]) <<endl;
                right[i]=right[i-1]+1;
            }
        }
        for(int i = n-2; i > -1; i--){
            if (ratings[i] > ratings[i+1]){
                left[i]=left[i+1]+1;
            }
            res[i] = max(left[i],right[i]);
        }
        
        res[n-1] = max(left[n-1],right[n-1]);
        // print(res);
        return accumulate(res.begin(),res.end(),0);
    }
};