from collections import Counter


def solution(v):
    answer = []
    rectangle = [v[0], v[1], v[2]]
    xValues = [p[0] for p in rectangle]
    yValues = [p[1] for p in rectangle]

    print(xValues, yValues)

    missingX = [mp for mp in xValues if xValues.count(mp) == 1][0]
    missingY = [mp for mp in yValues if yValues.count(mp) == 1][0]

    answer = [missingX, missingY]

    return answer


def cointPair(n, ar):
    ar = sorted(ar)
    same = []
    diff = list(set(ar))
    ckcount = 0
    for v in diff:
        same.append([val for i, val in enumerate(ar) if val == v])

    for n in same:
        if len(n) >= 2:
            ckcount += (len(n) // 2)

    return ckcount


if __name__ == '__main__':
    # print(solution([[1, 4], [3, 4], [3, 10]]))
    print(cointPair(100,
                    [50, 49, 38, 49, 78, 36, 25, 96, 10, 67, 78, 58, 98, 8, 53, 1, 4, 7, 29, 6, 59, 93, 74, 3, 67, 47,
                     12, 85, 84, 40, 81, 85, 89, 70, 33, 66, 6, 9, 13, 67, 75, 42, 24, 73, 49, 28, 25, 5, 86, 53, 10,
                     44, 45, 35, 47, 11, 81, 10, 47, 16, 49, 79, 52, 89, 100, 36, 6, 57, 96, 18, 23, 71, 11, 99, 95, 12,
                     78, 19, 16, 64, 23, 77, 7, 19, 11, 5, 81, 43, 14, 27, 11, 63, 57, 62, 3, 56, 50, 9, 13, 45]))
