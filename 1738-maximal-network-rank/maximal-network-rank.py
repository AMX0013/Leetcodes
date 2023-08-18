class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        densityDict = defaultdict(set)


        denseCityLen  = 0
        denseCity2Len = 0
        
        denseCity = 0
        denseCity2 =0

        for c1,c2 in roads:
            # densityDict[c1] = densityDict.get(c1,{})
            densityDict[c1].add(c2)
            densityDict[c2].add(c1)


            # This wont work

            # Eg: defaultdict(<class 'set'>, {0: {1, 3}, 1: {0, 2, 3}, 3: {0, 1}, 2: {1}})
            # 0: {1, 3}  and  3: {0, 1} have same len and cound be 2 
            #  but 0 preferred

            # if len(densityDict[c1]) > denseCityLen or len(densityDict[c2]) > denseCityLen:
            #     denseCity2 = denseCity
            #     if len(densityDict[c1]) > len(densityDict[c2]):
            #         denseCity = c1
            #     else:
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