import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Collector(object):

    def __init__(self):
        super(Collector, self).__init__()
        self.record = dict()

    def new_record(self, sort, n, t):
        try:
            self.record[n]
        except KeyError:
            self.record[n] = dict()
        try:
            temp = self.record[n][sort]
        except KeyError:
            temp = self.record[n][sort] = list()
        temp.append(t)

    def output_report(self):
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
            plt.title('{} Figure'.format(fig_name).upper())
            plt.savefig(fig_name)
            plt.close()

        plt.figure(0)
        plt.xlabel('# of elements (1000\'s)')
        plt.ylabel('Time (seconds)')
        plt.title('Sorting Performance Figure'.upper())
        plt.legend()
        plt.savefig('Sorting Performance Figure')
        plt.close()


if __name__ == '__main__':
    pass
