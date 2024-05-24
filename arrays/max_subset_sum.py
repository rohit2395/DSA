
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

    def onlyMaxSubArraySum(seld,arr):
        N = len(arr)
        max_sum = arr[0]
        current_sum = arr[0]
        for i in range(1,N,1):
            current_sum = max(current_sum+arr[i],arr[i])
            max_sum = max(max_sum,current_sum)
        print("Maximum contiguous sum is %d" % (max_sum))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":

    ob = Solution()
    print()
    print("#############################################")
    print()
    arr = [-2,-3,4,-1,-2,-1,15,-15,1,2,15,-3]
    print(arr)
    print("---------------------------------------------")
    ob.maxSubsetSum(arr)
    print("---------------------------------------------")
    ob.maxSubArraySum(arr)
    print("---------------------------------------------")
    ob.onlyMaxSubArraySum(arr)
    print()
    print("#############################################")
    print()
    arr = [-2,-3,4,-1,2,-1]
    print(arr)
    print("---------------------------------------------")
    ob.maxSubsetSum(arr)
    print("---------------------------------------------")
    ob.maxSubArraySum(arr)
    print("---------------------------------------------")
    ob.onlyMaxSubArraySum(arr)
    print()
    print("#############################################")
    print()
    arr = [2,-2,2,-2,4]
    print(arr)
    print("---------------------------------------------")
    ob.maxSubsetSum(arr)
    print("---------------------------------------------")
    ob.maxSubArraySum(arr)
    print()
    ob.onlyMaxSubArraySum(arr)
    print()
    print("#############################################")
    print()
    arr = [-20,-3,-4,-10,-20,-10,-10,-3]
    print(arr)
    print("---------------------------------------------")
    ob.maxSubsetSum(arr)
    print("---------------------------------------------")
    ob.maxSubArraySum(arr)
    print("---------------------------------------------")
    ob.onlyMaxSubArraySum(arr)
    print()
    print("#############################################")
    print()
    arr = [-5, -3, -6, -2]
    print(arr)
    print("---------------------------------------------")
    ob.maxSubsetSum(arr)
    print("---------------------------------------------")
    ob.maxSubArraySum(arr)
    print("---------------------------------------------")
    ob.onlyMaxSubArraySum(arr)
    print()
    print("#############################################")
# } Driver Code Ends