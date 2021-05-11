import re


def staircase(n):
    for i in range(1, n + 1):
        s = '#' * i
        print(s.rjust(n))


def frequencyCheck(string):
    d = {}
    for i in string:
        if i not in d.keys():
            d[i] = 0
        d[i] += 1

    print(d)


def frequencyCheckSimplified(string):
    d = {}
    for i in string:
        d[i] = d.get(i, 0) + 1

    print(d)


def groupStrings(s):
    for i in range(1, len(s) // 2 + 1):
        relist = re.sub('(\w{%i)' % i, '\g<1>', s).split()
        print(relist)


def removeOneEach(larr):
    print(list(map(lambda mv: mv - 1, larr)))


def vertexDiff(arrTd):
    print(arrTd[0][0])
    stack = []
    for i in range(1, len(arrTd)):
        add=[]
        for j in range(2):
            add.append(arrTd[0][j] - arrTd[i][j])
        stack.append(add)

    print(stack)


if __name__ == '__main__':
    # groupStrings("This is the new string")

    vertexDiff([[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
