class Solution:

    def digit_arr(self,num: int) -> int:
        # digit_arr = []
        digits = 0

        while num > 0:
            print(num%10)
            # mod = num%10
            # digit_arr.append(mod)
            digits+=1
            num = num//10

        # digit_arr.reverse()

        # return digit_arr
        return digits

    def constructLowest(self, digits:int, low:int ) -> int:
        
        low_arr = []
        # print("length of low =", len(str(low)), 10**( len(str(low))  -1  ) )
        first_digit = low//(10**( digits -1 ) )
        print(low, "first_digit", first_digit)

        for i in range( 0  ,digits,1):
            low_arr.append(first_digit+i)

        print("size: ",digits, low_arr)
        number = int(''.join(str(element) for element in low_arr ))

        return number

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_size = self.digit_arr(low)
        high_size = self.digit_arr(high)

        print(low_size , high_size)
        res = []

        size = low_size
        num = low

        while size <= high_size:
            
            num = self.constructLowest(size, num)
            ones_arr = [1]*size
            one =int(''.join(str(element) for element in (ones_arr) ))
            
            print("ONE:",one)
            while num %10 != 0 and num <= high  :
                print(num)
                if num >= low:
                    res.append(num)
                num = num+one


            num = 10**(size) 
            size+=1
            
        return res


        