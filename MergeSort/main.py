def merge_sort(array):
    if len(array) == 1:  # базовый случай рекурсии
        return array

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: len(array) // 2])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[len(array) // 2: len(array)])

    # заводим массив для результата сортировки
    result = [0] * len(array)

    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


if __name__ == "__main__":
    arr = [4, 5, 1, 9, 2, 7]
    print(merge_sort(arr))



def binary_search(array: List[int], val: int) -> int:
    first = 0
    last = len(array) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if array[mid] == val:
            index = mid
        else:
            if val < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index