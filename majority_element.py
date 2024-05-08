
class Solution:
        
    def findMajorityMoore(self, A):
        print(self.findMajorityMoore.__name__)
        ##### Sub routines #####
        def findCandidate(A):
                maj_index = 0
                count = 1
                for i in range(len(A)):

                    if A[maj_index] == A[i]:
                        count += 1
                    else:
                        count -= 1
                    if count == 0:
                        maj_index = i
                        count = 1
                return A[maj_index]
        
        def isMajority(A, cand):
            count = 0
            for i in range(len(A)):
                if A[i] == cand:
                    count += 1
            if count > len(A)/2:
                return True
            else:
                return False
        #########################
            
        # Find the candidate for Majority
        cand = findCandidate(A)
        # Print the candidate if it is Majority
        if isMajority(A, cand) == True:

            print("Majority found :-",cand)
        else:
            print("No Majority Element")


    def findMajorityHashmap(self,arr):
        print(self.findMajorityHashmap.__name__)
        m = {}
        size = len(arr)
        is_majority_present = False
        for i in range(size):
            if arr[i] in m:
                m[arr[i]] += 1
            else:
                m[arr[i]] = 1
            if m[arr[i]] > size/2:
                print("Majority found :-",arr[i])
                is_majority_present=True
                break
        if not is_majority_present:
            print("No Majority element")

    def findMajorityRecursion(self, arr, low, high):

        def countOccurrence(arr,low,high,majority):
            count = 0
            for i in range (low,high,1):
                if arr[i] == majority:
                    count += 1
            return count
        
        # print (f"low : {low}   high : {high}")

        if low == high:
            return arr[low]
        

        length = high-low + 1
        mid = (high+low) // 2
        leftMaj = self.findMajorityRecursion(arr,low,mid)
        rightMaj = self.findMajorityRecursion(arr,mid+1,high)

        if leftMaj == rightMaj:
            return leftMaj

        leftMajCount = countOccurrence(arr,low,high+1,leftMaj)
        rightMajCount = countOccurrence(arr,low,high+1,rightMaj)

        # print(f"leftMaj : {leftMaj},leftMajCount : {leftMajCount} | rightMaj:{rightMaj},rightMajCount : {rightMajCount}")

        if leftMajCount > length // 2:
            return leftMaj
        
        if rightMajCount > length // 2:
            return rightMaj
        
        #No majority element
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    # arr = [8,6,8,6,4,6,5,6,7,9,11]
    arr = [8,8,6,6,8,6,8,4]
    ob = Solution()
    ob.findMajorityMoore(arr)
    ob.findMajorityHashmap(arr)
    print(f"Majority element using recursion : {ob.findMajorityRecursion(arr, 0, len(arr)-1)}")
# } Driver Code Ends