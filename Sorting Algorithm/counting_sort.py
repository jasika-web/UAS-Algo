class Sorting():
    def countingSort(arr):
        max_val = max(arr)
        count = [0] * (max_val + 1)

        while len(arr) > 0:
            num = arr.pop(0)
            count[num] += 1

        for i in range(len(count)):
            while count[i] > 0:
                arr.append(i)
                count[i] -= 1

        return arr

    unsortedArr = [1, 9, 72, 5, 35, 111, -23, 2]
    sortedArr = countingSort(unsortedArr)
    print("Sorted array:", sortedArr)