from multiprocessing import Pool, cpu_count
from analysis import *

if __name__ == '__main__':
    # Python 2
    # N_list = [int(n) for n in input('Number of Elements (Separate with comma): ')]
    # Python 3
    # N_list = [n for n in input('Number of Elements (Separate with blank): ').replace(' ', '').split(',')]
    random_list = []
    N_list = [50000, 100000, 150000, 200000, 250000, 300000]
    N_list.sort(reverse=True)
    for each_N in N_list:
        test_data = list(range(each_N))
        for idx in range(times):
            random.shuffle(test_data)
            random_list.append(copy.deepcopy(test_data))
    pool = Pool(processes=cpu_count())
    pool.map(heap_sort, random_list)
    pool.map(quick_sort, random_list)
    pool.map(selection_sort, random_list)
    pool.map(insertion_sort, random_list)
    pool.map(bubble_sort, random_list)
    pool.close()
    pool.join()
    record.output_report()
