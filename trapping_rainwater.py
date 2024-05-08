
class Solution:
    def trap(self, arr):
        n=len(arr)
        lmax = [0] * n
        rmax = [0] * n
        sum=0
        
        lmax[0] = arr[0]
        for i in range (1,n,1):
            lmax[i] = max(arr[i], lmax[i-1])

        rmax[n-1] = arr[n-1]
        for i in range (n-2,-1,-1):
            rmax[i] = max(arr[i], rmax[i+1])

        print(f"lmax : {lmax}")
        print(f"rmax : {rmax}")
        for i in range (0 , n , 1):
            sum += min(lmax[i],rmax[i]) - arr[i]

        return sum



        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    # arr = [3,0,1,2,5,3,2,5]
    # arr = [2,3,5,0,1,2,5,3,2,5,4,3]
    # arr = [1,2,3]
    # arr = [3,2,1]
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    # arr = [3,2,1,2,1]
    # arr = [4,2,3]
    ob = Solution()
    print(ob.trap(arr))
    # ob.maxProfitGFG(arr)
# } Driver Code Ends