class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        densityDict = defaultdict(set)


        denseCityLen  = 0
        denseCity = 0

        for c1,c2 in roads:
            # densityDict[c1] = densityDict.get(c1,{})
            densityDict[c1].add(c2)
            densityDict[c2].add(c1)
            

            # Finding one densest city wont work as it landed on 11
            # {
            #    8: {1, 11, 12},
            #   12: {8, 5}, 
            #    5: {10, 11, 12}, 
            #   11: {8, 3, 5},
            #    9: {0, 4},
            #    4: {9, 3},
            #    0: {9},
            #    1: {8},
            #   10: {2, 5}, 
            #    2: {10}, 
            #   13: {14}, 
            #   14: {13},
            #    3: {11, 4}, 
            #    6: set(),
            #    7: set()
            # }

            # if len(densityDict[c2])>len(densityDict[c1]):

            #     if denseCityLen < len(densityDict[c2]):
            #         denseCityLen = len(densityDict[c2])
            #         denseCity = c2
            # else:

            #     if denseCityLen < len(densityDict[c1]):

            #         denseCityLen = len(densityDict[c1])
            #         denseCity = c1
            
        maxC = 0
        for c1 in range(n):
            lc1 = len(densityDict[c1])

            for c2 in range(n):
                
                if c1 == c2:
                    continue

                lc2 = len(densityDict[c2])
                if c1 in densityDict[c2]:
                    lc2-=1              
                maxC = max(maxC,lc1+lc2)
                # print(maxC ,densityDict[c1] ,densityDict[c2] )

        print(densityDict)
            
        # print(densityDict , denseCity , denseCity2 )
        return maxC