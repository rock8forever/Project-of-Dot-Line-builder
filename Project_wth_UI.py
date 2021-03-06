import numpy as np
import matplotlib.pyplot as plt


class DotsBuilder:
    def __init__(self, ax):
        self.ax = ax
        self.xs = []
        self.ys = []
        self.cid = ax.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        # print("db", event.xdata, event.ydata) #dbg only
        self.ax.clear()
        if event.xdata is not None or event.ydata is not None:
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
        self.ax.scatter(self.xs, self.ys, c='k', marker='.')
        plt.xlim((0, 100))
        plt.ylim((0, 100))
        plt.draw()


class LineBuilder:
    def __init__(self, ax):
        self.ax = ax
        self.cid = ax.figure.canvas.mpl_connect('button_press_event', self)
        self.a = 1
        self.b = 0

    def __call__(self, event):
        self.a = coeficients(db.xs, db.ys, "a")
        self.b = coeficients(db.xs, db.ys, "b")
        self.ax.plot((0, 100), (self.a * 0 + self.b, self.a * 100 + self.b))


def average(array):
    sum = 0
    for i in array:
        sum += i
    return sum / len(array)


def coeficients(xValues, yValues, mode):
    xmean = average(xValues)
    ymean = average(yValues)
    numerator = 0
    denominator = 0
    a, b = 0, 0
    x = 0
    y = 0
    for i in range(len(xValues)):
        x = xValues[i]
        y = yValues[i]
        numerator += (x - xmean) * (y - ymean)
        denominator += (x - xmean) * (x - xmean)
    if denominator:
        a = numerator / denominator
    b = ymean - a * xmean
    if mode == "a":
        return a
    return b


fig = plt.figure()
ax = fig.add_subplot(111)
db = DotsBuilder(ax)
lb = LineBuilder(ax)
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.show()