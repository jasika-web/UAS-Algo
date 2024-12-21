class Basic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def gcd_extended(self, a, b):
        # Base Case
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.gcd_extended(b % a, a)
        # Update x and y using results of recursive call
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    def compute(self):
        return self.gcd_extended(self.a, self.b)

# Driver code
a, b = 35, 15
extended_euclidean = Basic(a, b)
g, x, y = extended_euclidean.compute()
print("gcd(", a, ",", b, ") = ", g)

