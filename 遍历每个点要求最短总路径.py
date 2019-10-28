# 最小生成树算法原理简述述
# 从所有一个端点在生成树上，另一个端点不在生成树上的
# 边中选择权最小的加入到生成树中，直到所有点都在树中


def quan(n, k, v):
    # 函数返回n节点到k节点的距离
    return v[n - 1][k - 1]


def link(n, v):  # 找出连接到该节点的点
    k = []
    for x in range(len(v)):
        if v[n - 1][x] != 0:
            k.append(x + 1)
    return k


def execute(v):
    # 查找最小生成树方	法，返回生成树路径长度和具体连线方式
    result = [0]
    # result[0]保存总路径长度
    s = [1]
    while len(s) != len(v):
        mindist = float('inf')
        linkrote = None
        for test in s:
            for node in link(test, v):
                if node not in s and quan(test, node, v) < mindist:
                    mindist = quan(test, node, v)
                    linkrote = [test, node]
        s.append(linkrote[1])
        result[0] = result[0] + mindist
        result.append(linkrote)
    return result


tu = [
    [0, 5, 10, 14, 0],
    [5, 0, 15, 0, 0],
    [10, 15, 0, 0, 12],
    [14, 0, 0, 0, 3],
    [0, 0, 12, 3, 0],
]
print(execute(tu))
# print(v[2][1])
