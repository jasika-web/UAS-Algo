class Sorting:
    @staticmethod
    def selectionSort(array, size):
        for ind in range(size):
            min_index = ind
            for j in range(ind + 1, size):

                if array[j] < array[min_index]:
                    min_index = j

            array[ind], array[min_index] = array[min_index], array[ind]

arr = [1, 9, 72, 5, 35, 111, -23, 2]
size = len(arr)
Sorting.selectionSort(arr, size)
print(arr)
