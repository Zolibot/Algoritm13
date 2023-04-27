from random import choice

count = 0


def partition(array, pivot):
    left = [x for x in array if x < pivot]
    center = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return left, center, right


def quicksort(array):
    global count
    count += 1
    if len(array) < 2:
        return array
    else:
        pivot = choice(array)
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


if __name__ == '__main__':
    arr = [9, 7, 8, 6, 5, 4, 3, 2, 1, 0]
    print(quicksort(arr))
    print(count)
