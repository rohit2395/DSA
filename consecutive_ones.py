
class Solution:
    def countMaxOnes(self, arr):
        m = 0
        c = 0
        for i in range (0,len(arr),1):
            if arr[i] != 1:
                m = max(m,c)
                c = 0
            else:
                c += 1
        
        return max(m,c)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    # arr = [0,1,1,0,1,1,1,0,1,1,1,1,0,0,1]
    # arr = [0,0,0]
    arr = [1,1,1,1]
    ob = Solution()
    print(ob.countMaxOnes(arr))
# } Driver Code Ends