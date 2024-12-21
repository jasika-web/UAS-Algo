class Sorting:
    @staticmethod
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    @staticmethod
    def quicksort(array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = Sorting.partition(array, low, high)
            Sorting.quicksort(array, low, pivot_index - 1)
            Sorting.quicksort(array, pivot_index + 1, high)


if __name__ == "__main__":
    my_array = [1, 9, 72, 5, 35, 111, -23, 2]
    print("Original array:", my_array)
    Sorting.quicksort(my_array)
    print("Sorted array:", my_array)