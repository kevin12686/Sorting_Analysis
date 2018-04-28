from multiprocessing import Lock
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np


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
        # csv = StringIO()
        plt.style.use('ggplot')
        data = dict()
        for each_n, each_dict in self.record.items():
            for sort, tlist in each_dict.items():
                try:
                    temp = data[sort]
                except KeyError:
                    temp = data[sort] = list()
                temp.append((round(each_n / 1000), round(sum(tlist) / len(tlist))))

        fig_count = len(data) + 1
        fig_idx = 1
        fig_seq = ['all']
        fig_color = [np.random.rand(3) for a in range(fig_count - 1)]

        for each_sort, each_data in data.items():
            temp = np.asarray(each_data).swapaxes(0, 1)
            plt.figure(0)
            plt.plot(temp[0], temp[1], '-o', color=fig_color[fig_idx - 1], label=each_sort.replace('_', ' '))
            plt.figure(fig_idx)
            plt.plot(temp[0], temp[1], '-o', color=fig_color[fig_idx - 1])
            fig_idx += 1
            fig_seq.append(each_sort)

        for idx in range(1, fig_count):
            fig_name = fig_seq[idx].replace('_', ' ')
            plt.figure(idx)
            plt.xlabel('# of elements (1000\'s)')
            plt.ylabel('Time (seconds)')
            plt.title('{} Figure'.format(fig_name))
            plt.savefig(fig_name)
            plt.close()

        plt.figure(0)
        plt.xlabel('# of elements (1000\'s)')
        plt.ylabel('Time (seconds)')
        plt.title('Sorting Performance Figure')
        plt.legend()
        plt.savefig('Sorting Performance Figure')
        plt.close()


if __name__ == '__main__':
    plt.style.use('ggplot')
    plt.plot([50000, 100000, 150000, 200000, 250000, 300000], [1, 3, 4, 5, 2, 1], '-o', color=np.random.rand(3),
             label='test1')
    plt.plot([50000, 100000, 150000, 200000, 250000, 300000], [5, 5, 5, 5, 5, 5], '-o', color=np.random.rand(3),
             label='test2')
    plt.xlabel('haha')
    plt.legend()
    # plt.savefig('a.png')
    plt.show()
