class Array:
    def __init__(self, size):
        self.data = [0] * size

    def __setitem__(self, index, value):
        self.data[index] = value

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)


def compute_lps(pattern):
    """
    Fungsi untuk menghitung Longest Prefix Suffix (LPS) array
    """
    m = len(pattern)
    lps = Array(m)
    j = 0

    lps[0] = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    Fungsi untuk mencari pattern dalam text menggunakan algoritma KMP
    """
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    i = 0
    j = 0

    result = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


text = "ababcabcabababd"
pattern = "ababd"

result = kmp_search(text, pattern)
print("Pattern found at Index:", result)
