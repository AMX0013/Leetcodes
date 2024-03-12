class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> minTime(n + 1, INT_MAX);
        // node[node_num] (time, next_node)
        vector<pair<int, int>> node[n + 1];
        // pq(time, next_node)
        priority_queue<pair<int, int>, vector<pair<int, int>>,
                       greater<pair<int, int>>>
            pq;
        for (int i = 0; i < times.size(); i++) {
            int from = times[i][0];
            int to = times[i][1];
            int time = times[i][2];
            node[from].push_back(make_pair(time, to));
        }
        pq.push(make_pair(0, k));
        minTime[k] = 0;

        while (!pq.empty()) {
            int time = pq.top().first;
            int cur_node = pq.top().second;
            pq.pop();
            // cout << "cur_node" << cur_node << endl;
            if (time > minTime[cur_node]) {
                cout << "c" << endl;
                continue;
            }

            for (int i = 0; i < node[cur_node].size(); i++) {
                // cout << "node" << cur_node << "s"<< node[cur_node].size() <<
                // endl;
                int next_time = node[cur_node][i].first;
                int next_node = node[cur_node][i].second;
                if (next_time + minTime[cur_node] < minTime[next_node]) {
                    minTime[next_node] = next_time + minTime[cur_node];
                    pq.push(make_pair(next_time, next_node));
                    // cout << "push" << endl;
                }
            }
        }
        int ret = -1;
        for (int i = 1; i <= n; i++) {
            cout << "i" << i << ":" << minTime[i] << endl;
            ret = max(ret, minTime[i]);
        }
        if (ret == INT_MAX)
            return -1;

        return ret;
    }
};