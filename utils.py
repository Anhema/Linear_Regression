import math

def mean(arr: list[int]):
    sum: int = 0

    for n in arr:
        sum += n
    return sum / len(arr)


def median(arr: list[int]):
    arr.sort()
    return arr[int(len(arr) / 2)]


def mode(arr: list[int]):
    dic = {}
    n: int = 0

    for i in arr:
        if not i in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for g, j in dic.items():
        if j == max(dic.values()):
            n = g;

    return n


def standard_derivation(arr: list[int]):
    m: int = mean(arr)
    sum: int = 0

    for i in arr:
        sum += (i - m)**2

    return math.sqrt(sum / len(arr))


def percentile(arr: list[int], perc: int):
    return sorted(arr)[int(math.ceil((len(arr) * perc) / 100)) - 1]
