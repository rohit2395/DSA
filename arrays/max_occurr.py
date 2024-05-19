#https://www.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/video/NzU4OQ%3D%3D

class Solution:

    def max_occur(self, left, right, N):
        print(f"Left => {left}")
        print(f"Right => {right}")
        MAX = 10
        freq = [0] * MAX
        for i in range(0, N, 1):
            freq[left[i]] += 1
            freq[right[i]+1] -= 1
        res = 0     
        for i in range(1, MAX, 1):
            freq[i] = freq[i-1] + freq[i]
            if freq[i] > freq[res]:
                res = i;    
        print(f"[DEBUG] Freq array => {freq}")
        print(f"The maximum occurring element is {res}")

if __name__ == "__main__":
    solution = Solution()
    left = [1, 2, 4]
    right = [4, 5, 7]
    solution.max_occur(left,right,3)
    left = [1,2,2]
    right = [5,3,4]
    solution.max_occur(left,right,3)
    print()