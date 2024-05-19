class Solution:
    def equilibrium(self, arr):
        n = len(arr)
        r_sum = 0
        l_sum = 0
        for i in range(0, n, 1):
            r_sum += arr[i]
        
        for i in range(0, n, 1):
            r_sum -= arr[i]
            if r_sum == l_sum:
                return True
            l_sum += arr[i]

        return False

if __name__ == "__main__":
    solution = Solution()
    arr = [3,4,8,-9,9,7]
    print(solution.equilibrium(arr))