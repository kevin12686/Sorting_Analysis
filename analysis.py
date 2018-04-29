from multiprocessing.managers import BaseManager
from record_collector import Collector
import random
import copy
import time

BaseManager.register('Collector', Collector)
manager = BaseManager()
manager.start()
record = manager.Collector()


def time_analysis(func):
    def do_func(*args, **kwargs):
        print('[INFO] \'{}\' analysis started (N={}).'.format(func.__name__, len(args[0])))
        start_time = time.clock()
        result = func(*args, **kwargs)
        end_time = time.clock()
        total_time = end_time - start_time
        print('[INFO] \'{}\' took {} seconds (N={}).'.format(func.__name__, total_time, len(args[0])))
        record.new_record(func.__name__, len(result), total_time)
        return result

    return do_func


@time_analysis
def bubble_sort(num_list):
    num_len = len(num_list)
    for i in range(num_len - 1):
        for j in range(num_len - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


@time_analysis
def selection_sort(num_list):
    num_len = len(num_list)
    for i in range(num_len - 1):
        min_idx = i
        for j in range(i + 1, num_len):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]
    return num_list


@time_analysis
def insertion_sort(num_list):
    num_len = len(num_list)
    for i in range(1, num_len):
        value = num_list[i]
        while i > 0 and value < num_list[i - 1]:
            num_list[i] = num_list[i - 1]
            i -= 1
        num_list[i] = value
    return num_list


@time_analysis
def quick_sort(num_list):
    def quick(begin, end, array):
        if begin < end:
            i = begin + 1
            j = end
            while True:
                while i < end and array[begin] > array[i]:
                    i += 1
                while j > 0 and array[begin] < array[j]:
                    j -= 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                else:
                    array[begin], array[j] = array[j], array[begin]
                    break
            quick(begin, j - 1, array)
            quick(j + 1, end, array)

    quick(begin=0, end=len(num_list) - 1, array=num_list)
    return num_list


@time_analysis
def heap_sort(num_list):
    def construct(node, node_num, size, num_list):
        while node < node_num:
            left = (node << 1) + 1
            right = (node << 1) + 2
            if right < size:
                if num_list[left] > num_list[right]:
                    MAX = left
                else:
                    MAX = right
            else:
                MAX = left
            if num_list[node] < num_list[MAX]:
                num_list[node], num_list[MAX] = num_list[MAX], num_list[node]
                node = MAX
            else:
                break

    size = len(num_list)
    node_num = size >> 1
    for i in range(node_num - 1, -1, -1):
        construct(i, node_num, size, num_list)
    while size > 1:
        num_list[0], num_list[size - 1] = num_list[size - 1], num_list[0]
        size -= 1
        node_num = size >> 1
        construct(0, node_num, size, num_list)
    return num_list


if __name__ == '__main__':
    N = 10000
    print('N:{}'.format(N))

    r = list(range(N))
    random.shuffle(r)

    a = bubble_sort(copy.deepcopy(r))
    b = selection_sort(copy.deepcopy(r))
    c = insertion_sort(copy.deepcopy(r))
    d = quick_sort(copy.deepcopy(r))
    e = heap_sort(copy.deepcopy(r))
    print('Sorted Correct: {}'.format(a == b == c == d == e == list(range(N))))

    record.output_report()
