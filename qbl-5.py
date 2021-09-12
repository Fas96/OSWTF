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

    print(mak)


if __name__ == '__main__':
    divisibleSumPairs(2, 3, [])
    oddNumbers(3, 9)
