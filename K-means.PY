data = [(1, 2), (1, 1), (1, 3), (5, 5), (6, 4)]

k = 2

maxCalcTimes = 500

classCenter = [data[0], data[1]]

classed = [None] * k

print(classCenter)


def getDis(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


for i in range(maxCalcTimes):
    for x in data:
        for m in range(k):
            getDis(x, classCenter[m])
