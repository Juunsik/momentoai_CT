def solution(arr):
    if len(arr) == 1:
        return [-1]

    min_num = min(arr)
    count = arr.count(min_num)

    for _ in range(count):
        del arr[arr.index(min_num)]
    return arr if arr else [-1]
