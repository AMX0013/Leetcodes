class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numString = '123456789'
        res = []
        # window grows from 5 to 6 with digits
        for windowLen in range( len(str(low)), len(str(high))+1, 1 ):

            for i in range(0,9-windowLen+1):

                num = int(numString[i:i+windowLen])

                if num >= low and num <= high:
                    res.append(num)
            
        return res




    
    # def getNumLen(self,num: int) -> int:
        
    #     size = 0
    #     while num > 0:
    #         print(num%10)
    #         size+=1
    #         num = num//10

    #     return size

    # def constructLowest(self, size:int, low:int ) -> int:
        
    #     low_arr = []
    #     first_digit = low//(10**( size -1 ) )

    #     print(low, "first_digit", first_digit)

    #     for i in range( 0 ,size,1):
    #         low_arr.append(first_digit+i)



    #     print("size: ",size, low_arr)
    #     num = int(''.join(str(element) for element in low_arr ))

    #     ones_arr = [1]*size
    #     one =int(''.join(str(element) for element in (ones_arr) ))            
    #     if num < low:
    #         num = num + one

    #     return num, one

    # def sequentialDigits(self, low: int, high: int) -> List[int]:
    #     low_size = self.getNumLen(low)
    #     high_size = self.getNumLen(high)

    #     print(low_size , high_size)
    #     res = []

    #     size = low_size
    #     num = low

    #     while size <= high_size:
            
    #         num, one = self.constructLowest(size, num)            

    #         print("ONE:",one)
    #         while num %10 != 0 and num <= high  :
    #             print(num)
    #             res.append(num)
    #             num = num+one


    #         num = 10**(size) 
    #         size+=1
            
    #     return res


        