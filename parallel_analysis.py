from multiprocessing import Pool
from analysis import *


def bubble_sort_parallel(*args, **kwargs):
    return bubble_sort(*args, **kwargs)


def selection_sort_parallel(*args, **kwargs):
    return selection_sort(*args, **kwargs)


def insertion_sort_parallel(*args, **kwargs):
    return insertion_sort(*args, **kwargs)


def quick_sort_parallel(*args, **kwargs):
    return quick_sort(*args, **kwargs)


def heap_sort_parallel(*args, **kwargs):
    return heap_sort(*args, **kwargs)


if __name__ == '__main__':
    # Python 2
    # N_list = [int(n) for n in input('Number of Elements (Separate with comma): ')]
    # Python 3
    # N_list = [n for n in input('Number of Elements (Separate with blank): ').replace(' ', '').split(',')]
    N_list = [1000, 2000, 3000, 4000, 5000]
    N_list.sort(reverse=True)
    pool = Pool(processes=5)
    for each_N in N_list:
        test_data = list(range(each_N))
        for idx in range(times):
            random.shuffle(test_data)
            a = pool.apply_async(bubble_sort_parallel, (copy.deepcopy(test_data),))
            b = pool.apply_async(selection_sort_parallel, (copy.deepcopy(test_data),))
            c = pool.apply_async(insertion_sort_parallel, (copy.deepcopy(test_data),))
            d = pool.apply_async(quick_sort_parallel, (copy.deepcopy(test_data),))
            e = pool.apply_async(heap_sort_parallel, (copy.deepcopy(test_data),))
    pool.close()
    pool.join()
    record.output_report()
