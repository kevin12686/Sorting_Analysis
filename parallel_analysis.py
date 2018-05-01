from multiprocessing import Pool, Value
from analysis import *

status = Value('B', False)


def bubble_sort_parallel(*args, **kwargs):
    while not status.value:
        time.sleep(0.1)
    return bubble_sort(*args, **kwargs)


def selection_sort_parallel(*args, **kwargs):
    while not status.value:
        time.sleep(0.1)
    return selection_sort(*args, **kwargs)


def insertion_sort_parallel(*args, **kwargs):
    while not status.value:
        time.sleep(0.1)
    return insertion_sort(*args, **kwargs)


def quick_sort_parallel(*args, **kwargs):
    while not status.value:
        time.sleep(0.1)
    return quick_sort(*args, **kwargs)


def heap_sort_parallel(*args, **kwargs):
    while not status.value:
        time.sleep(0.1)
    return heap_sort(*args, **kwargs)


if __name__ == '__main__':
    # Python 2
    # N_list = [int(n) for n in input('Number of Elements (Separate with comma): ')]
    # Python 3
    # N_list = [n for n in input('Number of Elements (Separate with blank): ').replace(' ', '').split(',')]
    count = -1
    random_list = []
    N_list = [50000, 100000, 150000, 200000, 250000, 300000]
    N_list.sort(reverse=True)
    pool = Pool(processes=5)
    status.value = False
    for each_N in N_list:
        test_data = list(range(each_N))
        for idx in range(times):
            random.shuffle(test_data)
            random_list.append(copy.deepcopy(test_data))
            count += 1

            pool.apply_async(bubble_sort_parallel, (random_list[count],))
            pool.apply_async(selection_sort_parallel, (random_list[count],))
            pool.apply_async(insertion_sort_parallel, (random_list[count],))
            pool.apply_async(quick_sort_parallel, (random_list[count],))
            pool.apply_async(heap_sort_parallel, (random_list[count],))

    status.value = True
    pool.close()
    pool.join()
    record.output_report()
