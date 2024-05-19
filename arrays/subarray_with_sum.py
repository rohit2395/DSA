class Solution:
    def sum(self, arr, k):
        print(f"Input array : {arr}")
        start = 0
        sum = 0
        count = 0;
        for end in range(0, len(arr), 1):
            sum += arr[end]
            while sum > k:
                sum -= arr[start]
                start += 1
                count += 1
            if sum == k:
                print(f"Subarray from {start} to {end} has sum {k} | {count}")
                return
            count += 1
        print(f"There is no subarray with sum {k} | {count}")

if __name__ == "__main__":
    solution = Solution()

    arr = [1, 4, 20, 3, 10, 5]
    solution.sum(arr,33)
    print()
    arr = [1, 4, 0, 0, 3, 10, 5]
    solution.sum(arr,7)
    print()
    arr = [2, 4]
    solution.sum(arr,3)
    print()
    arr = [1,280,3,280,5,280,7,280,9,280,250]
    solution.sum(arr,250)