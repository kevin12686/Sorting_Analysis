import random
import copy
import timeit


def time_analysis(func):
    def do_func(*args, **kwargs):
        print('[INFO] \'{}\' analysis started.'.format(func.__name__))
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        print('[INFO] \'{}\' took {} seconds.'.format(func.__name__, end_time - start_time))
        return result

    return do_func


def generate_random_list(size):
    random_list = list(range(size))
    for i in range(size):
        r = random.randrange(size)
        temp = random_list[i]
        random_list[i] = random_list[r]
        random_list[r] = temp
    return list(range(size)), random_list


@time_analysis
def bubble_sort(num_list):
    num_len = len(num_list)
    for i in range(num_len - 1):
        for j in range(num_len - i - 1):
            if num_list[j] > num_list[j + 1]:
                temp = num_list[j]
                num_list[j] = num_list[j + 1]
                num_list[j + 1] = temp
    return num_list


@time_analysis
def selection_sort(num_list):
    num_len = len(num_list)
    for i in range(num_len - 1):
        min_idx = i
        for j in range(i + 1, num_len):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        temp = num_list[i]
        num_list[i] = num_list[min_idx]
        num_list[min_idx] = temp
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
    num_len = len(num_list)
    pass


@time_analysis
def heap_sort(num_list):
    num_len = len(num_list)
    pass


if __name__ == '__main__':
    s, r = generate_random_list(300000)
    a = bubble_sort(copy.deepcopy(r))
    b = selection_sort(copy.deepcopy(r))
    c = insertion_sort(copy.deepcopy(r))
    print(s == a == b == c)
