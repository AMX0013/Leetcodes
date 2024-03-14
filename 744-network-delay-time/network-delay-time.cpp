class Solution {
public:

    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> signalReceivedTime(n+1, INT_MAX);
        signalReceivedTime[k] = 0;
        priority_queue<

            pair<int,int>,

            vector<pair<int,int>>,

            greater<pair<int,int>>
        > pq;
        pq.push({0,k});
        vector<pair<int, int>> adj_list[n+1];        
        for (auto edge : times) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            adj_list[u].push_back({w,v});

        }

        while (!pq.empty()){
            int currNodeTime = pq.top().first;
            int currNode = pq.top().second;
            pq.pop();
            if (currNodeTime > signalReceivedTime[currNode]) {
                // cout<< currNodeTime <<" skip" <<endl;
                continue;
            }
            for (auto neighbors: adj_list[currNode]) {
                int neighborTime = neighbors.first;
                int neighbor = neighbors.second;
                // cout  << ",neighbor = "<<neighbor << ", neightime: "<< neighborTime<< endl;
                if (signalReceivedTime[neighbor] > currNodeTime + neighborTime ) {
                    signalReceivedTime[neighbor] = currNodeTime + neighborTime;
                    pq.push( {signalReceivedTime[neighbor],neighbor} );
                }
            }//done bfs
        } //done while

        int res = -1;
        for (int i = 1; i<=n; i++) {
            int dur = signalReceivedTime[i];
            res = max(res, dur);
        }
        if (res == INT_MAX){
            return -1;
        }
        return res;


    }// done func
};