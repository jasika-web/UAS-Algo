class Sorting():
    @staticmethod
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # Recursively heapify the affected sub-tree
            Sorting.heapify(arr, n, largest)

    @staticmethod
    def sort(arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            Sorting.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  
            Sorting.heapify(arr, i, 0)

if __name__ == "__main__":
    arr = [1, 9, 72, 5, 35, 111, -23, 2]
    print("Original array:", arr)
    Sorting.sort(arr)
    print("Sorted array:", arr)