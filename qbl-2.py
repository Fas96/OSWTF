def solution(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def go():
    usList = solution(437674, 3)
    print(usList)
    zerolIS = []
    count = 0
    LIS = []
    for i in range(1, len(usList) - 1):
        LIS = usList[:i + 1]
        if usList[i - 1] == 0 and usList[i + 1] != 0 and usList[i] != 0:
            count += 1
        if usList[i - 1] != 0 and usList[i + 1] == 0 and usList[i] != 0:
            count += 1

    print(count)
