arr = [1, 2, 4, 53, 3, 5, 2, 1, 4, 5, 7, 5, 3, 23]

arr2 = [None] * len(arr)

for i, value in enumerate(arr):
    if i > 0:
        arr2[i] = arr[i] - arr[i - 1]
    else:
        arr2[0] = 0

print(arr2)
