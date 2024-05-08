
class Solution:
    def maxProfit(self, arr):
        profit = 0
        buyIndx=-1
        if len(arr) >= 2:
            for i in range (1,len(arr),1):
                if arr[i] > arr[i-1] and buyIndx == -1:
                    buyIndx = i-1
                    print(f"Buy at {buyIndx}")
                if arr[i] < arr[i-1] and buyIndx != -1:
                    profit_booked = arr[i-1] - arr[buyIndx]
                    profit += profit_booked
                    buyIndx = -1
                    print(f"Sell at {i-1} to book profit of {profit_booked}")
            if buyIndx != -1:
                profit_booked = arr[i] - arr[buyIndx]
                profit += profit_booked
                print(f"Sell at {i} to book profit of {profit_booked}")
            print(f"Total profit : {profit}")
    
    def maxProfitGFG(self, arr):
        profit = 0
        for i in range (1, len(arr), 1):
            if arr[i] > arr[i-1]:
                profit += arr[i] - arr[i-1]
        print(f"Total profit : {profit}")


        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    # arr = [2,5,7]
    # arr = [1,5,3,8,12,7,9]
    # arr = [7,1,5,3,6,4]
    arr = [20,15,10,5,10,20,30,20,10]
    ob = Solution()
    ob.maxProfit(arr)
    # ob.maxProfitGFG(arr)
# } Driver Code Ends