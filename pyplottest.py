import numpy
import matplotlib.pyplot as plt


# x=a(2cost-cos2t) y=a(2sint-sin2t)

def main():
    print('hello')
    t = numpy.arange(0, 15, 0.01)
    t = numpy.array(t)
    print(t)
    x = 2 * numpy.cos(t) - numpy.cos(2 * t)
    y = 2 * numpy.sin(t) - numpy.sin(2 * t)

    print(x, y)
    plt.scatter(y * 0.1, x)
    plt.show()


# 极坐标画图
def theta():
    import numpy as np
    import matplotlib.pyplot as plt
    theta = np.arange(0, 2 * np.pi, 0.002)
    plt.subplot(221, polar=True)
    plt.plot(theta, np.sin(4 * theta), '*')

    plt.subplot(222, polar=True)
    plt.plot(theta, np.sin(5 * theta), '*')

    plt.subplot(223, polar=True)
    plt.plot(theta, np.sin(6 * theta), '*')

    plt.subplot(224, polar=True)
    plt.plot(theta, np.sin(5 * theta))

    plt.show()


if __name__ == '__main__':
    theta()
    main()
