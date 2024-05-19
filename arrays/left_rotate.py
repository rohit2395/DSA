
import time


class Solution:

    def in_place_reverse(self, arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1

    def left_rotate(self, arr, d):
        print(f"Array Before : {arr}")
        n=len(arr)
        self.in_place_reverse(arr,0,d-1)
        self.in_place_reverse(arr,d,len(arr)-1)
        self.in_place_reverse(arr,0,len(arr)-1)
        print(f"Array After : {arr}")
    
    def right_rotate(self, arr, d):
        print(f"Array Before : {arr}")
        n=len(arr)
        self.in_place_reverse(arr,0,n-d-1)
        self.in_place_reverse(arr,n-d,len(arr)-1)
        self.in_place_reverse(arr,0,len(arr)-1)
        print(f"Array After : {arr}")



if __name__ == "__main__":
    solution = Solution()
    # arr = [1, 2, 3, 4, 5, 6 ,7]
    # solution.left_rotate(arr,3)
    print("###################")
    arr = [1,2,3,4,5,6]
    solution.right_rotate(arr,11%(len(arr)))