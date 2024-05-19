
import time


class Solution:

    def rearrange(self, arr):
        print(f"Array Before : {arr}")
        print()
        x_position = 0
        for i in range(0, len(arr), 1):
            if arr[i] != 0:
                arr[x_position] = arr[i]
                x_position += 1
                print(f"Array Now  : {arr}",end="\r")
                time.sleep(0.5)

        print()
        print()
        for i in range(x_position, len(arr), 1):
            if arr[i] != 0:
                arr[i] = 0
                print(f"Array Finally  : {arr}",end="\r")
                time.sleep(0.3)


if __name__ == "__main__":
    solution = Solution()
    arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9,2,4,9,0,3,45,0,5,3,0,0,3,4,0,0,0,0,0,0,0,0,3,45,6,7,3,3,5,5,0]
    solution.rearrange(arr)
    print()