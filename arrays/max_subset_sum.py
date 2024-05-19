
class Solution:
    def maxSubsetSum(self, arr):
        if len(arr) > 0:
            max_sum=arr[0]
            curr_sum=0
            start=0
            end=0
            s=0
            for i in range (0,len(arr),1):

                curr_sum += arr[i]

                if max_sum < curr_sum:
                    max_sum = curr_sum
                    start = s
                    end=i

                if curr_sum <= 0:
                    curr_sum = 0
                    s=i+1

            print(f"Max sum {max_sum}")
            print(f"Start : {start}")
            print(f"End : {end}")
        else:
            return 0

    def maxSubArraySum(self,a):
        max_so_far = a[0]
        max_ending_here = 0
        start = 0
        end = 0
        s = 0

        for i in range(0, len(arr)):

            max_ending_here += a[i]

            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                start = s
                end = i

            if max_ending_here < 0:
                max_ending_here = 0
                s = i+1

        print("Maximum contiguous sum is %d" % (max_so_far))
        print("Starting Index %d" % (start))
        print("Ending Index %d" % (end))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    # arr = [-2,-3,4,-1,-2,-1,15,-15,1,2,15,-3]
    # arr = [-2,-3,4,-1,2,-1]
    arr = [2,-2,2,-2,4]
    # arr = [-20,-3,-4,-10,-20,-10,-10,-3]
    ob = Solution()
    ob.maxSubsetSum(arr)
    ob.maxSubArraySum(arr)
# } Driver Code Ends