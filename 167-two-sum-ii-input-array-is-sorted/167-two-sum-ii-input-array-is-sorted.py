class Solution:
    def binarySearch(self, arr,N, Left, Right):
        while Left <= Right:
            mid = (Left + Right)//2
            if N== arr[mid] :
                print("found")
                return mid
            elif N < arr[mid]:
                Right = mid-1
            elif N > arr[mid]:
                Left = mid+1
        print("Not found",N)
        return None
            
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = numbers[i]
            y = target-x
            
            j = self.binarySearch(numbers,y,i+1,len(numbers)-1)
            print(x,y,i,j)
            if j:
                if j != i:
                    return [i+1,j+1]
        