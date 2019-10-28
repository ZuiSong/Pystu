import math


def quadratic_equation(a, b, c):
    # 求解一元二次方程
    d = b * b - 4 * a * c
    if d < 0:
        return "此方程无解"
    derita = math.sqrt(d)
    return (-b + derita) / (2 * a), (-b - derita) / (2 * a)


print(quadratic_equation(2, 3, 1))
print(quadratic_equation(1, -6, 5))

