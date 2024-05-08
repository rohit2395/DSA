#Rope_pieces
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def maxPieces(self,n,a,b,c):
        # print(n)
        if n == 0 :
            return 0
        if n < 0:
            return -1
        aa =  self.maxPieces(n-a,a,b,c)
        bb =  self.maxPieces(n-b,a,b,c)
        cc =  self.maxPieces(n-c,a,b,c)
        res = max(aa,bb,cc)
        print(n-res)
        if res == -1:
            return res
        else:
            # if res == aa:
            #     print(a)
            # elif res == bb:
            #     print(b)
            # elif res == cc:
            #     print(c)
            return res+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    ob=Solution()
    print(ob.maxPieces(5,2,5,1))
# } Driver Code Ends