class Solution {
public:
    // time to traverse = time
    // change: time to wait in each city
        // change indicates how many hops can we do after we start
        // then we'll have to wait for the remiander of the time in the city we are in
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        
        priority_queue<

            pair<int,int>,
            vector<pair<int,int>>,
            // greater the value, lesser the priority
            greater<pair<int, int>>
        > pq;
        // min distances here
        vector<int> minTime(n+1, INT_MAX);
        // second min Timeances here
        vector<int> minTime2(n+1, INT_MAX);
        // 2 visits vector
        int visitedDest = 0;

        vector<int> adj_list[n+1];
        for (auto edge: edges){
            int src = edge[0];
            int dest = edge[1];

            adj_list[src].push_back(dest);
            adj_list[dest].push_back(src);
            
        } 
        // steps: the number of cities being visited, except 1
        // pq.push({step=0, start =1})
        pq.push({0,1});
        
        while (!pq.empty()) {
            int currTime = pq.top().first;
            int currNode = pq.top().second;
            pq.pop();

            if (currNode == n) {
                visitedDest +=1;
                // cout << "reached " << currNode << " at : " << currTime <<"for the "<< visitedDest <<endl;
                if (visitedDest==2){
                    return currTime;
                }
            }
            
            // cout << "reached " << currNode << " at : " << currTime <<endl;

            // wait for signal
            if ((currTime/change)%2!=0) {
                currTime = change * (currTime/change +1);
                // cout << "Signal red at: "<< currNode << "expected departure time : "<< currTime <<endl;

            }
            // Compute Travel time to neighbor
            int travelTime =  currTime + time;
            // cout << "from "<< currNode << ", est travel time to neighbors = " << travelTime <<endl;
            
            

            for (auto neighbor : adj_list[currNode]) {

                // decide how to enter it into the two
                if ( minTime[neighbor] > travelTime ){
                    // see if its the second least time and insert there
                    // cout<< "going to " << neighbor << "for the first time , reaching at time: "<< travelTime << endl;
                    minTime2[neighbor] = minTime[neighbor];
                    minTime[neighbor] = travelTime ;
                    // Insert this
                    pq.push({travelTime, neighbor});
                }
                // prevent taking a route that will be a new shortest route as stored in minTime
                else if (minTime2[neighbor] > travelTime and travelTime !=  minTime[neighbor] ){
                    // cout<< "going to " << neighbor << "for the SECOND time , reaching at time: "<< travelTime << endl;

                    minTime2[neighbor] = travelTime ;
                    // Insert this
                    pq.push({travelTime, neighbor});
                }
                else{
                    continue;
                }
            }
        }
        // find second largest step
        // ensure visited policy
        // return steps*time
        // if (minTime2[n] != INT_MAX) {
        //     return minTime2[n];
        // }

        return 0;   
    }
};