import random


def quick_sort(num_list):
    def quick(begin, end, array):
        i = begin + 1
        j = end
        print('i: {}, j:{}'.format(i, j))
        while i < j:
            while i <= end and begin > array[i]:
                i += 1
            while j > -1 and begin < array[j]:
                j -= 1
            array[i], array[j] = array[j], array[i]
        array[begin], array[j] = array[j], array[begin]
        quick(begin, j - 1, array)
        quick(begin, j + 1, array)

    quick(begin=0, end=len(num_list) - 1, array=num_list)
    return num_list


if __name__ == '__main__':
    test = list(range(9))
    random.shuffle(test)
    ans = quick_sort(test)
    print(ans)
