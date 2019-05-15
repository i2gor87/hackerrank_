from utils.compute_time import timeit

@timeit
def hourglassSum(arr):
    """
    Given following array, calculate all 16
    hourglass sum.
    -9 -9 -9  1 1 1 
    0 -9  0  4 3 2
    -9 -9 -9  1 2 3
    0  0  8  6 6 0
    0  0  0 -2 0 0
    0  0  1  2 4 0
    Hourglass is represented as
    aaa
     a
    aaa
    Print maximum sum found in arr
    """
    result = []
    _max = 0
    new_iterable = [item for sublist in arr for item in sublist]
    for num in range(0, 22):
        if num in [4, 10, 16, 22, 5, 11, 17, 23]:
            pass
        else:
            hourglass = [new_iterable[num], 
                        new_iterable[num+1], 
                        new_iterable[num+2], 
                        new_iterable[num+7], 
                        new_iterable[num+12], 
                        new_iterable[num+13], 
                        new_iterable[num+14]]
            if _max < sum(hourglass):
                _max = sum(hourglass)
    return _max

failing_test = hourglassSum([
                        [3, 7, -3, 0, 1, 8],
                        [1, -4, -7, -8, -6, 5],
                        [-8, 1, 3, 3, 5, 7],
                        [-2, 4, 3, 1, 2, 7],
                        [2, 4, -5, 1, 8, 4],
                        [5, -7, 6, 5, 2, 8]
                        ])

answer = hourglassSum([
                        [1, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0],
                        [0, 0, 2, 4, 4, 0],
                        [0, 0, 0, 2, 0, 0],
                        [0, 0, 1, 2, 4, 0]])

assert answer==19, 'Something wrong'
assert failing_test==33, "Something wrong"

@timeit
def newHourglass(arr):
    total = 0
    max_total = -1073741824
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (j+2 < 6) and (i+2 < 6):
                total = arr[i][j] + arr[i][j+1] + arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                if max_total < total:
                    max_total = total
    return max_total

failing_test = newHourglass([
                        [3, 7, -3, 0, 1, 8],
                        [1, -4, -7, -8, -6, 5],
                        [-8, 1, 3, 3, 5, 7],
                        [-2, 4, 3, 1, 2, 7],
                        [2, 4, -5, 1, 8, 4],
                        [5, -7, 6, 5, 2, 8]
                        ])

answer = newHourglass([
                        [1, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0],
                        [0, 0, 2, 4, 4, 0],
                        [0, 0, 0, 2, 0, 0],
                        [0, 0, 1, 2, 4, 0]])

assert answer==19, 'Something wrong'
assert failing_test==33, "Something wrong"
