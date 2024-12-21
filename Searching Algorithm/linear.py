class Searching():
    def linear_search(arr, target):
        for index in range(len(arr)):
            if arr[index] == target:
                return index
        return -1

    arr = [10, 23, 45, 70, 11, 15]
    target = 70

    result = linear_search(arr, target)

    if result != -1:
        print(f"Element {result} found at index: {result}")
    else:
        print("Element {result} not found in the array")