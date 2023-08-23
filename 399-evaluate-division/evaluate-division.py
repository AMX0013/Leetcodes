


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        dic = {}
        # implement unionFind


        # a:(b,2)
        # b:(c,3)
        # c:(c,1)

        # find(b) > b/c = 3
                # > b->c =3
                # > returns (c,3)
        # find(a) > returns (b,2)
                    # recursively find 
                # >   

        def find(x):
            if x not in dic:
                # store tuples, (parent , value)

                # default for a new var
                dic[x] = (x,1)

            group , val = dic[x]
            print("\n","initialised " ,x ,"to :", dic[x])

            # recur find the connected components to source
            # Note we are only mentione directed path 
            if x!= group:

                new_group , new_val = find(group)
                # b->c = 3
                # a->b = 2
                    # >> a->c = 6
                dic[x] = (new_group , new_val*val)

            print("post collapsing find " ,x ,"evaluated to :", dic[x],"\n")

            return dic[x]
        def union(numer, denom, val):
            grp1 , val1 = find(numer) 
            grp2 , val2 = find(denom)

            # Lets only add new eqns here

            if grp1 != grp2:
                # add a new relationship

                # assume a/b = 2
                # then there's a new input a/e = 5
                    # then we must change the link from b to e> 
                    # dic[a_parent]= (e_parent ,  5*( e->e= 1 / a->b=2  ) )

                print("creating new reln")
                dic[grp1]= (grp2 , (value*val2/val1)  ) 


        # begin 
        res = []

        # load equations and values
        for (dividend ,  divisor) , value in zip(equations , values):
            union(dividend , divisor ,value)
        
        print(dic)

        # Solve queries:

        for numer , denom in queries:
            # unknown var
            if (numer not in dic ) or (denom not in dic):
                res.append(-1.00)
                continue
            # a/a
            if numer == denom:
                res.append(1.00)
                continue

            # crunch the queries
            # numerator -> . . . -> denom


            grp1 , val1 = find(numer)
            grp2 , val2 = find(denom) 

            if grp1 == grp2:
                # a common factor found and divison generates the query
                res.append(val1/val2)
            else:
                # no relationship with query
                res.append(-1.00)

        return res
