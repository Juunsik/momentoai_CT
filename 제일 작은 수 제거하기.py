def solution(arr):

    del arr[arr.index(min(arr))]
    return arr if arr else [-1]
