class Solution {
public:
    int kthFactor(int n, int k) {
        std::vector<int> factorLow;
        std::vector<int> factorHigh;
        //The loop condition (i * i <= n) only needs the incremented value of i.
        // Using ++i avoids a potential extra copy of the original value of i,
        //  which might be created with i++ in some cases.
        for (int i = 1; i*i <= n; ++i ) {
            if (n%i == 0){
                factorLow.push_back(i);
                k-=1;
                if (k==0){
                    return i;
                }

                if (i != n/i ) {
                    factorHigh.push_back(n/i);
                }

            }
        }

        if (k > factorHigh.size()) {
            return -1;
        }

        return factorHigh[  (factorHigh.size()) - k ];

    }
};