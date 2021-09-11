def solution(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


if __name__ == '__main__':
    usList = solution(437674, 3)

    print(usList)
    count = 0
    for i in range(1, len(usList) - 1):
        if usList[i - 1] == 0 and usList[i + 1] == 0 and usList[i] != 0:
            print(usList[i])
        if usList[i]!=0 and usList[i+1]==0:
            print(usList[i])
        if usList[i]!=0 and usList[i-1]==0:
            print(usList[i])



