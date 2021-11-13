import matplotlib.pyplot as plt
plt.style.use('dark_background')

def collatz(initial):
    n = 0
    u = initial

    res = []

    while u != 1:
        if u % 2 == 0:
            u = u / 2
        else:
            u = 3 * u + 1
        res.append(u)

    return res



x = collatz(4)
print(x)
plt.plot(x)
plt.show()