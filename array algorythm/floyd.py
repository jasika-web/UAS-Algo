import math

class Array:
    @staticmethod
    def sign(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        return 0

    @staticmethod
    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    @staticmethod
    def select(arr: list, left: int, right: int, k: int):
        while right > left:
            if right - left > 600:
                n = right - left + 1
                i = k - left + 1
                z = math.log(n)
                s = 0.5 * math.exp(2 * z / 3)
                sd = 0.5 * math.sqrt(z * s * (n - s) / n) * \
                    Array.sign(i - n / 2)
                newLeft = int(max(left, k - i * s / n + sd))
                newRight = int(min(right, k + (n - i) * s / n + sd))
                Array.select(arr, newLeft, newRight, k)
            t = arr[k]
            i = left
            j = right
            Array.swap(arr, left, k)
            if arr[right] > t:
                Array.swap(arr, left, right)
            while i < j:
                Array.swap(arr, i, j)
                i = i + 1
                j = j - 1
                while arr[i] < t:
                    i = i + 1
                while arr[j] > t:
                    j = j - 1

            if arr[left] == t:
                Array.swap(arr, left, j)
            else:
                j = j + 1
                Array.swap(arr, right, j)

            if j <= k:
                left = j + 1
            if k <= j:
                right = j - 1
        return arr[k]


if __name__ == "__main__":
    arr = [7, 3, 4, 0, 1, 6]
    k = 2
    res = Array.select(arr, 0, len(arr) - 1, k - 1)
    print('The {}-th smallest element is {}'.format(k, res))
