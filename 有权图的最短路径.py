# 求有向权图的最短路径算法原理简述
#
#


def link(n, v):  # 找出连接到该节点的点
    k = []
    for x in range(len(v)):
        if v[n - 1][x] != 0:
            k.append(x + 1)
    return k


def quan(n, k, v):  # 函数返回n节点到k节点的距离
    return v[n - 1][k - 1]


def initDist(v):
    dist = {}
    for i in range(len(v)):
        dist[i + 1] = float('inf')
    return dist


def distance(s, e, v):  # 函数返回从s节点开始到e节点的最短路径
    # knowed = []  # 保存已经遍历的节点
    dist = initDist(v)  # 节点为键,到开始节点的距离为值
    rote = {s: [s]}  # 保存路线

    queue = []  # 遍历队列
    dist[s] = 0
    queue.append(s)
    # knowed.append(s)
    while len(queue) != 0:
        n = queue.pop(0)
        temp = rote[n]
        for i in link(n, v):
            # if (i not in knowed) or (dist[i] > dist[n] + quan(n, i,v)):
            if dist[i] > (dist[n] + quan(n, i, v)):
                queue.append(i)
                # knowed.append(i)
                t = temp.copy()
                t.append(i)
                rote[i] = t
                dist[i] = dist[n] + quan(n, i, v)
    return dist[e], rote[e]


if __name__ == '__main__':
    tu = [
        [0, 5, 10, 14, 0],
        [5, 0, 15, 0, 0],
        [10, 15, 0, 0, 12],
        [14, 0, 0, 0, 3],
        [0, 0, 12, 3, 0],
    ]
    # tu = [
    # 	[0, 5, 10, 14, 0],
    # 	[5, 0, 15, 0, 0],
    # 	[10, 15, 0, 0, 12],
    # 	[14, 0, 0, 0, 3],
    # 	[0, 0, 12, 3, 0],
    # ]

    print(distance(1, 5, tu))
