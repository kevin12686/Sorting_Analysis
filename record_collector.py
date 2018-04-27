from multiprocessing import Lock
import numpy as np
import matplotlib.pyplot as plt


class Collector(object):

    def __init__(self):
        super(Collector, self).__init__()
        self.record_lock = Lock()
        self.record = dict()

    def new_record(self, sort, n, t):
        self.record_lock.acquire()
        try:
            self.record[n]
        except KeyError:
            self.record[n] = dict()
        try:
            temp = self.record[n][sort]
        except KeyError:
            temp = self.record[n][sort] = list()
        temp.append(t)
        self.record_lock.release()

    def output_report(self):
        x_axis = list()
        y_axis = dict()
        for each_n, each_dict in self.record.items():
            x_axis.append(each_n)
            for sort, tlist in each_dict:
                y_axis[sort] = sum(tlist) / len(tlist)
        for sort, y_value in y_axis.items():
            plt.plot(x_axis, y_value)


if __name__ == '__main__':
    # plt.plot([50000, 100000, 150000, 200000, 250000, 300000], [1, 3, 4, 5, 2, 1], '-v')
    # plt.savefig('a.png')
    print(np.random.rand(10))
