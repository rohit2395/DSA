
class Solution:
        
    def max_sum(self, arr, k):
        maximum_sum = 0
        curr_sum = 0
        if k > len(arr) or k <= 0:
            print(f"Invalid input")
            return
        for i in range(0,k,1):
            curr_sum += arr[i]
        # print(f"Curr sum : {curr_sum}")
        maximum_sum = curr_sum
        for i in range(k,len(arr),1):
            # print(f"Curr sum : {curr_sum} - {arr[i-k]} + {arr[i]} = {curr_sum - arr[i-k] + arr[i]}")
            curr_sum = curr_sum - arr[i-k] + arr[i]
            maximum_sum = max(maximum_sum,curr_sum)
        print(f"Max sum = {maximum_sum}")
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    ob = Solution()
    arr = [1,8,30,-5,20,7]
    ob.max_sum(arr,3)

    arr = [1,-8,30]
    ob.max_sum(arr,3)

    arr = [1,-8]
    ob.max_sum(arr,3)
    
    arr = [1,5,4,2,9,9,9]
    ob.max_sum(arr,3)
# } Driver Code Ends