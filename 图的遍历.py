def link(n, v):  # 从图v找出n节点连接到的点
    k = []
    for x in range(len(v)):
        if v[n - 1][x] != 0:
            k.append(x + 1)
    return k


def visit(s, v):
    # 从s节点开始遍历这个图
    knowed = [s]
    visitqueue = [s]
    knowed.append(1)
    # knowed = [s, ]
    # visitqueue = [s]
    #            visitqueue.append(1)
    pass
    #     while True:
    #         n = visitQueue.pop(0)
    #         print(n)  # 对节点的操作放在这
    #         for i in link(n, v):
    #             if i not in knowed:  # 未知节点遍历
    #                 knowed.append(i)
    #                 visitQueue.append(i)


if __name__ == '__main__':
    v1 = [
        [0, 1, 0, 1],
        [1, 0, 1, 1],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]
    visit(2, v1)
