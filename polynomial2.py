import numpy as np

class Trinomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def equation(self):
        return f"{self.a}x^2 + {self.b}x + {self.c} = 0"

    def discriminant(self):
        return (self.b**2) - (4 * self.a * self.c)

    def root_number(self):
        d = self.discriminant()
        if d < 0:
            return 0
        elif d == 0:
            return 1
        elif d > 0:
            return 2

    def solutions(self):
        rn = self.root_number()
        if rn == 0:
            return None
        elif rn == 1:
            return -self.b / (2 * self.a)
        elif rn == 2:
            return [
                (-self.b + np.sqrt(self.discriminant())) / (2 * self.a),
                (-self.b - np.sqrt(self.discriminant())) / (2 * self.a)
            ]


try:
    a, b, c = input().split()
    a, b, c = float(a), float(b), float(c)

    trinomial = Trinomial(a, b, c)

    print(
    f"""
---equation---
{trinomial.equation()}
---

---discriminant---
{trinomial.discriminant()}
---

---solutions---
S = {trinomial.solutions()}
---
    """
    )

except:
    print("enter 3 valid terms")