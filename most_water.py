class Solution:
    def maxArea(self, height) -> int:
        x=0
        y=len(height)-1
        maxWater=0
        a=0
        b=0
        while(x < y):
            h = height[x] if height[y] > height[x] else height[y]
            w = y-x
            if maxWater < (h*w):
                maxWater = h*w
                a=x
                b=y
            if height[x] < height[y]:
                x += 1
            else:
                y -= 1
        print(f"Maxium water will be stored between {a} and {b} with area {maxWater}")
        return maxWater
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    arr = [1,8,6,2,5,4,8,3,7]
    ob = Solution()
    ob.maxArea(arr)
# } Driver Code Ends