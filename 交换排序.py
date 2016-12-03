import random


def sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] < temp:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    return arr


if __name__ == '__main__':
    array = []
    for x in range(10):
        array.append(random.random())
    print(array)

    print(sort(array))
