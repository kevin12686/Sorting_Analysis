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
    pool = Pool(processes=3)

    N = 5000
    print('N:{}'.format(N))
    r = list(range(N))
    random.shuffle(r)
    a = pool.apply_async(bubble_sort_parallel, (copy.deepcopy(r),))
    b = pool.apply_async(selection_sort_parallel, (copy.deepcopy(r),))
    c = pool.apply_async(insertion_sort_parallel, (copy.deepcopy(r),))
    d = pool.apply_async(quick_sort_parallel, (copy.deepcopy(r),))
    e = pool.apply_async(heap_sort_parallel, (copy.deepcopy(r),))

    N = 10000
    print('N:{}'.format(N))
    r = list(range(N))
    random.shuffle(r)
    a = pool.apply_async(bubble_sort_parallel, (copy.deepcopy(r),))
    b = pool.apply_async(selection_sort_parallel, (copy.deepcopy(r),))
    c = pool.apply_async(insertion_sort_parallel, (copy.deepcopy(r),))
    d = pool.apply_async(quick_sort_parallel, (copy.deepcopy(r),))
    e = pool.apply_async(heap_sort_parallel, (copy.deepcopy(r),))

    N = 15000
    print('N:{}'.format(N))
    r = list(range(N))
    random.shuffle(r)
    a = pool.apply_async(bubble_sort_parallel, (copy.deepcopy(r),))
    b = pool.apply_async(selection_sort_parallel, (copy.deepcopy(r),))
    c = pool.apply_async(insertion_sort_parallel, (copy.deepcopy(r),))
    d = pool.apply_async(quick_sort_parallel, (copy.deepcopy(r),))
    e = pool.apply_async(heap_sort_parallel, (copy.deepcopy(r),))

    N = 20000
    print('N:{}'.format(N))
    r = list(range(N))
    random.shuffle(r)
    a = pool.apply_async(bubble_sort_parallel, (copy.deepcopy(r),))
    b = pool.apply_async(selection_sort_parallel, (copy.deepcopy(r),))
    c = pool.apply_async(insertion_sort_parallel, (copy.deepcopy(r),))
    d = pool.apply_async(quick_sort_parallel, (copy.deepcopy(r),))
    e = pool.apply_async(heap_sort_parallel, (copy.deepcopy(r),))

    N = 25000
    print('N:{}'.format(N))
    r = list(range(N))
    random.shuffle(r)
    a = pool.apply_async(bubble_sort_parallel, (copy.deepcopy(r),))
    b = pool.apply_async(selection_sort_parallel, (copy.deepcopy(r),))
    c = pool.apply_async(insertion_sort_parallel, (copy.deepcopy(r),))
    d = pool.apply_async(quick_sort_parallel, (copy.deepcopy(r),))
    e = pool.apply_async(heap_sort_parallel, (copy.deepcopy(r),))

    N = 30000
    print('N:{}'.format(N))
    r = list(range(N))
    random.shuffle(r)
    a = pool.apply_async(bubble_sort_parallel, (copy.deepcopy(r),))
    b = pool.apply_async(selection_sort_parallel, (copy.deepcopy(r),))
    c = pool.apply_async(insertion_sort_parallel, (copy.deepcopy(r),))
    d = pool.apply_async(quick_sort_parallel, (copy.deepcopy(r),))
    e = pool.apply_async(heap_sort_parallel, (copy.deepcopy(r),))

    pool.close()
    pool.join()

    # print('Sorted Correct: {}'.format(a.get() == b.get() == c.get() == d.get() == e.get() == list(range(N))))
    record.output_report()
