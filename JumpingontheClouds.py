def jumpingOnClouds(c):
    same = []
    diff = list(set(c))
    print([i for i, val in enumerate(c) if val == 1])
    for v in diff:
        same.append([i for i, val in enumerate(c) if val == v])
    return len(same[0]) - 1


def rotLeft(a, d):
    res = a.copy()
    for k in range(0, len(a)):
        res[k - d] = a[k]

    # simplified way to rotate a list
    # print(a[d:]+a[:d])


if __name__ == '__main__':
    rotLeft([1, 2, 3, 4, 5], 1)
