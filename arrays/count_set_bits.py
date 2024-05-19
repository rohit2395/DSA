#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBitsRec(self,n):
        print("n == " + str(n))
        if n <= 1:
            return 0
        i=0 #total bits in n
        x=2
        while(x<=n):
            x*=2
            i+=1
        x=x/2
        i-=1
        print("x == " + str(x))
        if n == x:
            return (int(x/2))*(i+1)
        else:
            return n-x + self.countSetBitsRec(x) + self.countSetBitsRec(n-x)
            
    def countSetBits(self,n):
        # code here
        return self.countSetBitsRec(n+1)
            
        # return the count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    ob=Solution()
    print(ob.countSetBits(10))
# } Driver Code Ends