from analysis import *
from multiprocessing import Process, Semaphore, cpu_count

global_semaphore = Semaphore(cpu_count())


def critical_section(func, *args, **kwargs):
    global_semaphore.acquire()
    func(*args, **kwargs)
    global_semaphore.release()


if __name__ == '__main__':
    # Python 2
    # N_list = [int(n) for n in input('Number of Elements (Separate with comma): ')]
    # Python 3
    # N_list = [n for n in input('Number of Elements (Separate with blank): ').replace(' ', '').split(',')]
    random_list = []
    process_list = []
    N_list = [50000, 100000, 150000, 200000, 250000, 300000]
    N_list.sort(reverse=True)
    for each_N in N_list:
        test_data = list(range(each_N))
        for idx in range(times):
            random.shuffle(test_data)
            random_list.append(copy.deepcopy(test_data))
            bub = Process(target=critical_section, args=(bubble_sort, random_list[-1]))
            sel = Process(target=critical_section, args=(selection_sort, random_list[-1]))
            ins = Process(target=critical_section, args=(insertion_sort, random_list[-1]))
            qui = Process(target=critical_section, args=(quick_sort, random_list[-1]))
            hea = Process(target=critical_section, args=(heap_sort, random_list[-1]))
            process_list.append(bub)
            process_list.append(sel)
            process_list.append(ins)
            process_list.append(qui)
            process_list.append(hea)
    for each_process in process_list:
        each_process.start()
    for each_process in process_list:
        each_process.join()
    record.output_report()
