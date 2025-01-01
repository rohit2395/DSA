#User function Template for python3

class Solution:
    result = []
    delta = -5
    orig = 0
    
    def logic(self, N):
        print(N)
        if N > self.orig:
            return
        self.result.append(N)
        if N <= 0:
            self.delta = 5
        self.pattern(N + self.delta)
    
    def pattern(self, N):
        self.orig = N
        self.logic(N)
        return self.result
        
        


17 12 7 2 -3 2 7 12 17
17 12 7 2 -3 2 7 12 17

if __name__ == '__main__':
    ob = Solution()
    ans = ob.pattern(4)
    for i in ans:
        print(i, end = " ")
    print()