#https://www.geeksforgeeks.org/batch/dsa-4/track/DSASP-Arrays/problem/frequency-of-array-elements-1587115620

class Solution:

    def freq(self, arr):
        N = len(arr)
        index = 0
        while(index < N):
            if arr[index] <= 0:
                index += 1
                continue

            # print(f"index = {index}")
            
            x = arr[index]-1
            
            arr[index] = 0 if arr[x] < 0 else arr[x]

            # print(f"x = {x}")
            # print(f"temp = {arr[index]}")
            
            if arr[x] > 0:
                arr[x] = -1
            else:
                arr[x] += -1

            print(" ".join(map(str, arr)))
            print()

        for i in range (0, N, 1):
            arr[i] *= -1
        
        return

if __name__ == "__main__":
    solution = Solution()
    arr = [2, 3, 2, 3, 5]
    solution.freq(arr)
    print("Result : " + " ".join(map(str, arr)))
    print()