
class Solution:
    def leader(self, arr):
        index = len(arr)-1
        curr_lead=arr[index]
        print(curr_lead," ")
        while index >= 0:
            if arr[index] > curr_lead:
                curr_lead = arr[index]
                print(curr_lead," ")
            index -= 1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    arr = [20,7,10,4,3,6,5,2]
    # arr = [-20,-3,-4,-10,-20,-10,-10,-3]
    ob = Solution()
    ob.leader(arr)
# } Driver Code Ends