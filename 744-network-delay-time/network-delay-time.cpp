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
        pq.push({k,0});
        vector<pair<int, int>> adj_list[n+1];        
        for (auto edge : times) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            adj_list[u].push_back({v, w});

        }
        while (!pq.empty()){
            int currNode = pq.top().first;
            int currNodeTime = pq.top().second;
            pq.pop();
            if (currNodeTime > signalReceivedTime[currNode]) {
                continue;
            }
            for (auto neighbors: adj_list[currNode]) {
                int neighbor = neighbors.first;
                int neighborTime = neighbors.second;
                cout  << ",neighbor = "<<neighbor << ", neightime: "<< neighborTime<< endl;
                if (signalReceivedTime[neighbor] > currNodeTime + neighborTime ) {
                    signalReceivedTime[neighbor] = currNodeTime + neighborTime;
                    pq.push( {neighbor, signalReceivedTime[neighbor] } );
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