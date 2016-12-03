
def link(n, v):  # 找出连接到该节点的点
    k = []
    for x in range(len(v)):
        if v[n - 1][x] != 0:
            k.append(x + 1)
    return k


def distance(s, e, v):  # 从s节点开始到e节点  函数返回最短路径
    knowed = []
    dist = {}
    queue = []
    dist[s] = 0
    queue.append(s)
    knowed.append(s)
    while len(queue) != 0:
        n = queue.pop(0)
        if n == e:
            return dist[n]
        for i in link(n, v):
            if i not in knowed:
                dist[i] = dist[n] + 1
                queue.append(i)
                knowed.append(i)
    return -1


if __name__ == '__main__':
    tu = [
        [0, 2, 1, 5],
        [2, 0, 4, 3],
        [0, 4, 0, 0],
        [5, 3, 0, 0]]
    print(distance(3, 1, tu))
# print(v[2][1])
