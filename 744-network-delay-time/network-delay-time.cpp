class Solution {
public:

    int networkDelayTime(vector<vector<int>>& times, int n, int k) {

        // Creating adj_list of size n+1
        vector<pair<int, int>> adj_list[n+1];

        // populating adj_list
        for (auto edge : times) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            adj_list[u].push_back({v, w});

            // cout <<"src : " << u << " v " << v << ", wt " << w << ";" <<endl;
        }

        // creating a vector to indicate the time a signal is received for each int node
        // initialized to INT_MAX, to verify if anything is unreached
        vector<int> signalReceivedTime(n+1, INT_MAX);

        // creating heap a.k.a priority queue
        /*
        Vector: Generally efficient for smaller priority queues and when frequent random access to elements is needed.
        Deque: Better for larger priority queues with frequent insertions and removals at both ends.
        Custom Container: Allows for specialized implementations and fine-tuned performance for specific use cases.
        */
        priority_queue<
            // Element type
            pair<int,int>,
            // How are they stored together? ideally as an array right?
            //  so vector. Can also use deque for efficient left and right insertion:
            vector<pair<int,int>>,
            // Comparison function like minheap or max heap: maxHeap in our case so..
            greater<pair<int,int>>
        > pq;

        // init pq
        pq.push({k,0});
        
        // init signalReceivedTime
        signalReceivedTime[k] = 0;

        while (!pq.empty()){
            // use pq.top to refer the top element and copy the values
            int currNode = pq.top().first;
            int currNodeTime = pq.top().second;

            // cout << "at node" << currNode << ",time elapsed ="<<currNodeTime << endl;
            
            // then pop it. this will delete it ensuring no dangling pointers exist, de-allocating memory
            pq.pop();

            // if node was already visited, and at an earlier time obv, continue
            if (currNodeTime > signalReceivedTime[currNode]) {
                // cout << "currNodeTime > signalReceivedTime[currNode] , SKIP" << endl;
                continue;
            }

            // bfs on currNode
            for (auto neighbors: adj_list[currNode]) {
                int neighbor = neighbors.first;
                int neighborTime = neighbors.second;
                cout  << ",neighbor = "<<neighbor << ", neightime: "<< neighborTime<< endl;
                // before adding to heap
                // check whether the current path is a better path or the first path
                if (signalReceivedTime[neighbor] > currNodeTime + neighborTime ) {
                    // cout <<  "Pushing into heap, neighbor ="<<neighbor << endl;
                    // init signalReceived[neighbor]
                    signalReceivedTime[neighbor] = currNodeTime + neighborTime;
                    // push to heap
                    pq.push( {neighbor, signalReceivedTime[neighbor] } );


                }
            }//done bfs
        } //done while

        int res = INT_MIN;
        for (int i = 1; i<=n; i++) {
            int dur = signalReceivedTime[i];
            // cout << dur << "," << endl;
            res = max(res, dur);
        }
        if (res == INT_MAX){
            return -1;
        }
        return res;


    }// done func
};