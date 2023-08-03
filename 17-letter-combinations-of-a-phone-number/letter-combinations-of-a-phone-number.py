class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2":["a","b","c"] , "3":["d","e","f"] ,"4":["g","h","i"] , "5":["j","k","l"],"6":["m","n","o"] , "7":["p","q","r","s"] ,"8":["t","u","v"] ,  "9":["w","x","y","z"] }
        # print(phone)


        def recur(digs):
            returnRes = []
            if len(digs) == 1:
                return phone[digs]

            else:
                head = digs[0]

                headChars = phone[head]

                rest = recur(digs[1:])
                print(rest)
                for char in headChars:
                    for combs in rest:
                        temp = char+combs
                        if temp not in returnRes:
                            returnRes.append(temp)
            return returnRes

        if digits == "":
            return []
        return recur(digits)
        
