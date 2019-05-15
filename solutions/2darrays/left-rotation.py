from utils.compute_time import timeit

@timeit
def rotLeft(a, d):
    """
    Left rotation operation on array
    :param a: array of int
    :param d: rotation count 1<x<10^5
    :return: rotated array
    """
    
    arr_len = len(a)
    if arr_len > d:
        k = d
    else:
        k = arr_len%d
    p = a[:k]
    s = a[k:]+p


    return s


simpletest = rotLeft([1, 2, 3, 4, 5], 4)
newtest = rotLeft([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10)

assert simpletest == [5, 1, 2, 3, 4], "Something is wrong"
assert newtest == [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77], "Something is wrong"