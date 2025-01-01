
class Solution:
    def rearrange(self,arr):
        
        n = len(arr)
        # Initialize index of first minimum 
        # and first maximum element
        max_idx = n - 1
        min_idx = 0
    
        # Store maximum element of array
        max_elem = arr[n-1] + 1
    
        # Traverse array elements
        for i in range(0, n) :
    
            # At even index : we have to put maximum element
            print(f"max_idx = {max_idx}")
            print(f"max_elem = {max_elem}")
            print(f"arr[{max_idx}] = {arr[max_idx]}")
            print(f"arr[{i}] = {arr[i]}")
            if i % 2 == 0 :
                arr[i] += (arr[max_idx] % max_elem ) * max_elem
                max_idx -= 1
    
            # At odd index : we have to put minimum element
            else :
                arr[i] += (arr[min_idx] % max_elem ) * max_elem
                min_idx += 1
        print(arr)
        # array elements back to it's original form
        for i in range(0, n) :
            arr[i] = arr[i] // max_elem 


        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ob = Solution()
    print(arr)
    ob.rearrange(arr)
    print(arr)
    # ob.maxProfitGFG(arr)
# } Driver Code Ends