def minimumBribes(q):
    bribes = 0

    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
             print("Too chaotic")
             return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])