def solution(s):
    return len(s[:len(s) - 4]) * '*' + s[len(s) - 4:]


def findNumber(arr, k):
    # Write your code here
    if k in arr:
        print("YES")
    else:
        print("NO")


def oddNumbers(l, r):
    answer = []
    for i in range(l, r + 1):
        if (i % 2) != 0:
            answer.append(i)
    return answer


def divisibleSumPairs(n, k, ar):
    ar = [1, 2, 3, 4, 5, 6]
    k = 5
    n = 6
    mak = []
    for i in range(n):
        for j in range(0, i):
            if (ar[i] + ar[j]) % k == 0:
                mak.append([ar[j], ar[i]])

    # print(mak)


# migratoryBirds hacker rank
def migratoryBirds(arr):
    arr = [1, 1, 4, 4, 5, 3]
    arr = sorted(arr)
    dArr = {}

    for i in sorted(arr):
        if i not in dArr:
            dArr[i] = 1
        else:
            dArr[i] += 1

    sorted_tuples = sorted(dArr.items(), key=lambda item: item[1])

    sorted_dict = {k: v for k, v in sorted_tuples}

    ls = sorted_dict.popitem()
    bls = sorted_dict.popitem()

    res = 0
    if ls[1] == bls[1]:
        res = bls[0]
    else:
        res = ls[0]

    return res


def bonAppetit(bill, k, b):

    k= 1
    bill=[3 ,10, 2 ,9]
    b=12
    totalCost = 0
    for i in range(len(bill)):
        if i != k:
            totalCost += bill[i]
    # Write your code here
    if totalCost/2==b:
        print("Bon Appetit")
    else:
        print(int(b-(totalCost/2)))


if __name__ == '__main__':
    bonAppetit([],[],[])
    migratoryBirds([])
    divisibleSumPairs(2, 3, [])
    oddNumbers(3, 9)
