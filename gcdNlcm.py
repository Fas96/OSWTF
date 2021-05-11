from functools import reduce


def getTotalX(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(a, a % b)

    def lcm(a, b):
        return a * b // gcd(a, b)


def pageCount(n, p):
    front = p // 2
    if n % 2 == 1:
        back = (n - p) // 2
    else:
        back = (n - p + 1) // 2
    return min(front, back)


if __name__ == '__main__':
    print(getTotalX(2, 8))
    print(pageCount(7, 4))
