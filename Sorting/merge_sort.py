class Sorting():
    @staticmethod
    def sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            Sorting.sort(left_half)
            Sorting.sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

if __name__ == "__main__":
    arr = [1, 9, 72, 5, 35, 111, -23, 2]
    print("Original array:", arr)
    Sorting.sort(arr)
    print("Sorted array:", arr)