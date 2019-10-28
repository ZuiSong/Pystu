# 计算c(n)=2/n*sum(c[0]~c(n-1))+n的最优算法


def eval(n):
    c = 1
    sum = 0
    for i in range(1, n + 1):
        sum = sum + c
        c = 2.0 * sum / i + i
    return c


def feibonaqie(n):  # 计算斐波那契数列的最优算法
    if n == 1 or n == 2:
        return 1
    n1 = 1
    n2 = 1
    f = 0
    for i in range(1, n - 1):
        f = n1 + n2
        n1 = n2
        n2 = f
    return f


print(eval(1))
