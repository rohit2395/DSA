class Solution:
    ##Complete this function
    #Function to check if array is sorted and rotated.
    
    def checkIfIncreasing(self, arr, n):
        isIncreasing = True
        for i in range (1, n , 1):
            if arr[i] < arr[i-1]:
                isIncreasing = False
                break
        return isIncreasing
        
    def checkIfDecreasing(self, arr, n):
        isDecreasing = True
        for i in range (1, n , 1):
            if arr[i] > arr[i-1]:
                isDecreasing = False
                break
        return isDecreasing
        
    def checkRotatedAndSorted(self,arr,n):
        #code here
        if n == 2:
            return True

        ## If sorted array is allowed then comment the following two lines
        # if self.checkIfIncreasing(arr,n) or self.checkIfDecreasing(arr,n):
        #     return False

        count1 = 0
        if arr[0] < arr[n-1]:
            count1 += 1
        for i in range(1, n, 1):
            if arr[i-1] > arr[i]:
                count1 += 1
                
        count2 = 0
        if arr[0] > arr[n-1]:
            count2 += 1
        for i in range(1, n, 1):
            if arr[i-1] < arr[i]:
                count2 += 1

        return count1 <= 1 or count2 <= 1

if __name__ == "__main__":
    solution = Solution()
    arr = [3,4,5,1,2]
    print(solution.checkRotatedAndSorted(arr,len(arr)))

    arr = [2,1,3,4]
    print(solution.checkRotatedAndSorted(arr,len(arr)))

    arr =[1,2,3]
    print(solution.checkRotatedAndSorted(arr,len(arr)))

    arr =[6,10,6]
    print(solution.checkRotatedAndSorted(arr,len(arr)))

