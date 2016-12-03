import random


def insertsort(arr):  # 插入排序
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] < temp:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    return arr


def shellsort(arr):  # 希尔排序
    step = len(arr) // 2
    while step > 0:
        for i in range(step, len(arr)):
            temp = arr[i]
            j = i
            while j > 0 and temp > arr[j - step]:
                arr[j] = arr[j - step]
                j = j - step
            arr[j] = temp
        step = step // 2
    return arr


if __name__ == '__main__':
    unsortlist = []
    for x in range(100):
        unsortlist.append(random.random())
        # 将list赋值为一串随机数

    # unsortlist = [2, 3, 1, 4]
    print(unsortlist)

    sortedlist = shellsort(unsortlist)
