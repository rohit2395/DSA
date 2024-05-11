
class Solution:
    def flip(self, arr,n):
        count = 0
        flag = 0
        for i in range (0, n, 1):
            if arr[i] != arr[0] and flag == 0:
                print(f"From {i}", end = " ")
                flag = 1
            elif arr[i] == arr[0] and flag != 0:
                print(f"To {i-1}")
                flag = 0
                count += 1
            if i == n-1 and flag != 0:
                print(f"To {i}")
                count += 1
        print(f"Total flips : {count}")

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    
    ob = Solution()
    arr = [1,0,0,0,1,0,0,1,1,1,1]
    print(arr)
    ob.flip(arr,len(arr))
    arr = [1,1,1,1,1,0,0]
    print(arr)
    ob.flip(arr,len(arr))
    arr = [1,1,1,1,1]
    print(arr)
    ob.flip(arr,len(arr))
    arr = [0,0,1,1,1,1,1,0,0]
    print(arr)
    ob.flip(arr,len(arr))
# } Driver Code Ends