class Array:
    def __init__(self, arr):
        """
        Initialize the array.
        :param arr: List of elements in the array.
        """
        self.arr = arr

    def partition(self, l, r):
        """
        Standard partition process of QuickSort. It considers the last element as pivot
        and moves all smaller elements to the left of it and greater elements to the right.
        :param l: Left index of the subarray.
        :param r: Right index of the subarray.
        :return: Index of the pivot element after partitioning.
        """
        x = self.arr[r]
        i = l
        for j in range(l, r):
            if self.arr[j] <= x:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[i], self.arr[r] = self.arr[r], self.arr[i]
        return i

    def kth_smallest(self, l, r, k):
        """
        Finds the k-th smallest element in the array using QuickSelect algorithm.
        :param l: Left index of the subarray.
        :param r: Right index of the subarray.
        :param k: The k-th position to find (1-based index).
        :return: The k-th smallest element.
        """
        if 0 < k <= r - l + 1:
            index = self.partition(l, r)

            # If position is same as k
            if index - l == k - 1:
                return self.arr[index]

            # If position is more, recur for left subarray
            if index - l > k - 1:
                return self.kth_smallest(l, index - 1, k)

            # Else recur for right subarray
            return self.kth_smallest(index + 1, r, k - index + l - 1)

        raise IndexError("Index out of bound")


if __name__ == "__main__":
    arr = [10, 4, 5, 8, 6, 11, 26]
    n = len(arr)
    k = 3

    # Create an instance of Array class
    array_instance = Array(arr)

    print("K-th smallest element is", end=" ")
    print(array_instance.kth_smallest(0, n - 1, k))
