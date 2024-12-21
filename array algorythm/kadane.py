class Array():
    def __init__(self, arr):
        self.arr = arr

    # Function to find the sum of subarray with maximum sum
    def maxSubarraySum(self):
        res = self.arr[0]

        # Outer loop for starting point of subarray
        for i in range(len(self.arr)):
            currSum = 0

            # Inner loop for ending point of subarray
            for j in range(i, len(self.arr)):
                currSum = currSum + self.arr[j]

                # Update res if currSum is greater than res
                res = max(res, currSum)

        return res


if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    array_instance = Array(arr)
    print(array_instance.maxSubarraySum())
